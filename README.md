# automation-report

Python package to generate HTML report of your automation cases and its steps with its valid status.


### Installation
```
$ pip install automation-report
```

### Code Example
```
# Importing package
from automation_report.report import AutomationReport

# Create new object for your first test; Report name is passed as a parameter and report is generated with same name
new_report = AutomationReport("Login Test")

# Use starttest() method to start a new case with its name given as parameter
new_report.starttest("CASE 0001: Test the screen")

# Populate the various steps status with info(), success(), fail() methods for particular case
new_report.info("Page is opened")
new_report.success("Login Successfully")

# End above started case
new_report.endtest()

# Create yet another case as following
new_report.starttest("CASE 0002: Logout")
new_report.info("User is logged in")
new_report.success("Logout link is present")
new_report.fail("User not logged out")
new_report.endtest()

# Use close method to finally complete whole report generation
new_report.close()
```
### Screenshots of report of above code
![Automation Report](https://user-images.githubusercontent.com/12621555/77243942-c3129f00-6c37-11ea-8e2d-3d4195133bfa.png)

![Automation report](https://user-images.githubusercontent.com/12621555/77243945-d3c31500-6c37-11ea-9eaa-67236010b9e5.png)
