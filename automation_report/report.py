from datetime import datetime
import string
import codecs
import os

class AutomationReport:
    testCaseLinks = ""
    testCasecontent = ""
    now = datetime.now()
    report_name = "report" + now.strftime("%m%d%Y%H%M%S")
    report_file = None
    case_count = 0
    total_pass = 0
    total_fail = 0
    fail_case = False

    def __init__(self, report_name):
        self.report_name = report_name
        self.report_file = open((self.report_name + ".html"), "w+")

    def starttest(self, case_name):
        self.fail_case = 0
        self.case_count = self.case_count + 1
        active_class = ""
        if self.case_count == 1:
            active_class = 'active' 
        self.testCaseLinks = self.testCaseLinks + \
            "<li> <a href='#' class='testname %s' id='Test%s'>%s</a> - <span class='PASS casestatus status-%s'><i><b>PASS</b> </i></span></li>" % (
                active_class, self.case_count, case_name, self.case_count)
        self.testCasecontent = self.testCasecontent + \
            "<div id='Test%sSteps' class='case'>" % self.case_count
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
        self.testCaseLinks = self.testCaseLinks.replace(\
            "'PASS casestatus status-"+ str(self.case_count) + "'><i><b>PASS",\
            "'FAIL casestatus status-"+ str(self.case_count) + "'><i><b>FAIL")
        self.testCasecontent = self.testCasecontent + \
            "<tr class='table-danger'><td><i><b>FAIL</b></i></td><td> %s </td></tr>\n" % message

    def info(self, message):
        self.testCasecontent = self.testCasecontent + \
            "<tr class='table-info'><td><i><b>INFO</b></i></td><td> %s </td></tr>\n" % message

    def close(self):
        __location__ = os.path.realpath(os.path.join(
            os.getcwd(), os.path.dirname(__file__)))
        source_report_file = codecs.open(os.path.join(
            __location__, 'report.html'), 'r', 'utf-8')
        allcontent = source_report_file.read()
        allcontent = allcontent.replace('%testCaseLinks%', self.testCaseLinks)
        allcontent = allcontent.replace('%testCasecontent%', self.testCasecontent)
        allcontent = allcontent.replace('%headTitle%', self.report_name + " | Automation Report")
        allcontent = allcontent.replace('%totalCases%', str(self.case_count))
        allcontent = allcontent.replace('%passedCases%', str(self.case_count - self.total_fail))
        allcontent = allcontent.replace('%failedCases%', str(self.total_fail))
        self.report_file.write(allcontent)
        self.report_file.close()

