# import requests
# from bs4 import BeautifulSoup
#
# web = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=")
#
#
# soup = BeautifulSoup(web.content, 'lxml')
# description = soup.find_all('li')
#
#
#
# for i in description:
#     text = i.text
#     print(text)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
from tabulate import tabulate

head = [
    "Job Description",
    "KeySkills"
]

table = [
    [
        "2 to 3 Years experience in Python.Expert in Python ,  with knowledge of at least one Python web framework  Flask ,  Django etc.Expert in server programming.Go... More Details",
        "rest  ,  python  ,  database  ,  django  ,  debugging  ,  mongodb"
    ],
    [
        "Python Developer ELIGIBILITY: FRESHERS Your RoleUnderstand requirements and participate in project road map discussions in order to design ,  estimate ,  and deliver... More Details",
        "python  ,  web technologies  ,  linux  ,  mobile  ,  mysql  ,  angularjs  ,  javascript"
    ],
    [
        "Excellent understanding of machine learning techniques and algorithms ,  such as k-NN ,  Naive Bayes ,  SVM ,  Decision Forests ,  etc.Experience with common data science tool... More Details",
        "python  ,  research  ,  python programmer  ,  Machine Learning  ,  Pattern Recognition  ,  Image Processing  ,  Digital Image  ,  Signal Processing  ,  Electronic Circuits  ,  Network Analysis"
    ]
]

content = tabulate(table, headers=head, tablefmt="grid")
print(content)
# import africastalking
#
# airtime = africastalking.Airtime
# phone_number = "+2347042546311"
# amount = 5000
# currency_code = "NGN"
#
# try:
#     response = airtime.send(phone_number=phone_number, amount=amount, currency_code=currency_code)
#     print(response)
# except Exception as e:
#     print(f"Encountered an error while sending airtime. More error details below\n {e}")