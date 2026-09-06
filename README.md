# python-web-content-discovery
A basic Python web content discovery tool that uses HTTP requests and a wordlist to identify potentially accessible web paths.

# Python Web Content Discovery Tool

A basic web content discovery tool built with Python to understand how automated web path enumeration works.

The script uses Python's `requests` library and a wordlist to send HTTP GET requests to potential web paths and identify responses that are different from `404 Not Found`.

As part of this project, I compared the results of my Python implementation with **Gobuster's directory enumeration mode** against the same authorized lab environment.

## Objective

The main objective of this project was to understand the fundamentals behind web content discovery rather than simply using an existing enumeration tool.

I wanted to understand how a tool such as Gobuster can:

- Take a target URL
- Read paths from a wordlist
- Make HTTP requests
- Analyze HTTP response codes
- Identify potentially accessible resources

I then implemented a simplified version of this process using Python.

## How It Works

The Python script:

1. Takes a base URL.
2. Reads potential paths from a wordlist.
3. Constructs URLs using the base URL and each word.
4. Sends an HTTP GET request using the `requests` library.
5. Checks the HTTP response status code.
6. Prints paths that return a status other than `404`.

Example:

```text
Base URL: http://LAB_IP

Wordlist:
admin
login
test
robots.txt
phpinfo.php
```
##The script generates requests such as:

http://LAB_IP/admin
http://LAB_IP/login
http://LAB_IP/test
http://LAB_IP/robots.txt
http://LAB_IP/phpinfo.php

##Technologies Used

Python
Requests library
HTTP
HTTP status codes
Wordlists
Gobuster
Kali Linux

##Example Wordlist

admin
login
dashboard
robots.txt
sitemap.xml
backup
backups
config
test
dev
api
uploads
images
css
js
server-status
phpinfo.php
.git
.env
database
db
old
temp
private
admin.php
login.php

##Testing Environment

The Python script and Gobuster were tested against the same intentionally vulnerable and authorized laboratory environment.

##Gobuster Command

gobuster dir -u http://LAB_IP -w wordlist.txt

##Key Learnings

Through this project, I learned:

How Python's requests library can be used to make HTTP requests.
How HTTP response status codes can provide information about web resources.
How wordlists can automate web content discovery.
How URLs can be generated programmatically.
How request timeouts and exception handling improve reliability.
The basic concept behind web content enumeration.
How a simple Python implementation compares with a dedicated tool such as Gobuster.
Limitations

This is a basic learning implementation.

##Current limitations include:

Sequential requests
Small wordlist
No command-line arguments
No multithreading
Limited response analysis
Basic error handling
No extension enumeration
No advanced filtering
Future Improvements

##Possible improvements include:

Add command-line arguments
Add multithreading
Support custom status-code filtering
Display response size
Add response-time information
Support file extensions
Save results to a file
Improve error handling
Add redirect handling
Ethical Use

This tool should only be used against systems that you own or have explicit permission to test.

Testing for this project was performed in an authorized laboratory environment.

##Author

Chethan M

Computer Science & Engineering – Cyber Security

Presidency University, Bengaluru
