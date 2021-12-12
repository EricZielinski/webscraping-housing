# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).
Copied from [CHANGELOG example] (https://gist.github.com/juampynr/4c18214a8eb554084e21d6e288a18a2c)

## 2021-12-11
A lot of refactoring basically.  I will push changes on a more frequent basis.
 
### Added
- This file :D
- Methods in the BS class
- brokers.json example
   
### Changed
- Reworded a lot of variables and class names to make the code more readable and consistent
- Removed the link scraping functionality from the broker class and placed it in its own class
- Reduced complexity of parser search method by using css selectors from BS

### Next todo
- A little more refactoring elsewhere before a context switch

## 2021-12-06
  
First commit.  Basic functionality for a web scraper.
 
### Added
- BeautifulSoup parser to retrieve links of available housing units
- Retrieves relevant data on the housing unit by visiting each link
- Store this data to the MongoDB
- Basic functionality for email alerts that will be important when more brokers are added