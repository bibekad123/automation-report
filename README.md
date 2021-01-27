# automation-report
[![Downloads](https://pepy.tech/badge/automation-report)](https://pepy.tech/project/automation-report)

Python package to generate HTML report of your automation or test cases with:

- Supports multiple test cases and its steps with valid status
- Well displayed chart according to the test results
- Dynamic HTML Report contents, user allowed to modify accordingly


### Installation
```
$ pip install automation-report
```

### Code Example

###### Importing package :
```
from automation_report.report import AutomationReport
```
###### Passing optional 'options' dictionary as parament with following keys
- **LogoImage** : Provide URL of the image
- **MainHeader**: When header text is to be used instead of logo
- **FooterContent**: Provide HTML content to add on the footer section
```
options = {}
#options["LogoImage"] = "logo.png"
options["MainHeader"] = "Automation Report"
options["FooterContent"] = "<a href='#'> Footer link </a>" 
```
 
##### Create new object for your first test with Report name and optional options dictionary
```
new_report = AutomationReport("Login Test", options)
```
##### Use starttest() method to start a new case with its name given as parameter
```
new_report.starttest("CASE 0001: Login to the system")
```

##### Populate the various steps status with info(), success(), fail() methods for particular case
```
new_report.info("Entered email in email field")
new_report.success("Login Successfully:")
```

##### End above started case
```
new_report.endtest()
```

##### Create yet another case as following
```
new_report.starttest("CASE 0002: Logout User")
new_report.info("User is logged in")
new_report.success("Logout link is present")
new_report.fail("User not logged out")
new_report.endtest()
```
##### Use close method to finally complete whole report generation
```
new_report.close()
```
### Screenshots of report of above code:
![Automation Report](https://user-images.githubusercontent.com/12621555/78378665-06362000-75f1-11ea-86aa-7f3ff063cfcf.png)

![Automation report](https://user-images.githubusercontent.com/12621555/78378679-0b936a80-75f1-11ea-84ee-8d5c490a46b9.png)
