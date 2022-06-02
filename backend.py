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


def getResultsData(hallTicektNo, sessionToken, urlCode) -> list:
    """ fetches results info """
    res = _session.get(f'https://jntuaresults.ac.in/results/res.php?ht={hallTicektNo}&id={urlCode}&accessToken={sessionToken}').text
    xamAttempted = (res.find("Invalid Hall Ticket Number for the Exam code you have selected") != 38)
    if(xamAttempted):
        s = BeautifulSoup(res, 'lxml')
        h, [_, *d] = [i.text.lstrip() for i in s.find_all('th')], [[i.text for i in b.find_all('td')] for b in s.find_all('tr')]
        results_data = [dict(zip(h, i)) for i in d]
        results_data.pop() # removing last item since there is always an object object
        return results_data


def main(_hallTicektNo):
    # _hallTicektNo = '163g1a0505'
    _sessionToken = getaccessToken()
    _allR15UrlCodes = getAllR15_UrlCodes()
    resultsList = []
    progressCounter = len(_allR15UrlCodes)
    studentDetailsNotFound = True
    for _urlCode in _allR15UrlCodes:
        print(progressCounter, "items left")
        progressCounter -= 1
        results_data  = getResultsData(_hallTicektNo, _sessionToken, _urlCode)
        results_title = getTitleData()

        ### it will get called only till student details found ###  
        if(studentDetailsNotFound):
            studentDetails = getStudentDetailsData()
            studentDetailsNotFound = False
        ### it will get called only till student details found ###
        
        if (results_data != None):
            resultObject = {"data" : results_data, "title" : results_title}
            resultsList.append(resultObject)
            # break
            # print(resultObject)

    endResultsObject = {'results' : resultsList, 'user': studentDetails}
    return endResultsObject
