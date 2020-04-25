from datetime import datetime
import string
import codecs
import os

class AutomationReport:
    testCaseLinks = ""
    testCasecontent = ""
    now = datetime.now()
    report_file = None
    case_count = 0
    total_pass = 0
    total_fail = 0
    fail_case = False

    def __init__(self, report_name, options={}):
        self.report_name = report_name
        self.report_file = open((self.report_name + ".html"), "w+")
        self.options = options

    def starttest(self, case_name):
        self.fail_case = 0
        self.case_count = self.case_count + 1
        active_class = ""
        if self.case_count == 1:
            active_class = 'active'
        self.testCaseLinks = self.testCaseLinks + \
            "<li class='testname " + \
             active_class + "' id='Test" + str(self.case_count) + "'> <span class='PASS casestatus status-" + str(self.case_count) + "'>PASS</span> <span class ='casename' title='"+ case_name +  "'>" + case_name + "</span></li>"
        self.testCasecontent = self.testCasecontent + \
            "<div id='Test%sSteps' class='case table-responsive'>" % self.case_count
        tableContent = """<table class="table table-hover table-bordered">
                        <thead>
                            <th>Status</th>
                            <th>Message</th>
                        </thead>
                        <tbody>"""
        self.testCasecontent = self.testCasecontent + tableContent

    def endtest(self):
        self.testCasecontent = self.testCasecontent + "\n </tbody>\n</table>\n</div>"
        if self.fail_case == True:
            self.total_fail = self.total_fail + 1

    def success(self, message):
        self.testCasecontent = self.testCasecontent + \
            "<tr class='table-success'><td><i><b>SUCCESS</b></i></td><td> %s </td></tr>\n" % message

    def fail(self, message):
        self.fail_case = True
        self.testCaseLinks = self.testCaseLinks.replace(
            "'PASS casestatus status-" + str(self.case_count) + "'>PASS",
            "'FAIL casestatus status-" + str(self.case_count) + "'>FAIL")
        self.testCasecontent = self.testCasecontent + \
            "<tr class='table-danger'><td><i><b>FAIL</b></i></td><td> %s </td></tr>\n" % message

    def info(self, message):
        self.testCasecontent = self.testCasecontent + \
            "<tr class='table-info'><td><i><b>INFO</b></i></td><td> %s </td></tr>\n" % message

    def close(self):
        __location__ = os.path.realpath(os.path.join(
            os.getcwd(), os.path.dirname(__file__)))
        source_report_file = codecs.open(os.path.join(
            __location__, 'html_source/report.html'), 'r', 'utf-8')
        allcontent = source_report_file.read()
        allcontent = allcontent.replace('%testCaseLinks%', self.testCaseLinks)
        allcontent = allcontent.replace(
            '%testCasecontent%', self.testCasecontent)
        allcontent = allcontent.replace(
            '%headTitle%', self.report_name + " | automation-report")
        allcontent = allcontent.replace('%totalCases%', str(self.case_count))
        total_pass = self.case_count - self.total_fail
        allcontent = allcontent.replace(
            '%passedCases%', str(total_pass))
        allcontent = allcontent.replace('%failedCases%', str(self.total_fail))
        passedPercent = (total_pass / self.case_count) * 100
        allcontent = allcontent.replace(
            '%passedPercent%', str(round(passedPercent,2)) + "%")
        
        # Changing according to options
        if "LogoImage" in self.options:
            allcontent = allcontent.replace('%mainHeader%', "<img src=" + self.options['LogoImage'] +" height='80'/>")
        if "MainHeader" in self.options:
            allcontent = allcontent.replace('%mainHeader%', self.options["MainHeader"])
        else:
            allcontent = allcontent.replace('%mainHeader%', "Automation Report")
        if "FooterContent" in self.options:
            allcontent = allcontent.replace('%footerContent%', self.options["FooterContent"])
        else:
            allcontent = allcontent.replace('%footerContent%', "")
        self.report_file.write(allcontent)
        self.report_file.close()
