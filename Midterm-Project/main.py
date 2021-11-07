# by Kristen Marcinek, Tiffany Alston, and Scott Mitchell

from bs4 import BeautifulSoup # package 1 
import requests # package 2
import re # package 3

print("Welcome! This program will scrape to find whatever word or phrase you input in my portfolio.")
print("This program is case-sensitive, so make sure you type correctly!")

def scrape(): # function to be ran for output
    userInput = input("Type a word or phrase you would like to find: ") # word to be scraped for
    website = "https://kirbong.github.io/" # Kristen's portfolio
    data = requests.get(website) # allows beautiful soup to send a request to the website
    soup = BeautifulSoup(data.text, "html.parser") # parses the page
    phrase = soup.find_all(string=re.compile('.*{0}.*'.format(userInput))) # scrapes for the word or phrase that the user input
    
    if len(phrase) >= 1: # if >= 1, there is a phrase (1 or more instances)
        print(phrase)
        print (f"{userInput} was found {len(userInput)} times!")
    elif len(phrase) == 0: # if there is no phrase, the length would be 0 (no instances)
        print("Could not find phrase!") 
    else: # exceptions
        pass

scrape() # runs scrape function