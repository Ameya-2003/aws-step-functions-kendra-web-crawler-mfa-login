import requests
import pyotp
import argparse
import json
from aws_step_functions_kendra_web_crawler_search_engine import WebCrawler

# Define the arguments for the CLI tool
parser = argparse.ArgumentParser(description='A CLI tool to crawl a website for which you must first log in with MFA')
parser.add_argument('-u', '--username', type=str, required=True, help='Your username for the website')
parser.add_argument('-p', '--password', type=str, required=True, help='Your password for the website')
parser.add_argument('-s', '--secret', type=str, required=True, help='Your secret key for MFA')
parser.add_argument('-l', '--login_url', type=str, required=True, help='The URL of the login page')
parser.add_argument('-w', '--website_url', type=str, required=True, help='The URL of the website to crawl')
parser.add_argument('-o', '--output_file', type=str, default='output.json', help='The name of the output file')
args = parser.parse_args()

def login_with_mfa(username, password, secret, login_url):
    """
    A function to log in to a website with MFA using requests and pyotp
    :param username: The username for the website
    :param password: The password for the website
    :param secret: The secret key for MFA
    :param login_url: The URL of the login page
    :return: A requests session object if login was successful, None otherwise
    """
    # Create a TOTP object for MFA
    totp = pyotp.TOTP(secret)

    # Initialize a session
    session = requests.Session()

    # This is the form data that the page sends when logging in
    login_data = {
        'username': username,
        'password': password,
        'otp': totp.now(),  # Add the OTP to the form data
    }

    # Authenticate
    r = session.post(login_url, data=login_data)

    # Check if login was successful
    if r.status_code == 200:
        print("Successfully logged in.")
        return session
    else:
        print("Failed to log in.")
        return None

def crawl_website(session, website_url, output_file):
    """
    A function to crawl a website using the webcrawler module from the main repo
    :param session: A requests session object
    :param website_url: The URL of the website to crawl
    :param output_file: The name of the output file
    :return: None
    """
    # Create a webcrawler object
    crawler = WebCrawler(session)
    # Crawl the website
    crawler.crawl(website_url)
    # Save the output to a file
    with open(output_file, 'w') as f:
        json.dump(crawler.output, f, indent=4)
    print(f"Successfully crawled {website_url} and saved the output to {output_file}.")

# Log in to the website with MFA
session = login_with_mfa(args.username, args.password, args.secret, args.login_url)

# If login was successful, crawl the website
if session is not None:
    crawl_website(session, args.website_url, args.output_file)
