import re
import requests
from bs4 import BeautifulSoup

_session = requests.Session()

def getAllR15_UrlCodes():
    """ get all b.tech r15 results links """
    site = 'https://jntuaresults.ac.in/'
    src = requests.get(site).text
    soup = BeautifulSoup(src, 'lxml')
    # table = soup.find('table', {'class': 'ui table segment'})
    urls = [site+row['href'] for row in soup.findAll("a", href=True) if (("B.Tech" and "R15") in row.text) and ("B.Pharmacy" not in row.text)]
    codes = []
    for i in urls:
        pattern = re.compile(r"[0-9].*[0-9]")
        codes.append(re.findall(pattern, i)[0])
    return codes


def getaccessToken():
    """ Get accessToken """
    data=_session.get('https://jntuaresults.ac.in/view-results-56736602.html').text
    accessToken=0
    soup=BeautifulSoup(data,'lxml')
    for link in soup.find_all('script'):
        pattern = re.compile(r"\(([^}]+)\);\\nxmlhttp")
        txt = re.findall(pattern, str(link.contents))
        # txt=(useRegex(str(link.contents)))
        if len(txt)>0:
            res=txt[0].split(',')[1].replace('"','').replace("+",'')
            res=res.split('&')
            accessToken=(res[len(res)-1].split('=')[1])
    return accessToken

def getStudentDetailsData() -> dict:
    """ fetches students details info """
    return {f"Hall Ticket No": "*********", "Student name": "**********"}

def getTitleData() -> str:
    """ fetches title info """
    # return requests.get(f'https://jntuaresults.ac.in/view-results-{urlCode}.html').text
    return "Dummy title"


def getResultsDataList(hallTicektNo, sessionToken, urlCode) -> list:
    """ fetches results info """
    res = _session.get(f'https://jntuaresults.ac.in/results/res.php?ht={hallTicektNo}&id={urlCode}&accessToken={sessionToken}').text
    xamAttempted = (res.find("Invalid Hall Ticket Number for the Exam code you have selected") != 38)
    if(xamAttempted):
        soup = BeautifulSoup(res, 'lxml')
        table = soup.find('table', {'class': 'ui table segment'})
        resl = ['Subject Code', 'Subject Name',  'Internals', 'Externals',
                'Total Marks', 'Result Status', 'Credits', 'Grades']

        values = [i.text for i in table.findAll("td")]
        resultsDataList = []
        _from = 0
        _to = 8
        for _ in range(len(values)//8):
            x = {}
            for i, j in zip(resl, values[_from:_to]):
                x[i] = j
            _from += 8
            _to += 8
            resultsDataList.append(x)
        return resultsDataList


def main(_hallTicektNo):
    _sessionToken = getaccessToken()
    _allR15UrlCodes = getAllR15_UrlCodes()
    resultsList = []
    progressCounter = len(_allR15UrlCodes)
    studentDetailsNotFound = True
    for _urlCode in _allR15UrlCodes:
        print(progressCounter, "items left")
        progressCounter -= 1
        results_data_list  = getResultsDataList(_hallTicektNo, _sessionToken, _urlCode)
        results_data_title = getTitleData()
        studentDetails = {}
        if (results_data_list != None):
            if(studentDetailsNotFound): ## it will get called only till student details found ###  
                studentDetails = getStudentDetailsData()
                studentDetailsNotFound = False
            resultObject = {"data" : results_data_list, "title" : results_data_title, 'resultsCode': _urlCode}
            resultsList.append(resultObject)
            break
            # print(resultObject)
    
    endResultsObject = {'results' : resultsList, 'user': studentDetails}
    return endResultsObject


# print(main('163g1a0505'))