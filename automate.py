import os
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import requests
import json


class Automate:
    print('site')
    site = 'https://jntuaresults.ac.in/'
    print('src')
    src = requests.get(site).text
    print('soup')
    soup = BeautifulSoup(src, 'lxml')
    status = 'Invalid Hall Ticket Number for the Exam code you have selected.'

    def __init__(self, rollno, course) -> None:
        self.rollno = rollno
        self.course = course
        # self.regulation = regulation
    
        def set_regulation():
            rollNo = self.rollno

            _reg = int(rollNo[0:2])

            if _reg >= 15 and _reg < 19:
                _reg = "R15"
                self.regulation = _reg
            elif _reg >= 19:
                _reg = "R19"
                self.regulation = _reg
        set_regulation()
    

    @classmethod
    def getPublishedResults(cls):
        soup = cls.soup
        site = cls.site
        table = soup.find('table', {'class': 'ui table segment'})

        allDates = [e.text for i, e in enumerate(
            table.findAll('td')) if i % 2 == 0]
        # print(allDates)

        allTitles = [e.text for i, e in enumerate(
            table.findAll('td')) if i % 2 != 0]
        # print(allTitles)

        allLinks = [site+i['href'] for i in table.findAll('a', href=True)]
        # print(allLinks)

        # allDates = ['2020-06-11',
        #          '2020-06-08', '2020-06-08', '2020-06-08', '2020-06-08', '2020-05-23',
        #          '2020-05-23',
        #          '2020-05-23', '2020-05-23', '2020-05-20', '2020-05-20', '2020-05-20', '2020-05-20', '2020-05-20', '2020-05-20', '2020-05-20', '2020-05-20', '2020-05-11', '2020-05-09', '2020-05-09', '2020-05-09', '2020-05-09', '2020-05-09', '2020-05-09', '2020-05-09', '2020-03-20', '2020-03-20', '2020-03-20', '2020-03-20', '2020-03-20', '2020-03-20', '2020-03-20', '2020-03-19', '2020-03-19', '2020-03-19', '2020-03-19', '2020-03-19', '2020-03-19', '2020-03-19', '2020-03-17', '2020-03-13', '2020-03-13', '2020-03-13', '2020-03-13', '2020-03-13', '2020-03-13', '2020-03-13', '2020-03-13', '2020-03-13', '2020-03-07', '2020-03-06', '2020-03-05', '2020-03-05', '2020-03-05', '2020-03-05', '2020-03-05', '2020-03-03', '2020-03-03', '2020-03-03', '2020-03-03', '2020-03-03', '2020-03-02', '2020-03-02', '2020-02-29', '2020-02-29', '2020-02-29', '2020-02-29', '2020-02-28', '2020-02-28', '2020-02-28', '2020-02-28', '2020-02-28', '2020-02-28', '2020-02-28', '2020-02-25', '2020-02-24', '2020-02-18', '2020-02-18', '2020-02-14', '2020-02-11', '2020-02-01', '2020-01-31', '2020-01-30', '2020-01-20', '2019-12-05', '2019-12-05', '2019-12-05', '2019-12-05', '2019-12-05', '2019-12-05', '2019-12-05', '2019-11-30', '2019-11-28', '2019-11-28', '2019-11-28', '2019-11-28', '2019-11-18', '2019-11-18', '2019-11-17', '2019-11-13', '2019-11-13', '2019-11-09', '2019-10-29', '2019-10-26', '2019-10-26', '2019-10-26', '2019-10-18', '2019-10-18', '2019-10-18', '2019-10-18', '2019-10-18', '2019-10-18', '2019-10-18', '2019-10-18', '2019-10-18', '2019-10-18', '2019-10-18', '2019-10-18', '2019-10-16', '2019-10-16', '2019-10-16', '2019-10-16', '2019-10-15', '2019-10-15', '2019-10-15', '2019-10-05', '2019-09-27', '2019-09-27', '2019-09-27', '2019-09-27', '2019-09-27', '2019-09-27', '2019-09-27', '2019-09-20', '2019-09-13', '2019-09-11', '2019-09-11',
        #          '2019-09-09', '2019-09-09', '2019-09-09', '2019-09-09', '2019-09-09', '2019-09-09',
        #          '2019-08-31',
        #          '2019-08-31', '2019-08-31', '2019-08-31', '2019-08-31', '2019-08-31', '2019-08-31', '2019-08-31', '2019-08-31', '2019-08-31', '2019-08-21', '2019-08-21', '2019-08-21', '2019-08-21', '2019-08-21', '2019-08-21', '2019-08-21', '2019-08-21', '2019-08-21', '2019-08-21', '2019-08-16', '2019-08-16', '2019-08-16', '2019-08-16', '2019-08-11', '2019-08-11', '2019-08-08', '2019-08-08', '2019-08-01', '2019-08-01', '2019-07-19', '2019-07-19', '2019-07-19', '2019-07-19', '2019-07-19', '2019-07-19', '2019-07-19', '2019-07-19', '2019-07-19', '2019-06-27', '2019-06-27', '2019-05-16', '2019-05-16', '2019-05-16', '2019-05-16', '2019-05-16', '2019-05-16', '2019-05-10', '2019-05-10', '2019-05-08', '2019-05-08', '2019-05-08', '2019-05-08', '2019-05-08', '2019-05-08', '2019-05-04', '2019-04-25', '2019-04-18', '2019-04-18', '2019-04-18', '2019-04-18', '2019-04-18', '2019-04-18', '2019-04-18', '2019-04-18', '2019-04-18', '2019-04-10', '2019-04-10', '2019-04-10', '2019-04-04', '2019-04-04', '2019-04-04', '2019-03-27', '2019-03-26', '2019-03-26', '2019-03-26', '2019-03-25', '2019-03-25', '2019-03-25', '2019-03-21', '2019-03-21', '2019-03-21', '2019-03-21', '2019-03-21', '2019-03-21', '2019-03-12', '2019-02-26', '2019-02-26', '2019-02-26', '2019-02-26', '2019-02-26', '2019-02-26', '2019-02-18', '2019-02-18', '2019-02-18', '2019-02-18', '2019-02-18', '2019-02-18', '2019-02-16', '2019-02-16', '2019-02-05', '2019-02-05', '2019-02-05', '2019-02-05', '2019-02-05', '2019-02-05', '2019-02-05', '2019-02-05', '2019-01-30', '2019-01-30', '2019-01-21', '2019-01-19', '2018-09-24', '2018-09-24', '2018-09-05', '2018-09-05', '2018-09-01', '2018-08-14', '2018-08-14', '2018-08-14', '2018-08-14', '2018-08-14', '2018-08-10', '2018-08-08', '2018-08-03', '2018-08-03', '2018-08-03', '2018-08-01', '2018-08-01', '2018-07-25', '2018-05-21']

        # allTitles = ['B.Pharmacy I Year I Semester (R19) Regular Examinations, February 2020',
        #           'M.Tech I semester (R17) Regular & Supplementary Examinations, January/February 2020',
        #           'M.Tech I semester (R09) Supplementary Examinations, January/February 2020',
        #           'M.Tech II semester (R17) Supplementary Examinations, January/February 2020',
        #           'M.Tech II semester (R09) Supplementary Examinations, January/February 2020',
        #           'M.Pharmacy I semester (R17) Regular & Supplementary Examinations, January/February 2020',
        #           'M.Pharmacy II semester (R17) Supplementary Examinations, January / February 2020',
        #           'M.Pharmacy I semester (R09) Supplementary Examinations, January / February 2020 ',
        #           'M.Pharmacy II semester (R09) Supplementary Examinations, January / February 2020', 'Pharm.D IV Year Regular & Supplementary (R14) Examinations, February 2020', 'Pharm.D I (First) Year (R17) Supplementary Examinations, February 2020', 'Pharm.D I (First) Year (R14) Supplementary Examinations, February 2020', 'M.sc. I Year I Semester (R09) Regular and Supply Examinations Dec/Jan 2019 - 2020.', 'M.Sc. I Year II Semester (R09) Supplementary Examinations, Dec/Jan 2019 - 2020', 'Pharm.D (PB) I Year (R17) Supplementary Examinations, Jan/Feb 2020', 'Pharm.D (PB) II Year (R17) Supplementary Examinations, December 2019.', 'B.Tech I Year I Semester (R19) Regular Examinations, January 2020', 'MBA I semester (R17) Regular &  Supplementary Examinations, January 2020.', 'MBA I semester (R14) Supplementary Examinations, January 2020',
        #           'MBA II semester (R17) Supplementary Examinations, January 2020', 'MBA II semester (R14) Supplementary Examinations, January 2020', 'MCA I semester (R17) Regular & Supplementary Examinations, January 2020', 'MCA I semester (R09) Supplementary Examinations, January 2020', 'MCA II semester (R09) Supplementary Examinations, January 2020', 'MCA II semester (R17) Supplementary Examinations, January 2020', 'B.Tech I Year II Semester (R15) Supplementary Examinations, December/January 2019/2020', 'B.Tech I Year (R13) Supplementary Examinations, December/January 2019/2020', 'B.Tech I Year (R09) Supplementary Examinations, December/January 2019/2020', 'B.Pharmacy I Year II Semester (R15) Supplementary Examinations, December/January 2019/2020', 'B.Pharmacy I Year (R13) Supplementary Examinations, December/January 2019/2020', 'B.Pharmacy I Year (R09) Supplementary Examinations, December/January 2019/2020', 'B.Tech I Year (R09) (Last Chance) Supplementary Examinations, December/January 2019/2020', 'B.Tech II Year II Semester (R15) Supplementary Examinations, December/January 2019/2020.', 'B.Tech II Year II Sem (R09) (Last Chance) Supplementary Examinations, December/January 2019/2020', 'B.Tech II Year II Semester (R13) Supplementary Examinations, December/January 2019/2020', 'B.Tech II Year II Semester (R09) Supplementary Examinations, December/January 2019/2020', 'B.Pharmacy II Year II Semester (R15) Supplementary Examinations, December/January 2019/2020', 'B.Pharmacy II Year II Semester (R13) Supplementary Examinations, December/January 2019/2020', 'B.Pharmacy II Year II Semester (R09) Supplementary Examinations, December/January 2019/2020', 'M.Tech III semester (R17) Regular & Supplementary Examinations, January 2020', 'M.Pharmacy III semester (R17) Regular & Supplementary Examinations, January 2020', 'B.Tech III Year II Semester (R15) Supplementary Examinations, December/January 2019/2020', 'B.Tech III Year II Semester (R09 & R13) (Last Chance) Supplementary Examinations, Dec/Jan 2019/2020', 'B.Tech III Year II Semester (R13) Supplementary Examinations, December/January 2019/2020', 'B.Tech  III  Year II Semester (R09) Supplementary Examinations, December/January 2019/2020 ', 'B.Pharmacy III Year II Semester (R15) Supplementary Examinations, December/January 2019/2020', 'B.Pharmacy III Year II Semester (R13) Supplementary Examinations, December/January 2019/2020', 'B.Pharmacy III Year II Semester (R09) Supplementary Examinations, December/January 2019/2020', 'B.Pharmacy III Year II Semester (R09) (Last Chance) Supplementary Examinations, Dec/Jan 2019/2020', 'B.Tech I Year I Semster (R15) Supplementary Examinations, Nov/Dec 2019', 'B.Tech II Year I Semster (R09) (Last Chance) Supplementary Examinations, Nov/Dec 2019', 'B.Tech II Year I Semster (R09) Supplementary Examinations, Nov/Dec 2019', 'B.Pharmacy II Year I Semster (R13) Supplementary Examinations, Nov/Dec 2019', 'B.Pharmacy II Year I Semster (R09) Supplementary Examinations, Nov/Dec 2019', 'B.Tech II Year I Semster (R13) Supplementary Examinations, Nov/Dec 2019', 'MBA III semester (R17) Regular & Supplementary Examinations, November/ December 2019', 'B.Tech III Year I Semster (R13) Supplementary Examinations, Nov/Dec 2019', 'B.Pharmacy III Year I Semster (R13) Supplementary Examinations, Nov/Dec 2019', 'B.Tech III Year I Semster (R09) Supplementary Examinations, Nov/Dec 2019', 'B.Pharmacy III Year I Semster (R09) Supplementary Examinations, Nov/Dec 2019', 'B.Tech III Year I Semster (R09 & R13) (Last Chance) Supplementary Examinations, Nov/Dec 2019', 'B.Pharmacy II Year I Semester (R15) Regular & Supplementary Examinations, Nov/Dec 2019', 'B.Pharmacy I Year I Semster (R15) Supplementary Examinations, Nov/Dec 2019', 'MBA III semester (R14) Supplementary Examinations, November/December 2019', 'MBA IV semester (R14) Supplementary Examinations, November/December 2019', 'MCA III semester (R09) Supplementary Examinations, November/December 2019', 'MCA IV semester (R09) Supplementary Examinations, November/December 2019', 'B.Pharmacy IV Year I Semester (R13) Supplementary Examinations, Nov/Dec 2019', 'B.Tech IV Year I Semester (R09) Supplementary Examinations, Nov/Dec 2019', 'B.Pharmacy IV Year I Semester (R09) Supplementary Examinations, Nov/Dec 2019', 'B.Tech IV Year I Semester (R13) Supplementary Examinations, Nov/Dec 2019', 'MBA IV semester (R17) Supplementary Examinations, November/December 2019', 'MCA III semester (R17) Regular & Supplementary Examinations, November/December 2019', 'MCA IV semester (R17) Supplementary Examinations, November/December 2019', 'B.Tech IV Year I Semester (R09 & R13) (Last Chance) Supplementary Examinations, Nov/Dec 2019', 'B.Tech II Year I Semester (R15) Regular & Supplementary Examinations, Nov/Dec 2019', 'Pharm.D Second Year (R14) Supplementary Examinations, December 2019', 'Pharm.D Second Year (R17) Supplementary Examinations, December 2019', 'B.Pharmacy III Year I Semester (R15) Regular & Supplementary Examinations, Nov/Dec 2019', 'B.Tech III Year I Semester (R15) Regular & Supplementary Examinations, Nov/Dec 2019', 'M.Sc. III Semester Regular & Supplementary Examinations, October 2019', 'B.Pharmacy IV Year I Semester (R15) Regular & Supplementary Examinations, Nov/Dec 2019', 'B.Tech IV Year I Semester (R15) Regular & Supplementary Examinations, Nov/Dec 2019', 'Pharm.D V Year (R14) Regular & Supplementary Examinations, December 2019', 'M.Tech I semester (R17) Supplementary Examinations, July/August 2019', 'M.Tech II semester (R17) Regular & Supplementary Examinations, July/August 2019', 'MCA V semester (R09) Supplementary Examinations,October 2019', 'M.Tech I semester (R09) Supplementary Examinations, July/August 2019', 'M.Tech II semester (R09) Supplementary Examinations, July/August 2019', 'M.Pharmacy I Semester (R09) Supplementary Examinations, July/August 2019', 'M.Pharmacy II Semester (R09) Supplementary Examinations, July/August 2019', 'Pharm.D (PB) I Year (R17) Regular & Supplementary Examinations, July/August 2019', 'M.Pharmacy III Semester (R17) Supplementary Examinations, July/August 2019.', 'M.Pharmacy IV Semester (R17) Regular Examinations, August 2019.', 'M.Tech III Semester (R17) Supplementary Examinations, July/August 2019', 'MCA V Semester (R17) Regular Examinations, October 2019', 'Pharm.D III Year (R09) & (R14) Supplementary Examinations, August 2019', 'Pharm.D I Year (R09) & (R14) Supplementary Examinations, July/August 2019', 'M.Pharmacy I Semester (R17) Supplementary Examinations, July/August 2019', 'Pharm.D IV Year (R09 and R14) Supplementary Examinations, August 2019', 'Pharm.D V Year (R09 and R14) Supplementary Examinations, August 2019', 'M.Pharmacy II semester (R17) Regular & Supplementary Examinations, July/August 2019', 'Pre Ph.D Regular & Supplementary Examinations, September 2018 Re-valuation Results (Pending Results)', 'B.Tech I Year (R09) (Last Chance) Supplementary Examinations, June/July 2019', 'B.Tech II Year I Semester (R09) (Last Chance) Supplementary Examinations, June/July 2019', 'B.Tech III Year I Semester (R09) (Last Chance) Supplementary Examinations, June/July 2019', 'MBA II semester (R17) Regular & Supplementary Examinations, May/June 2019', 'MBA II semester (R14) Supplementary Examinations, May/June 2019', 'MBA I semester (R17) Supplementary Examinations, May/June 2019', 'MBA I semester (R14) Supplementary Examinations, May/June 2019', 'MCA II semester (R17) Regular & Supplementary Examinations, May/June 2019', 'MCA II semester (R09) Supplementary Examinations, May/June 2019', 'MCA I semester (R17) Supplementary Examinations, May/June 2019', 'MCA I semester (R09) Supplementary Examinations, May/June 2019', 'Pharmm D III Year (R09) & (R14) Supplementary Examinations, August 2019', 'Pharm.D III Year (R09) & (R17) Supplementary Examinations, August 2019', 'Pharm.D III Year (R09) & (R14) Supplementary Examinations, August 2019', 'Pharm.D III Year (R09) & (R14) Supplementary Examinations, August 2019', 'B.Tech II Year II Semester (R09) (Last Chance) Supplementary Examinations, May/June 2019', 'B.Tech IV Year I Semester (R09) (Last Chance) Supplementary Examinations, June/July 2019', 'B.Tech III Year II Semester (R09) (Last Chance) Supplementary Examinations, May/June 2019', 'B.Tech IV Year II Semester (R09) (Last Chance) Advanced Supplementary Examinations, July 2019', 'M.Sc. I (1st) Semester (R09) Supplementary Examinations, May 2019', 'M.Sc. II (2nd) Semester (R09) Regular & Supplementary Examinations, May 2019', 'M.Sc. III (3rd) Semester (R09) Supplementary Examinations, May 2019', 'Pharm.D I Year (R17) Regular & Supplementary Examinations, July/August 2019', 'B.Pharmacy I Year (R09) Supplementary Examinations, June/July 2019', 'B.Pharmacy I Year (R13) Supplementary Examinations, June/July 2019', 'B.Pharmacy I Year I Semester (R15) Supplementary Examinations, May/June 2019', 'B.Pharmacy I Year II Semester (R15) Regular & Supplementary Examinations, July 2019', 'B.Tech I Year (R09) Supplementary Examinations, June/July 2019', 'B.Tech I Year I Semester (R15) Supplementary Examinations, June.July 2019', 'B.Tech I Year (R13) Supplementary Examinations, June/July 2019', 'B.Tech I Year II Semester (R15) Regular & Supplementary Examinations, May/June 2019', 'Pre Ph.D Regular ', 'B.Pharmcy III Year I Semester (R15) Supplementary Examinations, June/July 2019', 'B.Pharmacy II Year I Semester (R15) Supplementary Examinations, June/July 2019', 'B.Tech III Year I Semester (R15) Supplementary Examinations, June/July 2019', 'B.Tech II Year I Semester (R15) Supplementary Examinations, June/July 2019', 'B.Tech II Year I Semester (R13) Supplementary Examinations, June/July 2019', 'B.Tech II Year I Semester (R09) Supplementary Examinations, June/July 2019', 'B.Pharmacy II Year I Semester (R13) Supplementary Examinations, June/July 2019', 'B.Pharmacy II Year I Semester (R09) Supplementary Examinations, June/July 2019', 'B.Tech II Year II Semester (R15) Regular & Supplementary Examinations, May/June 2019', 'B.Tech II Year II Semester (R13) Supplementary Examinations, May/June 2019', 'B.Tech II Year II Semester (R09) Supplementary Examinations, May/June 2019', 'B.Pharmacy II Year II Semester (R15) Regular & Supplementary Examinations, May/June 2019', 'B.Pharmacy II Year II Semester (R13) Supplementary Examinations, May/June 2019', 'B.Pharmacy II Year II Semester (R09) Supplementary Examinations, May/June 2019', 'B.Tech III Year I Semester (R13) Supplementary Examinations, June/July 2019', 'B.Tech III Year I Semester (R09) Supplementary Examinations, June/July 2019', 'B.Pharmacy III Year I Semester (R13) Supplementary Examinations, June/July 2019', 'B.Pharmacy III Year I Semester (R09) Supplementary Examinations, June/July 2019', 'B.Pharmacy IV Year I Semester (R09) Supplementary Examinations, June/July 2019', 'B.Tech IV Year I Semester (R15) Supplementary Examinations, June/July 2019', 'B.Pharmcy IV Year I Semester (R15) Supplementary Examinations, June/July 2019', 'B.Tech IV Year I Semester (R13) Supplementary Examinations, June/July 2019', 'B.Pharmacy IV Year I Semester (R13) Supplementary Examinations, June/July 2019', 'B.Tech IV Year I Semester (R09) Supplementary Examinations, June/July 2019', 'B.Tech III Year II Semester (R13) Supplementary Examinations, May/June 2019', 'B.Tech III Year II Semester (R09) Supplementary Examinations, May/June 2019', 'B.Pharmacy III Year II Semester (R13) Supplementary Examinations, May/June 2019', 'B.Pharmacy III Year II Semester (R09) Supplementary Examinations, May/June 2019', 'B.Tech IV Year II Semester (R13) Advanced Supplementary Examinations, July 2019', 'B.Tech IV Year II Semester (R09) Advanced Supplementary Examinations, July 2019', 'B.Pharmacy IV Year II Semester (R13) Advanced Supplementary Examinations, July 2019', 'BPharmacy IV Year II Semester (R09) Advanced Supplementary Examinations, July 2019', 'B.Tech IV Year II Semester (R15) Advanced Supplementary Examinations, July 2019', 'B.Pharmacy IV Year II Semester (R15) Advanced Supplementary Examinations, July 2019', 'B.Pharmacy III Year II Semester (R15) Regular & Supplementary Examinations, May/June 2019', 'B.Tech III Year II Semester (R15) Regular & Supplementary Examinations, May/June 2019', 'Pharm.D Second Year (R17) Regular Examinations May/June 2019', 'Pharm.D Second Year (R14) Supplementary Examinations May/June 2019', 'MCA IV Semester (R09) Supplementary Examinations, May 2019', 'MCA V Semester (R09) Supplementary Examinations, May 2019', 'MCA III Semester (R09) Supplementary Examinations, May 2019', 'MBA IV Semester (R14) Supplementary Examinations, May 2019 ', 'MBA III Semester (R14) Supplementary Examinations, May 2019 ', 'MCA IV Semester (R17) Regular & Supplementary Examinations, May 2019', 'MCA III Semester (R17) Supplementary Examinations,May 2019', 'MBA IV Semester (R17) Regular & Supplementary Examinations, May 2019 ', 'MBA III Semester (R17) Supplementary Examinations, May 2019 ', 'M.Tech III Semester (R17) Regular Examinations,January 2019', 'M.Pharmacy III Semester (R17) Regular Examinations,January 2019', 'B.Pharmacy IV Year II Semester (R09) Supplementary Examinations, April 2019', 'B.Pharmacy IV Year II Semester (R13) Supplementary Examinations, April 2019', 'B.Tech IV Year II Semester (R09) Supplementary Examinations, April 2019', 'B.Tech IV Year II Semester (R13) Supplementary Examinations, April 2019', 'B.Tech IV Year II Semester (R15) Regular Examinations, April 2019.', 'B.Pharmacy IV Year II Semester (R15) Regular Examinations, April 2019', 'M.Tech I Semester (R17) Regular & Supplementary Examinations, January/February 2019', 'M.Pharmacy I Semester (R17) Regular & Supplementary Examinations, January/February 2019', 'M.Tech I Semester (R09) Supplementary Examinations, January/February 2019', 'M.Tech II Semester (R17) Supplementary Examinations, January/February 2019', 'M.Tech II Semester (R09) Supplementary Examinations, January/February 2019', 'M.Pharmacy I Semester (R09) Supplementary Examinations, January/February 2019', 'M.Pharmacy II Semester (R17) Supplementary Examinations, January/February 2019', 'M.Pharmacy II Semester (R09) Supplementary Examinations, January/February 2019', 'Pharm.D IV Year (R14) Regular & Supplementary Examinations, January 2019', 'Pharm.D III Year (R14) Regular & Supplementary Examinations, March 2019', 'B.Pharmacy I Year I Semester (R15) Regular & Supplementary Examinations, February 2019', 'MBA I Semester (R14) Supplementary Examinations, December/January 2018/2019', 'MBA I Semester (R17) Regular &Supplementary Examinations, December/January 2018/2019 ', 'MBA II Semester (R14) Supplementary Examinations, December/January 2018/2019 ', 'MBA II Semester (R17) Supplementary Examinations, December/January 2018/2019 ', 'MCA I Semester (R09) Supplementary Examinations, December 2018', 'MCA I Semester (R17) Regular & Supplementary Examinations, December 2018', 'MCA II Semester (R17) Supplementary Examinations, December/January 2018/2019', 'MCA II Semester (R09) Supplementary Examinations, December/January 2018/2019', 'B.Pharmacy I Year (R09) Supplementary Examinations, December 2018', 'B.Pharmacy I Year (R13) Supplementary Examinations, December 2018', 'B.Pharmacy I Year II Semester (R15) Supplementary Examinations, December 2018', 'B.Tech I Year (R09) Supplementary Examinations, December/January 2018/2019', 'B.Tech I Year (R13) Supplementary Examinations, December/January 2018/2019', 'B.Tech I Year II Semester (R15) Supplementary Examinations, December 2018', 'Pharm.D V (Fifth) Year Regular and Supplementary Examinations, February 2019', 'B.Pharmacy II Year II Semester (R09) Supplementary Examinations, December 2018', 'B.Pharmacy II Year II Semester (R13) Supplementary Examinations, December 2018', 'B.Pharmacy II Year II Semester (R15) Supplementary Examinations, December 2018', 'B.Tech II Year II Semester (R09) Supplementary Examinations, December 2018', 'B.Tech II Year II Semester (R13) Supplementary Examinations, December 2018', 'B.Tech II Year II Semester (R15) Supplementary Examinations, December 2018', 'B.Pharmacy III Year II Semester (R09) Supplementary Examinations, December 2018', 'B.Pharmacy III Year II Semester (R13) Supplementary Examinations, December 2018', 'B.Pharmacy III Year II Semester (R15) Supplementary Examinations, December 2018', 'B.Tech III Year II Semester (R09) Supplementary Examinations, December 2018', 'B.Tech III Year II Semester (R13) Supplementary Examinations, December 2018', 'B.Tech III Year II Semester (R15) Supplementary Examinations, December/January 2018/2019', 'B.Tech I Year I Semester (R15) Regular and Supplementary Examinations, November/December 2018', 'B.Pharmacy II Year I Semester (R09) Supplementary Examinations, November/December 2018', 'B.Pharmacy II Year I Semester (R13) Supplementary Examinations, November/December 2018', 'B.Pharmacy II Year I Semester (R15) Regular and Supplementary Examinations, November/December 2018', 'B.Tech II Year I Semester (R09) Supplementary Examinations, November/December 2018', 'B.Tech II Year I Semester (R13) Supplementary Examinations, November/December 2018', 'B.Tech II Year I Semester (R15) Regular and Supplementary Examinations, November/December 2018', 'MCA III Semester (R09) Supplementary Examinations, November/December 2018', 'MCA III Semester (R17) Regular Examinations, November/December 2018', 'MCA IV Semester (R09) Supplementary Examinations, November/December 2018',
        #           'MBA III Semester (R14) Supplementary Examinations, November/December 2018', 'MBA III Semester (R17) Regular Examinations, November/December 2018', 'MBA IV Semester (R14) Supplementary Examinations, November/December 2018', 'Pharm.D I Year (R17) Advanced Supplementary Examinations, December 2018', 'Pharm.D I Year (R14) Supplementary Examinations, December 2018', 'B.Tech III Year I Semester (R13) Supplementary Examinations, November/December 2018', 'B.Tech IV Year I Semester (R09) Supplementary Examinations, November/December 2018', ' B.Tech III Year I Semester (R09) Supplementary Examinations, November/December 2018', 'B.Pharmacy IV Year I Semester (R13) Supplementary Examinations, November/December 2018', 'B.Pharmacy III Year I Semester (R13) Supplementary Examinations, November/December 2018', 'B.Pharmacy IV Year I Semester (R09) Supplementary Examinations, November/December 2018', 'B.Pharmacy III Year I Semester (R09) Supplementary Examinations, November/December 2018', 'B.Tech IV Year I Semester (R13) Supplementary Examinations, November/December 2018', 'B.Tech III Year I Semester (R15) Regular and Supplementary Examinations, November/December 2018', 'B.Pharmacy III Year I Semester (R15) Regular and Supplementary Examinations, November/December 2018', 'B.Pharmacy IV Year I Semester (R15) Regular Examinations, November/December 2018', 'B.Tech IV Year I Semester (R15) Regular Examinations, November/December 2018', 'B.Pharmacy I Year I Semester (R15) Supplementary Examinations June 2018', 'B.Pharmacy I Year II Semester (R15) Regular & Supplementary Examinations June 2018', 'B.Pharmacy II Year I Semester (R15) Supplementary Examinations June 2018', 'B.Pharmacy III Year I Semester (R15) Supplementary Examinations June 2018', 'B.Pharmacy II Year II Semester (R15) Regular & Supplementary Examinations MayJune 2018', 'B.Pharmacy I Year (R09) Supplementary Examinations June 2018', 'B.Pharmacy I Year (R13) Supplementary Examinations June 2018', 'B.Pharmacy II Year I Semester (R09) Supplementary Examinations June 2018', 'B.Pharm III year I Semester (R09) Supplementary Examinations June 2018', 'B.Pharmacy IV Year I Semester (R09) Supplementary Examinations June 2018', 'B.Pharmacy II Year I Semester (R13) Supplementary Examinations June 2018', 'B.Pharmacy III Year I Semester (R13) Supplementary Examinations June 2018', 'B.Pharmacy IV Year I Semester (R13) Supplementary Examinations June 2018', 'B.Pharmacy II Year II Semester (R09) Supplementary Examinations MayJune 2018', 'B.Pharmacy II Year II Semester (R13) Supplementary Examinations MayJune 2018', 'B.Pharmacy III Year II Semester (R09) Supplementary Examinations MayJune 2018', 'B.Pharmacy III Year II Semester (R13) Supplementary Examinations MayJune 2018', 'B.Pharmacy III Year II Semester (R15) Regular Examinations MayJune 2018', ' B.Pharmacy IV Year II Semester (R09) Supplementary Examinations April 2018']

        # links = ['https://jntuaresults.ac.in/view-results-56736333.html', 'https://jntuaresults.ac.in/view-results-56736327.html', 'https://jntuaresults.ac.in/view-results-56736328.html', 'https://jntuaresults.ac.in/view-results-56736329.html', 'https://jntuaresults.ac.in/view-results-56736330.html', 'https://jntuaresults.ac.in/view-results-56736323.html', 'https://jntuaresults.ac.in/view-results-56736324.html', 'https://jntuaresults.ac.in/view-results-56736325.html', 'https://jntuaresults.ac.in/view-results-56736326.html', 'https://jntuaresults.ac.in/view-results-56736314.html', 'https://jntuaresults.ac.in/view-results-56736315.html', 'https://jntuaresults.ac.in/view-results-56736316.html', 'https://jntuaresults.ac.in/view-results-56736318.html', 'https://jntuaresults.ac.in/view-results-56736319.html', 'https://jntuaresults.ac.in/view-results-56736320.html', 'https://jntuaresults.ac.in/view-results-56736321.html', 'https://jntuaresults.ac.in/view-results-56736322.html', 'https://jntuaresults.ac.in/view-results-56736313.html', 'https://jntuaresults.ac.in/view-results-56736304.html', 'https://jntuaresults.ac.in/view-results-56736305.html', 'https://jntuaresults.ac.in/view-results-56736306.html', 'https://jntuaresults.ac.in/view-results-56736307.html', 'https://jntuaresults.ac.in/view-results-56736308.html', 'https://jntuaresults.ac.in/view-results-56736310.html', 'https://jntuaresults.ac.in/view-results-56736311.html', 'https://jntuaresults.ac.in/view-results-56736296.html', 'https://jntuaresults.ac.in/view-results-56736297.html', 'https://jntuaresults.ac.in/view-results-56736298.html', 'https://jntuaresults.ac.in/view-results-56736299.html', 'https://jntuaresults.ac.in/view-results-56736300.html', 'https://jntuaresults.ac.in/view-results-56736301.html', 'https://jntuaresults.ac.in/view-results-56736302.html', 'https://jntuaresults.ac.in/view-results-56736289.html', 'https://jntuaresults.ac.in/view-results-56736290.html', 'https://jntuaresults.ac.in/view-results-56736291.html', 'https://jntuaresults.ac.in/view-results-56736292.html', 'https://jntuaresults.ac.in/view-results-56736293.html', 'https://jntuaresults.ac.in/view-results-56736294.html', 'https://jntuaresults.ac.in/view-results-56736295.html', 'https://jntuaresults.ac.in/view-results-56736288.html', 'https://jntuaresults.ac.in/view-results-56736279.html', 'https://jntuaresults.ac.in/view-results-56736280.html', 'https://jntuaresults.ac.in/view-results-56736281.html', 'https://jntuaresults.ac.in/view-results-56736282.html', 'https://jntuaresults.ac.in/view-results-56736283.html', 'https://jntuaresults.ac.in/view-results-56736284.html', 'https://jntuaresults.ac.in/view-results-56736285.html', 'https://jntuaresults.ac.in/view-results-56736286.html', 'https://jntuaresults.ac.in/view-results-56736303.html', 'https://jntuaresults.ac.in/view-results-56736277.html', 'https://jntuaresults.ac.in/view-results-56736276.html', 'https://jntuaresults.ac.in/view-results-56736271.html', 'https://jntuaresults.ac.in/view-results-56736272.html', 'https://jntuaresults.ac.in/view-results-56736273.html', 'https://jntuaresults.ac.in/view-results-56736274.html', 'https://jntuaresults.ac.in/view-results-56736275.html', 'https://jntuaresults.ac.in/view-results-56736266.html', 'https://jntuaresults.ac.in/view-results-56736267.html', 'https://jntuaresults.ac.in/view-results-56736268.html', 'https://jntuaresults.ac.in/view-results-56736269.html', 'https://jntuaresults.ac.in/view-results-56736270.html', 'https://jntuaresults.ac.in/view-results-56736264.html', 'https://jntuaresults.ac.in/view-results-56736265.html', 'https://jntuaresults.ac.in/view-results-56736260.html', 'https://jntuaresults.ac.in/view-results-56736261.html', 'https://jntuaresults.ac.in/view-results-56736262.html', 'https://jntuaresults.ac.in/view-results-56736263.html', 'https://jntuaresults.ac.in/view-results-56736256.html', 'https://jntuaresults.ac.in/view-results-56736257.html', 'https://jntuaresults.ac.in/view-results-56736258.html', 'https://jntuaresults.ac.in/view-results-56736259.html', 'https://jntuaresults.ac.in/view-results-56736252.html', 'https://jntuaresults.ac.in/view-results-56736253.html', 'https://jntuaresults.ac.in/view-results-56736254.html', 'https://jntuaresults.ac.in/view-results-56736242.html', 'https://jntuaresults.ac.in/view-results-56736241.html', 'https://jntuaresults.ac.in/view-results-56736239.html', 'https://jntuaresults.ac.in/view-results-56736240.html', 'https://jntuaresults.ac.in/view-results-56736238.html', 'https://jntuaresults.ac.in/view-results-56736237.html', 'https://jntuaresults.ac.in/view-results-56736236.html', 'https://jntuaresults.ac.in/view-results-56736235.html', 'https://jntuaresults.ac.in/view-results-56736234.html', 'https://jntuaresults.ac.in/view-results-56736233.html', 'https://jntuaresults.ac.in/view-results-56736226.html', 'https://jntuaresults.ac.in/view-results-56736227.html', 'https://jntuaresults.ac.in/view-results-56736228.html', 'https://jntuaresults.ac.in/view-results-56736229.html', 'https://jntuaresults.ac.in/view-results-56736230.html', 'https://jntuaresults.ac.in/view-results-56736231.html', 'https://jntuaresults.ac.in/view-results-56736232.html', 'https://jntuaresults.ac.in/view-results-56736225.html', 'https://jntuaresults.ac.in/view-results-56736221.html', 'https://jntuaresults.ac.in/view-results-56736222.html', 'https://jntuaresults.ac.in/view-results-56736223.html', 'https://jntuaresults.ac.in/view-results-56736224.html', 'https://jntuaresults.ac.in/view-results-56736219.html', 'https://jntuaresults.ac.in/view-results-56736220.html', 'https://jntuaresults.ac.in/view-results-56736206.html',
        #          'https://jntuaresults.ac.in/view-results-56736204.html', 'https://jntuaresults.ac.in/view-results-56736205.html', 'https://jntuaresults.ac.in/view-results-56736203.html', 'https://jntuaresults.ac.in/view-results-56736202.html', 'https://jntuaresults.ac.in/view-results-56736199.html', 'https://jntuaresults.ac.in/view-results-56736200.html', 'https://jntuaresults.ac.in/view-results-56736201.html', 'https://jntuaresults.ac.in/view-results-56736188.html', 'https://jntuaresults.ac.in/view-results-56736191.html', 'https://jntuaresults.ac.in/view-results-56736193.html', 'https://jntuaresults.ac.in/view-results-56736194.html', 'https://jntuaresults.ac.in/view-results-56736195.html', 'https://jntuaresults.ac.in/view-results-56736196.html', 'https://jntuaresults.ac.in/view-results-56736197.html', 'https://jntuaresults.ac.in/view-results-56736198.html', 'https://jntuaresults.ac.in/view-results-56736214.html', 'https://jntuaresults.ac.in/view-results-56736215.html', 'https://jntuaresults.ac.in/view-results-56736216.html', 'https://jntuaresults.ac.in/view-results-56736217.html', 'https://jntuaresults.ac.in/view-results-56736179.html', 'https://jntuaresults.ac.in/view-results-56736180.html', 'https://jntuaresults.ac.in/view-results-56736181.html', 'https://jntuaresults.ac.in/view-results-56736182.html', 'https://jntuaresults.ac.in/view-results-56736176.html', 'https://jntuaresults.ac.in/view-results-56736177.html', 'https://jntuaresults.ac.in/view-results-56736178.html', 'https://jntuaresults.ac.in/view-results-56736175.html', 'https://jntuaresults.ac.in/view-results-56736167.html', 'https://jntuaresults.ac.in/view-results-56736168.html', 'https://jntuaresults.ac.in/view-results-56736169.html', 'https://jntuaresults.ac.in/view-results-56736170.html', 'https://jntuaresults.ac.in/view-results-56736171.html', 'https://jntuaresults.ac.in/view-results-56736173.html', 'https://jntuaresults.ac.in/view-results-56736174.html', 'https://jntuaresults.ac.in/view-results-56736166.html', 'https://jntuaresults.ac.in/view-results-56736165.html', 'https://jntuaresults.ac.in/view-results-56736162.html', 'https://jntuaresults.ac.in/view-results-56736163.html', 'https://jntuaresults.ac.in/view-results-56736156.html', 'https://jntuaresults.ac.in/view-results-56736157.html', 'https://jntuaresults.ac.in/view-results-56736158.html', 'https://jntuaresults.ac.in/view-results-56736159.html', 'https://jntuaresults.ac.in/view-results-56736160.html', 'https://jntuaresults.ac.in/view-results-56736161.html', 'https://jntuaresults.ac.in/view-results-56736146.html', 'https://jntuaresults.ac.in/view-results-56736147.html', 'https://jntuaresults.ac.in/view-results-56736148.html', 'https://jntuaresults.ac.in/view-results-56736149.html', 'https://jntuaresults.ac.in/view-results-56736150.html', 'https://jntuaresults.ac.in/view-results-56736151.html', 'https://jntuaresults.ac.in/view-results-56736152.html', 'https://jntuaresults.ac.in/view-results-56736153.html', 'https://jntuaresults.ac.in/view-results-56736154.html', 'https://jntuaresults.ac.in/view-results-56736155.html', 'https://jntuaresults.ac.in/view-results-56736135.html', 'https://jntuaresults.ac.in/view-results-56736137.html', 'https://jntuaresults.ac.in/view-results-56736138.html', 'https://jntuaresults.ac.in/view-results-56736139.html', 'https://jntuaresults.ac.in/view-results-56736140.html', 'https://jntuaresults.ac.in/view-results-56736141.html', 'https://jntuaresults.ac.in/view-results-56736142.html', 'https://jntuaresults.ac.in/view-results-56736143.html', 'https://jntuaresults.ac.in/view-results-56736144.html', 'https://jntuaresults.ac.in/view-results-56736145.html', 'https://jntuaresults.ac.in/view-results-56736131.html', 'https://jntuaresults.ac.in/view-results-56736132.html', 'https://jntuaresults.ac.in/view-results-56736133.html', 'https://jntuaresults.ac.in/view-results-56736134.html', 'https://jntuaresults.ac.in/view-results-56736129.html', 'https://jntuaresults.ac.in/view-results-56736130.html', 'https://jntuaresults.ac.in/view-results-56736127.html', 'https://jntuaresults.ac.in/view-results-56736128.html', 'https://jntuaresults.ac.in/view-results-56736125.html', 'https://jntuaresults.ac.in/view-results-56736126.html', 'https://jntuaresults.ac.in/view-results-56736090.html', 'https://jntuaresults.ac.in/view-results-56736091.html', 'https://jntuaresults.ac.in/view-results-56736093.html', 'https://jntuaresults.ac.in/view-results-56736095.html', 'https://jntuaresults.ac.in/view-results-56736097.html', 'https://jntuaresults.ac.in/view-results-56736114.html', 'https://jntuaresults.ac.in/view-results-56736115.html', 'https://jntuaresults.ac.in/view-results-56736116.html', 'https://jntuaresults.ac.in/view-results-56736117.html', 'https://jntuaresults.ac.in/view-results-56736087.html', 'https://jntuaresults.ac.in/view-results-56736088.html', 'https://jntuaresults.ac.in/view-results-56736078.html', 'https://jntuaresults.ac.in/view-results-56736079.html', 'https://jntuaresults.ac.in/view-results-56736080.html', 'https://jntuaresults.ac.in/view-results-56736081.html', 'https://jntuaresults.ac.in/view-results-56736084.html', 'https://jntuaresults.ac.in/view-results-56736086.html', 'https://jntuaresults.ac.in/view-results-56736076.html', 'https://jntuaresults.ac.in/view-results-56736077.html', 'https://jntuaresults.ac.in/view-results-56736070.html', 'https://jntuaresults.ac.in/view-results-56736071.html', 'https://jntuaresults.ac.in/view-results-56736072.html', 'https://jntuaresults.ac.in/view-results-56736073.html', 'https://jntuaresults.ac.in/view-results-56736074.html', 'https://jntuaresults.ac.in/view-results-56736075.html', 'https://jntuaresults.ac.in/view-results-56736067.html', 'https://jntuaresults.ac.in/view-results-56736066.html', 'https://jntuaresults.ac.in/view-results-56736041.html', 'https://jntuaresults.ac.in/view-results-56736057.html', 'https://jntuaresults.ac.in/view-results-56736058.html', 'https://jntuaresults.ac.in/view-results-56736059.html', 'https://jntuaresults.ac.in/view-results-56736060.html', 'https://jntuaresults.ac.in/view-results-56736061.html', 'https://jntuaresults.ac.in/view-results-56736062.html', 'https://jntuaresults.ac.in/view-results-56736064.html', 'https://jntuaresults.ac.in/view-results-56736065.html', 'https://jntuaresults.ac.in/view-results-56736038.html', 'https://jntuaresults.ac.in/view-results-56736039.html', 'https://jntuaresults.ac.in/view-results-56736040.html', 'https://jntuaresults.ac.in/view-results-56736035.html', 'https://jntuaresults.ac.in/view-results-56736036.html', 'https://jntuaresults.ac.in/view-results-56736037.html', 'https://jntuaresults.ac.in/view-results-56736034.html', 'https://jntuaresults.ac.in/view-results-56736031.html', 'https://jntuaresults.ac.in/view-results-56736032.html', 'https://jntuaresults.ac.in/view-results-56736033.html', 'https://jntuaresults.ac.in/view-results-56736028.html', 'https://jntuaresults.ac.in/view-results-56736029.html', 'https://jntuaresults.ac.in/view-results-56736030.html', 'https://jntuaresults.ac.in/view-results-56736022.html', 'https://jntuaresults.ac.in/view-results-56736023.html', 'https://jntuaresults.ac.in/view-results-56736024.html', 'https://jntuaresults.ac.in/view-results-56736025.html', 'https://jntuaresults.ac.in/view-results-56736026.html', 'https://jntuaresults.ac.in/view-results-56736027.html', 'https://jntuaresults.ac.in/view-results-56736021.html', 'https://jntuaresults.ac.in/view-results-56736015.html', 'https://jntuaresults.ac.in/view-results-56736016.html', 'https://jntuaresults.ac.in/view-results-56736017.html', 'https://jntuaresults.ac.in/view-results-56736018.html', 'https://jntuaresults.ac.in/view-results-56736019.html', 'https://jntuaresults.ac.in/view-results-56736020.html', 'https://jntuaresults.ac.in/view-results-56736009.html', 'https://jntuaresults.ac.in/view-results-56736010.html', 'https://jntuaresults.ac.in/view-results-56736011.html', 'https://jntuaresults.ac.in/view-results-56736012.html', 'https://jntuaresults.ac.in/view-results-56736013.html', 'https://jntuaresults.ac.in/view-results-56736014.html', 'https://jntuaresults.ac.in/view-results-56736007.html', 'https://jntuaresults.ac.in/view-results-56736008.html', 'https://jntuaresults.ac.in/view-results-56736000.html', 'https://jntuaresults.ac.in/view-results-56736001.html', 'https://jntuaresults.ac.in/view-results-56736002.html', 'https://jntuaresults.ac.in/view-results-56736003.html', 'https://jntuaresults.ac.in/view-results-56736004.html', 'https://jntuaresults.ac.in/view-results-56736005.html', 'https://jntuaresults.ac.in/view-results-56736006.html', 'https://jntuaresults.ac.in/view-results-56735999.html', 'https://jntuaresults.ac.in/view-results-56735996.html', 'https://jntuaresults.ac.in/view-results-56735998.html', 'https://jntuaresults.ac.in/view-results-56735990.html', 'https://jntuaresults.ac.in/view-results-56735995.html', 'https://jntuaresults.ac.in/view-results-56736112.html', 'https://jntuaresults.ac.in/view-results-56736113.html', 'https://jntuaresults.ac.in/view-results-56736110.html', 'https://jntuaresults.ac.in/view-results-56736111.html', 'https://jntuaresults.ac.in/view-results-56736109.html', 'https://jntuaresults.ac.in/view-results-56736118.html', 'https://jntuaresults.ac.in/view-results-56736119.html', 'https://jntuaresults.ac.in/view-results-56736120.html', 'https://jntuaresults.ac.in/view-results-56736121.html', 'https://jntuaresults.ac.in/view-results-56736122.html',
        #          'https://jntuaresults.ac.in/view-results-56736107.html', 'https://jntuaresults.ac.in/view-results-56736106.html', 'https://jntuaresults.ac.in/view-results-56736098.html', 'https://jntuaresults.ac.in/view-results-56736104.html', 'https://jntuaresults.ac.in/view-results-56736105.html', 'https://jntuaresults.ac.in/view-results-56736099.html', 'https://jntuaresults.ac.in/view-results-56736100.html', 'https://jntuaresults.ac.in/view-results-56736102.html', 'https://jntuaresults.ac.in/view-results-56736124.html']

        AllpublishedResults = []

        for i in range(len(allTitles)):
            td = {
                "publishd_date": allDates[i],
                "title": allTitles[i],
                "url": allLinks[i],
            }

            AllpublishedResults.append(td)

        # with open('trash\\j.json', 'w') as f:
        #     json.dump(d, f)
        return AllpublishedResults

    @classmethod
    def getAllUrls(cls):
        site = cls.site
        soup = cls.soup
        # table = soup.find('table', {'class': 'ui table segment'})
        return [site+row['href'] for row in soup.findAll("a", href=True)]

    @classmethod
    def getUrls(cls, course, regulation):
        '''
        get all results links
        '''
        site = cls.site
        soup = cls.soup
        # table = soup.find('table', {'class': 'ui table segment'})
        return [site+row['href'] for row in soup.findAll("a", href=True) if ((course and regulation) in row.text) and ("B.Pharmacy" not in row.text)]

    @staticmethod
    def submiCredentials(driver, rollno, e):
        driver.get(e)
        field = driver.find_element_by_xpath(
            '/html/body/div/div[1]/div/div/center/table/tbody/tr/th/center/input[1]')
        btn = driver.find_element_by_xpath(
            '/html/body/div/div[1]/div/div/center/table/tbody/tr/th/center/input[2]')
        # print('enterning roll no')
        field.send_keys(rollno)
        # print('button click')
        btn.click()

        def waitForPageLoad():
            html = driver.page_source
            while True:
                # print('checking for  source')
                t = driver.page_source
                if html != t:
                    # print('source changed')
                    return 0

        # print('witing for loading')
        waitForPageLoad()
        # print('capturing screenshot')
        # driver.save_screenshot("images\\screenshot.png")
        return driver.page_source

    @staticmethod
    def userDetails(res):
        src = res
        soup = BeautifulSoup(src, 'lxml')
        user = {}
        for i in soup.findAll('b'):
            if i.text == 'Hall Ticket No :':
                t = {'Hall Ticket No': i.next_sibling[:10].upper()}
                user.update(t)
            elif i.text == 'Student name: ':
                t = {'Student name': i.next_sibling}
                user.update(t)
        return user

    @staticmethod
    def userResults(res, regulation):
        src = res
        soup = BeautifulSoup(src, 'lxml')
        headder = soup.find('h1', {'class': 'ui info message bxinfo'})
        table = soup.find('table', {'class': 'ui table segment'})
        if regulation == "R15":
            resl = ['Subject Code', 'Subject Name',  'Internals', 'Externals',
                    'Total Marks', 'Result Status', 'Credits', 'Grades']
        elif regulation == "R19":
            resl = ['Subject Code', 'Subject Name',  'Result Status', 'Grades',
                    'Credits']
        else:
            resl = []
            print("invalid course +++++++++++++++++") # log
        try:
            values = [i.text for i in table.findAll("td")]
            l = []
            _from = 0
            _to = 8
            for _ in range(len(values)//8):
                x = {}
                for i, j in zip(resl, values[_from:_to]):
                    x[i] = j
                _from += 8
                _to += 8
                l.append(x)
            data = {str(headder.text.strip('Title : ')): l}
            return data
        except:
            # return {'title': headder.text.strip('Title : '), 'data': None}
            pass

    def getData(self, driver, urls):
        try:
            x = {}
            l = []
            userGoten = 0
            for i, e in enumerate(urls):
                print(len(urls) - i)
                res = Automate.submiCredentials(driver, self.rollno, e)
                if userGoten == 0:
                    ud = {'user': Automate.userDetails(res)}
                    if len(ud['user']) == 2:
                        x.update(ud)
                        userGoten += 1
                        
                regulation = self.regulation
                ur = Automate.userResults(res=res, regulation=regulation)
                try:
                    if ur is not None: 
                        l.append(ur)
                except Exception as identifier:
                    pass
            x.update({'results': l})
            return x
        except Exception as e:
            return e

    def start(self):

        # print("this driver for heorku")
        # options = Options()
        # options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        # options.add_argument("--headless")
        # options.add_argument("--disable-dev-shm-usage")
        # options.add_argument("--no-sandbox")
        # driver = webdriver.Chrome(executable_path=os.environ.get(
        #     "CHROMEDRIVER_PATH"), options=options)

        # print("this driver for local")
        # options = Options()
        # options.headless = True
        # driver = webdriver.Chrome(
        #     executable_path='res/chromedriver', options=options)

        options = Options()
        options.headless = True
        driver = webdriver.Chrome(
            executable_path="/home/wikyprash/myFiles/MyWorkSpace/fapp/jntua_world_api/res/chromedriver",
            options=options)

        urls = Automate.getUrls(course=self.course, regulation=self.regulation)
        print(urls)
        data = self.getData(driver, urls)

        print('closing browser')
        driver.quit()
        return data


if __name__ == "__main__":
    print("---")
    x = Automate(rollno="183g1a0505", course="B.Tech")
    # x.setRegulation("R19")
    print('calling start')

    
    print(x.start())
