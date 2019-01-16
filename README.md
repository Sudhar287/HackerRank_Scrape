# HackerRank_Scrape
A tool to scrape all your HackerRank submission codes.

## Working
### Requirements:
- Python3+
- Tkinter module
- Selenium module
### Input:
When prompted by the program, the user need to input the HacerRank login credentials (username & password). The user also needs to enter the path to chrome selenium driver.
The program goes into each challenge from the submissions page of the user and scrapes their code. 
The result is stored in a file that has the name: <challenge name>.<langauge>

## To Do
- [ ] Replace Time.Sleep() with Selenium wait functionality
- [ ] Create well defined fucntions for each task
- [ ] Automatically get the submissions pages variable.
- [ ] Handle the StaleElementReferenceException exceptions
- [ ] Functionality to group by subdomains
