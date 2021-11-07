# Mid-term Project - Package Research


## BeautifulSoup - Kristen
### Package Summary

BeautifulSoup is a Python package that parses and searches web pages, otherwise known as “web scraping.”

### Install and Run Instructions

1. In terminal: `pip install beautifulsoup4`
2. In code: `from bs4 import BeautifulSoup`
3. Hit "run" to run code

### Code

`soup = BeautifulSoup(data.text, "html.parser")`
- Parses the webpage
> Parse is a command for dividing the given program code into a small piece of code for analyzing the correct syntax 

> Source: https://www.educba.com/python-parser/

## Requests - Scott
### Package Summary

Requests is a Python package that allows the user to send HTTP/1.1 easily without the need to manually add query strings.

### Install and Run Instructions

1. In terminal: `pip install requests`
2. In code: `import requests`
3. Hit "run" to run code

### Code

`data = requests.get(website) `
- Allows BeautifulSoup to send a request to the website
> GET is used to request data from a specified resource.

> Source: https://www.w3schools.com/tags/ref_httpmethods.asp 

## Re - Tiffany
### Package Summary

Re is a python package that provides matching operations similar to perl. Regular expressions using backslash characters (‘\’) to indicate special forms.

### Install and Run Instructions

1. In terminal: `pip install re`
2. In code: `import re`
3. Hit "run" to run code

### Code

`phrase = soup.find_all(string=re.compile('.*{0}.*'.format(userInput)))`
> Regular expressions are text matching patterns described with a formal syntax. The patterns are interpreted as a set of instructions, which are then executed with a string as input to produce a matching subset or modified version of the original.

> re includes module-level functions for working with regular expressions as text strings, but it is usually more efficient to compile the expressions your program uses frequently. The compile() function converts an expression string into a RegexObject.

> Source: http://pymotw.com/2/re/

## Future Ideas

- Implement Flask package to convert code into a webpage
- How to further implement/use Requests package
- How to further implement/use Re package

**Written by Kristen Marcinek, Tiffany Alston, and Scott Mitchell**
