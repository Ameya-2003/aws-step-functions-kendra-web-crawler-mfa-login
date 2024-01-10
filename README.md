🎉**Welcome to the AWS STEP FUNCTION KENDRA WEB CRAWLER CLI_TOOL WITH MFA LOGIN**

📌**A Cli-tool, which includes the code of the master Repo (as specified by the owner)**

1. Created a folder for the cli, ```cli-tool```
2. The folder contains two files, ```cli_tool.py``` ,which contains the main code of cli and ```test_cli_tool.py``` for testing purposes

📌**Here are the clear instructions on how to install and use the CLI tool:**

To install the CLI tool, you need to have Python 3 and pip installed on your system. You also need to clone the main repo and the new repo to your local machine. You can do this by running the following commands in your terminal:

```bash script
# Clone the main repo
git clone https://github.com/aws-samples/aws-step-functions-kendra-web-crawler-search-engine.git

# Clone the new repo
git clone https://github.com/your_username/aws-step-functions-kendra-web-crawler-mfa-login.git

# Change directory to the new repo
cd aws-step-functions-kendra-web-crawler-mfa-login

# Install the required packages
pip install -r requirements.txt
```
📌**To use the CLI tool, you need to have the following information:**

1. Your username and password for the website you want to crawl
2. Your secret key for MFA, which you can generate using an app like Google Authenticator or Authy
3. The URL of the login page of the website
4. The URL of the website to crawl
5. The name of the output file, which will contain the crawled data in JSON format

To run the CLI tool, you need to execute the ```cli_tool.py``` file with the appropriate arguments. You can do this by running the following command in your terminal:

```
# Run the CLI tool with the required arguments
python cli_tool.py -u your_username -p your_password -s your_secret -l login_url -w website_url -o output_file
```
You can also use the ```-h``` or ```--help``` flag to see the usage and help message of the CLI tool:
```
# See the usage and help message of the CLI tool
python cli_tool.py -h

```
📌**Here are some examples and screenshots of using the CLI tool:**

Suppose you want to crawl the website ```https://www.example.com```, which requires login with MFA. You have the following information:

Your username is ```alice```

Your password is ```password123```

Your secret key is ```JBSWY3DPEHPK3PXP```

The URL of the login page is ```https://www.example.com/login```

The name of the output file is ```output.json```

📌**You can run the CLI tool with the following command:**
```
python cli_tool.py -u alice -p password123 -s JBSWY3DPEHPK3PXP -l
https://www.example.com/login -w https://www.example.com -o output.json
```
📌**Here are some unit tests to verify the functionality of the code:**

To write the unit tests, you need to have the ```unittest``` module installed on your system. You can do this by running the following command in your terminal:
```
# Install the unittest module
pip install unittest
```
📌**To run the unit tests, you need to create a file named ```test_cli_tool.py``` in the same directory as the ```cli_tool.py``` file. You can do this by running the following command in your terminal:**
```
# Create the test file
touch test_cli_tool.py

```
📌**You can run the unit tests with the following command in your terminal:**
```
# Run the unit tests
python test_cli_tool.py

```
I hope this will work, as per your suggestion, Thanks for your interest 🙏
