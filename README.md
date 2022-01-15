# Getting Started

### Run Application

**Requirements:** <br/>
-  Make Sure python 3 and pip (python package installer) installed on your system to run this project.
-  On root directory of project run: <br/> 
`pip install -r requirements.txt` <br/> 
to install required packages. <br/>
-  Place your git username  under `GIT_USERNAME` and access token (provided by github) under variable `GIT_API_TOKEN` inside file `config.py`. See [git doc](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to know more about this.<br/>
-  Before run application and to test your token please run a unit test placed under directory `/tests/unit_tests.py`. 
-  After that: <br/>
`python app.py` or `python3 app.py`
Open http://127.0.0.1:5000 on browser to see output.

**Note:** <br/>
-  Try to choose repo with less number of stars (recommended: less than 500 stars) as response time on html increases with increased number of stars in repo. 

### Application Structure


─ app<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;─ __init__.py <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;─ github.py <br/>
─ templates<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;─ page.html <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;─ result.html <br/>
─ tests<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;─ __init__.py <br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;─ unit_test.py <br/>
─ csv_downloads<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;─ star-history-probot.csv <br/>
─ app.py<br/>
─ config.py<br/>
─ README.md<br/>
─ requirements.txt<br/>


This is my application structure based on requirements and limited scope. It can be expand in multiple plugins with increased scope.


### Application Description

This application takes github repository (owner/repo_name) from user in html and outputs total number of star counts, history of star count (who gave a star, time/date of star etc.) in table format, line plot/graph to show history of stars of particular repo.

#### Application Approach:

Being an analyst i choose graphical approach for user to analyse how star count history grow with time. Standalone stars history (time, user, urls etc.) is not much informative as takes time and  effort of user to understand. Moreover, on top of that i have provide user to also see star users details in table format and csv.

#### Security Policy and conventions compromised to due time limitations:

- In early commit history, due to limited time frame for this task by mistake i have pushed username and access token which is against security policy and coding conventions. kindly ingore and provide your own username and token while accessing application.
- There should be seperate develop branch for development. 
<br/>
### More things can be doable if spend more time

- Use flask rest-plus framework instead of simple flask to automatically create documentation for APIs or [APIspec](https://github.com/marshmallow-code/apispec) to document APIs and its routes.
- It would be better to create a small docker image of this application and deploy to avoid environment issues. Due to time limitations i couldnt do that.
- More tests can be added for star info in dataframe and graph, csv created in csv_downloads or not, flask api responses etc.
- More error handling by using try catch and if else statements can be add in code.
Pushing all code to main because of limited time
- As sometime dataset might be large so comparison b/w dataframe row insert functions (append, iloc etc) would be helpful in order to make efficient and fast.

### Demo

![Alt text](demo-recording/star-history-recording.gif)