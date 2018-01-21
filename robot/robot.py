
# Перед запуском закрыть браузер!
# python3 robot.py
# py robot.py

from bs4 import BeautifulSoup, SoupStrainer # Windows py -m  pip install bs4
from requests import  Session
from generator import Generator
from random import randint, sample
from config_robot import *
from time import sleep

gener = Generator(LOGIN_LENGTH,PASSWORD_LENGTH)
users = gener.list_user(NUMBER_OF_USERS)
session = Session()
fileusers = open ('fileusers.txt', 'a')

for user in users:
    print("Login : " + user)
    print("Password : " + users[user])

    # Запрос страницы регистрации
    sleep(TIMEPAUS)
    response = session.get(URL_REGISTER ) 
    print(URL_REGISTER  + "    status_code :  " + str(response.status_code))

    soup = BeautifulSoup(response.content, 'html.parser', parse_only=SoupStrainer('input'))
    csrf_value = ''
    for tag in soup:
        if tag.get('name') == 'csrfmiddlewaretoken':
            csrf_value = str(tag.get('value'))

    # запрос регистраци
    sleep(TIMEPAUS)  
    response = session.post( URL_REGISTER ,  data  =  { 'csrfmiddlewaretoken': csrf_value, 'username': user, 'password1': users[user], 'password2': users[user], 'register': 'Submit'})
    print("Register  status_code :  " + str(response.status_code))
    if response.status_code == 200:
        print("fileusers.txt ok")
        fileusers.write(user + '\n')
        fileusers.write(users[user] + '\n')
        fileusers.write("-------------------------------------------" + '\n' + '\n')
    else:
        print("NOT Register ")
        exit(1)
    print("Register ")       
    
    # Запрос HOME
    sleep(TIMEPAUS)
    response = session.get(URL_HOME)
    print("home  status_code :  " + str(response.status_code))

    # Печать post
    for products in range(0,randint(1, MAX_POST_PER_USER)):
        # Запрос post
        sleep(TIMEPAUS)
        response = session.get(URL_POST)
        print("Post " + str(products) + "  status_code :  " + str(response.status_code))

        soup = BeautifulSoup(response.content, 'html.parser', parse_only=SoupStrainer('input'))
        csrf_value = ''
        for tag in soup:
            if tag.get('name') == 'csrfmiddlewaretoken':
                csrf_value = str(tag.get('value'))

        # запрос печатать post 
        sleep(TIMEPAUS)  
        response = session.post( URL_POST ,  data  =  { 'csrfmiddlewaretoken': csrf_value,'title': title_post, 'text': text_post})
        print("home  status_code :  " + str(response.status_code))
    
    # LIKES
    for products in range(0,randint(1, MAX_LIKES_PER_USER)):
        # Запрос home
        sleep(TIMEPAUS)
        response = session.get(URL_HOME)
        print("LIKES " + str(products) + " status_code :  " + str(response.status_code))

        soup = BeautifulSoup(response.content, 'html.parser', parse_only=SoupStrainer('input'))
        csrf_value = ''
        for tag in soup:
            if tag.get('name') == 'csrfmiddlewaretoken':
                csrf_value = str(tag.get('value'))
                
        souplike = BeautifulSoup(response.content, 'html.parser', parse_only=SoupStrainer('button'))
        
        list_button = [tag.get('value') for tag in souplike]
        random_button = sample(list_button, 1)
        
        # запрос like
        sleep(TIMEPAUS) 
        URL_LIKE = URL_HOME + "post/" + random_button[0] + '/'
        response = session.post( URL_LIKE,  data  =  { 'csrfmiddlewaretoken': csrf_value, 'Like': random_button[0]})
        print(URL_LIKE + " home  status_code :  " + str(response.status_code))
    
    # Запрос выхода
    sleep(TIMEPAUS)
    response = session.get(URL_LOGOUT)
    print("LOGOUT  status_code :  " + str(response.status_code))
    print("------------------------------------------------------------")
    
fileusers.close()
exit()#del

