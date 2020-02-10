from datetime import datetime
import string
import codecs
import os
testCaseLinks = ""
testCasecontent = ""
count = 0

def starttest(case_name):
    global count, testCaseLinks, testCasecontent
    count = count + 1
    testCaseLinks = testCaseLinks + \
        "<li> <a href='#' class='testname active' id='Test%s'>%s</a> - <span class='PASS casestatus'><i><b>PASS</b> </i></span> </li>" % (
            count, case_name)
    testCasecontent = testCasecontent + "<div id='Test%sSteps' class='case'>" % count
    tableContent = """<table class="table table-hover table-bordered">
                    <thead>
                        <th>Status</th>
                        <th>Message</th>
                    </thead>
                    <tbody>"""
    testCasecontent = testCasecontent + tableContent           


def endtest():
    global testCasecontent
    testCasecontent = testCasecontent + "\n </tbody>\n</table>\n</div>"

def success(message):
    global testCasecontent
    testCasecontent = testCasecontent + \
        "<tr class='table-success'><td><i><b>SUCCESS</b></i></td><td> %s </td></tr>\n" % message
    return testCasecontent

def fail(message):
    global testCasecontent, testCaseLinks
    testCaseLinks = testCaseLinks.replace('PASS', 'FAIL')
    testCasecontent = testCasecontent + \
        "<tr class='table-danger'><td><i><b>FAIL</b></i></td><td> %s </td></tr>\n" % message
    return testCasecontent

def info(message):
    global testCasecontent
    testCasecontent = testCasecontent + \
        "<tr class='table-info'><td><i><b>INFO</b></i></td><td> %s </td></tr>\n" % message
    return testCasecontent

def close():
    global testCasecontent, testCaseLinks
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    report_file = codecs.open(os.path.join(__location__, 'report.html'), 'r', 'utf-8')
    allcontent = report_file.read()
    allcontent = allcontent.replace('#testCaseLinks', testCaseLinks)
    allcontent = allcontent.replace('#testCasecontent', testCasecontent)
    now = datetime. now()
    f = open("report" + now.strftime("%m%d%Y%H%M%S") + ".html", "w+")
    f.write(allcontent)
    f.close
