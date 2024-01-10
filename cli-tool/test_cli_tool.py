import unittest
from cli_tool import login_with_mfa, crawl_website

class TestCliTool(unittest.TestCase):

    def test_login_with_mfa(self):
        # Test the login_with_mfa function with valid credentials and secret key
        username = 'alice'
        password = 'password123'
        secret = 'JBSWY3DPEHPK3PXP'
        login_url = 'https://www.example.com/login'
        session = login_with_mfa(username, password, secret, login_url)
        self.assertIsNotNone(session)

        # Test the login_with_mfa function with invalid credentials or secret key
        username = 'bob'
        password = 'wrongpassword'
        secret = 'WRONGSECRETKEY'
        login_url = 'https://www.example.com/login'
        session = login_with_mfa(username, password, secret, login_url)
        self.assertIsNone(session)

    def test_crawl_website(self):
        # Test the crawl_website function with a valid session and website URL
        username = 'alice'
        password = 'password123'
        secret = 'JBSWY3DPEHPK3PXP'
        login_url = 'https://www.example.com/login'
        website_url = 'https://www.example.com'
        output_file = 'output.json'
        session = login_with_mfa(username, password, secret, login_url)
        crawl_website(session, website_url, output_file)

        # Check if the output file exists and is not empty
        self.assertTrue(os.path.exists(output_file))
        self.assertTrue(os.path.getsize(output_file) > 0)

        # Test the crawl_website function with an invalid session or website URL
        username = 'bob'
        password = 'wrongpassword'
        secret = 'WRONGSECRETKEY'
        login_url = 'https://www.example.com/login'
        website_url = 'https://www.example.com'
        output_file = 'output.json'
        session = login_with_mfa(username, password, secret, login_url)
        crawl_website(session, website_url, output_file)

        # Check if the output file does not exist or is empty
        self.assertFalse(os.path.exists(output_file))
        self.assertFalse(os.path.getsize(output_file) > 0)

if __name__ == '__main__':
    unittest.main()
