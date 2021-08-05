import requests
'''

url = "http://127.0.0.1:5000/api/ngo"
obj = {
    'nameNGO':"Spendenhaus",
    'emailNGO':"ngo@ngo.com"
    }
x = requests.post(url,headers = obj)
print(x.text)


url = "http://127.0.0.1:5000/api/image"
obj = {
    'fileImage':"https://www.unicef.de/blob/221778/3c89d03bff7e4573ed1e8ab4fbd6d597/drc-mangelernaehrung-plumpy-nut-uni232071-data.jpg",
    'descriptionImage':"Eine Beschreibung",
    'formatImage':"image/jpg"
}
x = requests.post(url,headers = obj)
print(x.text)


url = "http://127.0.0.1:5000/api/description/summary"
obj = {
    'idImage':"1",
    'descriptionSummary':"Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum."
}
x = requests.post(url,headers = obj)
print(x.text)


url = "http://127.0.0.1:5000/api/description/solution"
obj = {
    'idImage':"1",
    'descriptionSolution':"dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum."
}
x = requests.post(url,headers = obj)
print(x.text)


url = "http://127.0.0.1:5000/api/description/problem"
obj = {
    'idImage':"1",
    'descriptionproblem':"ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum."
}
x = requests.post(url,headers = obj)
print(x.text)


url = "http://127.0.0.1:5000/api/projects"
obj = {
    'nameProject':"TestProjekt",
    'statusProject':'100.0',
    'amountProject':"1222.0",
    'shouldAmountProject':"4984844.0",
    'shortDescription': "teststestt",
    'paymentInformationProject':"kein Plan",
    'pageProject':"https://google.com",
    'idImage':"1",
    'idSolution':"1",
    'idProblem':"1",
    'idSummary':"1"
}
x = requests.post(url,headers = obj)
print(x.text)


url = "http://127.0.0.1:5000/api/projects"
obj = {
    'nameProject':"ZweitesTestProjekt",
    'statusProject':"0",
    'amountProject':"1222.0",
    'shouldAmountProject':"8888.0",
    'shortDescription': "teststestt",
    'paymentInformationProject':"Immernoch kein Plan",
    'pageProject':"https://google.com",
    'idImage':"1",
    'idSolution':"1",
    'idProblem':"1",
    'idSummary':"1"
}
x = requests.post(url,headers = obj)
print(x.text)


url = "http://127.0.0.1:5000/api/milestone"
obj = {
    "nameMilestone":"erstes",
    "amountMilestone":"800.0",
    "descriptionMilestone":"jiojaisd",
    "idProject":"2"
}
x = requests.post(url,headers = obj)
print(x.text)

url = "http://127.0.0.1:5000/api/milestone"
obj = {
    "nameMilestone":"zweites",
    "amountMilestone":"999.0",
    "descriptionMilestone":"dddddasda",
    "idProject":"2"
}
x = requests.post(url,headers = obj)
print(x.text)

url = "http://127.0.0.1:5000/api/milestone"
obj = {
    "nameMilestone":"Drittes",
    "amountMilestone":"222.0",
    "descriptionMilestone":"ffefegegegg",
    "idProject":"1"
}
x = requests.post(url,headers = obj)
print(x.text)


url = "http://127.0.0.1:5000/api/users/signup"
obj = {
    "email":"test@test.com",
    "password":"123",
    "firstname":"tester",
    "lastname":"testy"
}
x = requests.post(url,headers = obj)
print(x.text)


url = "http://127.0.0.1:5000/api/payment"
obj = {
    "idUser":"1",
    "idProject":"1",
    "amountPayment":"100.0",
    "statePayment":"2"
}
x = requests.post(url,headers = obj)
print(x.text)


url = "http://127.0.0.1:5000/api/payment"
obj = {
    "idUser":"1",
    "idProject":"2",
    "amountPayment":"200.0",
    "statePayment":"1"
}
x = requests.post(url,headers = obj)
print(x.text)


url = "http://127.0.0.1:5000/api/ngo"
obj = {
    'nameNGO':"Fussballspenden",
    'emailNGO':"ngo@irgendwasmitFussball.com"
    }
x = requests.post(url,headers = obj)
print(x.text)




url = "http://127.0.0.1:5000/api/description/summary/1"
obj = {
    "descriptionSummary":"Funktioniert Summary es?",
    'idImage': "1"
}
x = requests.put(url,headers=obj)
print(x.text)


url = "http://127.0.0.1:5000/api/description/solution/1"
obj = {
    "descriptionSolution":"Funktioniert Solution es?",
    'idImage': "1"
}
x = requests.put(url,headers=obj)
print(x.text)


url = "http://127.0.0.1:5000/api/description/problem/1"
obj = {
    "descriptionProblem":"Funktioniert Problem es?",
    'idImage': "1"
}
x = requests.put(url,headers=obj)
print(x.text)


url = "http://127.0.0.1:5000/api/projects/1"
obj = {
    'idSolution':"1",
    'idProblem':"1",
    'idSummary':"1"
}
x = requests.put(url,headers=obj)
print(x.text)

url = "http://127.0.0.1:5000/api/projects/2"
obj = {
    'idSolution':"2",
    'idProblem':"2",
    'idSummary':"2"
}
x = requests.put(url,headers=obj)
print(x.text)

url = "http://127.0.0.1:5000/api/projects/3"
obj = {
    'idSolution':"3",
    'idProblem':"3",
    'idSummary':"3"
}
x = requests.put(url,headers=obj)
print(x.text)

url = "http://127.0.0.1:5000/api/projects/4"
obj = {
    'idSolution':"3",
    'idProblem':"3",
    'idSummary':"3"
}
x = requests.put(url,headers=obj)
print(x.text)


url = "http://127.0.0.1:5000/api/projects/5"
obj = {
    'idSolution':"3",
    'idProblem':"3",
    'idSummary':"3"
}
x = requests.put(url,headers=obj)
print(x.text)


url = "http://127.0.0.1:5000/api/projects/6"
obj = {
    'idSolution':"3",
    'idProblem':"3",
    'idSummary':"3"
}
x = requests.put(url,headers=obj)
print(x.text)


url = "http://127.0.0.1:5000/api/projects/7"
obj = {
    'idSolution':"3",
    'idProblem':"3",
    'idSummary':"3"
}
x = requests.put(url,headers=obj)
print(x.text)


url = "http://127.0.0.1:5000/api/projects/8"
obj = {
    'idSolution':"3",
    'idProblem':"3",
    'idSummary':"3"
}
x = requests.put(url,headers=obj)
print(x.text)


url = "http://127.0.0.1:5000/api/projects/9"
obj = {
    'idSolution':"3",
    'idProblem':"3",
    'idSummary':"3"
}
x = requests.put(url,headers=obj)
print(x.text)


url = "http://127.0.0.1:5000/api/projects/10"
obj = {
    'idSolution':"3",
    'idProblem':"3",
    'idSummary':"3"
}
x = requests.put(url,headers=obj)
print(x.text)



url = "http://127.0.0.1:5000/api/projects/11"
obj = {
    'idSolution':"3",
    'idProblem':"3",
    'idSummary':"3"
}
x = requests.put(url,headers=obj)
print(x.text)


url = "http://127.0.0.1:5000/api/projects/12"
obj = {
    'idSolution':"3",
    'idProblem':"3",
    'idSummary':"3"
}
x = requests.put(url,headers=obj)
print(x.text)




url = "http://127.0.0.1:5000/api/payment/1"
obj = {
    'idUser':"1",
    'idProject':"1"
}
x = requests.put(url,headers=obj)
print(x.text)


url = "http://127.0.0.1:5000/api/payment/2"
obj = {
    'idUser':"1",
    'idProject':"3"
}
x = requests.put(url,headers=obj)
print(x.text)

url = "http://127.0.0.1:5000/api/payment/3"
obj = {
    'idUser':"4",
    'idProject':"1"
}
x = requests.put(url,headers=obj)
print(x.text)

url = "http://127.0.0.1:5000/api/payment/4"
obj = {
    'idUser':"2",
    'idProject':"2"
}
x = requests.put(url,headers=obj)
print(x.text)

url = "http://127.0.0.1:5000/api/payment/5"
obj = {
    'idUser':"1",
    'idProject':"3"
}
x = requests.put(url,headers=obj)
print(x.text)


url = "http://127.0.0.1:5000/api/projects"
obj = {
    'nameProject':"Besonderes Projekt",
    'statusProject':'100.0',
    'amountProject':"1222.0",
    'shouldAmountProject':"4984844.0",
    'shortDescription': "teststestt",
    'pageProject':"https://google.com",
    'idImage':"1",
    'idSolution':"1",
    'idProblem':"1",
    'idSummary':"1"
}
x = requests.post(url,headers = obj)
print(x.text)
'''
url = "http://127.0.0.1:5000/api/payment"
obj = {
    "idUser":"1",
    "idProject":"13",
    "amountPayment":"200.0",
    "statePayment":"1"
}
x = requests.post(url,headers = obj)
print(x.text)
