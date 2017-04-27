#from flask import Flask, render_template, flash, request, url_for, redirect, session
#from content_management import Content
import MySQLdb #import escape_string as thwart
from datetime import datetime, date

from dbconnect import connection

c, conn = connection()
class User_list:

    data = []

    def __init__(self, input_arr):
        self.data = []
        #print(str(len(input_arr)) + " Hello")
        for i in range(len(input_arr)):
            self.data.append(User(input_arr[i]))

    def print_data(self):
        #print(self.data)
        print("*************************************************************")
        print
        for i in self.data:
            i.print_user()
            print
        print("************************************************************")

    def add_user(self, input_user):
        self.data.append(input_user)

def read(email_input):
    c, conn = connection()
    content = c.execute("SELECT * FROM users WHERE email = " + "'" + email_input + "'")
    content = c.fetchone()
    #print(content)
    if content == None:
        print("Does not exist")
        return
    data = User(content)
    #read_uid = data.uid
    c, conn = connection()
    content = c.execute("SELECT * FROM profile WHERE uid = " + str(data.uid))
    content = c.fetchone()
    #print(content)
    data_profile = Profile(content)
    return data, data_profile

def get_uid(email_input):
    c, conn = connection()
    content = c.execute("SELECT uid FROM users WHERE email = " + "'" + email_input + "'")
    content = c.fetchone()
    return content[0]

class User:
    uid = 0
    first_name = ""
    last_name = ""
    email=""
    birth_day = ""
    passord = ""
    gender = ""
    year = ""

    def __init__(self, input):

        self.uid = input[0]
        self.first_name = input[1]
        self.last_name = input[2]
        self.email = input[3]
        self.birth_day = input[4]
        self.password = input[5]
        #self.gender = input[6]
        #self.year = input[7]

    def change_first_name(self, input):
        c, conn = connection()
        content = c.execute("SELECT uid FROM users WHERE email = " + "'" + self.email + "'")
        content = c.fetchone()
        #print(content)
        if content == None:
            print("Does not exist")
            return
        self.uid = content[0]
        self.first_name = input
        c.execute("UPDATE users SET firstname = " + "'" + self.first_name + "' WHERE email = '" + str(self.email) + "'")
        conn.commit()

    def change_last_name(self, input):
        c, conn = connection()
        content = c.execute("SELECT uid FROM users WHERE email = " + "'" + self.email + "'")
        content = c.fetchone()
        #print(content)
        if content == None:
            print("Does not exist")
            return
        self.last_name = input
        c.execute("UPDATE users SET last_name = " + "'" + self.last_name + "' WHERE email = '" + str(self.email) + "'")
        conn.commit()


    def change_email(self, input):
        c, conn = connection()
        content = c.execute("SELECT uid FROM users WHERE email = " + "'" + self.email + "'")
        content = c.fetchone()
        #print(content)
        if content == None:
            print("Does not exist")
            return
        self.uid = content[0]
        self.email = input
        c.execute("UPDATE users SET email = " + "'" + self.email + "' WHERE uid = " + str(self.uid) + "")
        conn.commit()

    def change_birth_day(self, input):
        c, conn = connection()
        content = c.execute("SELECT uid FROM users WHERE email = " + "'" + self.email + "'")
        content = c.fetchone()
        #print(content)
        if content == None:
            print("Does not exist")
            return
        self.birth_day = input
        c.execute("UPDATE users SET birth_day = " + "'" + self.birth_day + "' WHERE email = '" + str(self.email) + "'")
        conn.commit()

    def change_password(self, input):
        c, conn = connection()
        content = c.execute("SELECT uid FROM users WHERE email = " + "'" + self.email + "'")
        content = c.fetchone()
        #print(content)
        if content == None:
            print("Does not exist")
            return
        self.password = input
        c.execute("UPDATE users SET password = " + "'" + self.password + "' WHERE email = '" + str(self.email) + "'")
        conn.commit()

    def write(self):
        c, conn = connection()
        string = "'" + self.first_name + "', '" + self.last_name + "', '" + self.email + "', '"  + self.birth_day + "', '"+ self.password + "'"
        c.execute("INSERT INTO users (uid, firstname, lastname, email, birthday, password) VALUES (NULL, " + string + ")")
        c.execute("INSERT INTO profile values (null, ' ', ' ', ' ', ' ',  ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')")
        print("processed")
        conn.commit()

    def print_user(self):
        print(self.uid)
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.birth_day)
        print(self.password)


class Profile:
    uid = 0
    gender = None
    year = None
    interestedIn = None
    major = None
    secondMajor = None
    minor = None
    location = None
    nickname = None
    cityOrigin = None
    stateOrigin = None
    countryOrigin = None
    dorm = None
    music = None
    eats = None
    about = None

    def __init__(self, input):
        self.uid = input[0]
        self.gender = input[1]
        self.year = input[2]
        self.interestedIn = input[3]
        self.major = input[4]
        self.secondMajor = input[5]
        self.minor = input[6]
        self.location = input[7]
        self.nickname = input[8]
        self.cityOrigin = input[9]
        self.stateOrigin = input[10]
        self.countryOrigin = input[11]
        self.dorm = input[12]
        self.music = input[13]
        self.eats = input[14]
        self.about = input[15]

    def update_profile(self):

        c.execute("UPDATE profile set gender = " + "'" + self.gender + "' where uid = " + str(self.uid))
        c.execute("UPDATE profile set year = " + "'" + self.year + "' where uid = " + str(self.uid))
        c.execute("UPDATE profile set interestedIn = " + "'" + self.interestedIn + "' where uid = " + str(self.uid))
        c.execute("UPDATE profile set major = " + "'" + self.major + "' where uid = " + str(self.uid))
        c.execute("UPDATE profile set 2ndMajor = " + "'" + self.secondMajor + "' where uid = " + str(self.uid))
        c.execute("UPDATE profile set minor = " + "'" + self.minor + "' where uid = " + str(self.uid))
        c.execute("UPDATE profile set location = " + "'" + self.location + "' where uid = " + str(self.uid))
        c.execute("UPDATE profile set nickname = " + "'" + self.nickname + "' where uid = " + str(self.uid))
        c.execute("UPDATE profile set cityOrigin = " + "'" + self.cityOrigin + "' where uid = " + str(self.uid))
        c.execute("UPDATE profile set stateOrigin = " + "'" + self.stateOrigin + "' where uid = " + str(self.uid))
        c.execute("UPDATE profile set countryOrigin = " + "'" + self.countryOrigin + "' where uid = " + str(self.uid))
        c.execute("UPDATE profile set dorm = " + "'" + self.dorm + "' where uid = " + str(self.uid))
        c.execute("UPDATE profile set music = " + "'" + self.music + "' where uid = " + str(self.uid))
        c.execute("UPDATE profile set eats = " + "'" + self.eats + "' where uid = " + str(self.uid))
        c.execute("UPDATE profile set about = " + "'" + self.about + "' where uid = " + str(self.uid))
        print("processed")
        conn.commit()

    def print_profile(self):
        print(self.uid)
        print(self.gender)
        print(self.year)
        print(self.interestedIn)
        print(self.major)
        print(self.secondMajor)
        print(self.minor)
        print(self.location)
        print(self.nickname)
        print(self.cityOrigin)
        print(self.stateOrigin)
        print(self.countryOrigin)
        print(self.dorm)
        print(self.music)
        print(self.eats)
        print(self.about)

    def update_gender(self, input):
        self.gender = input
        c, conn = connection()
        c.execute("UPDATE profile SET gender = " + "'" + self.gender + "' WHERE uid = " + str(self.uid) + "")
        conn.commit()

    def update_year(self, input):
        self.year = input
        c.execute("UPDATE profile SET year = " + "'" + self.year + "' WHERE uid = " + str(self.uid) + "")
        conn.commit()

    def update_interestedIn(self, input):
        self.interestedIn = input
        c.execute("UPDATE profile SET interestedIn = " + "'" + self.interestedIn + "' WHERE uid = " + str(self.uid) + "")
        conn.commit()

    def update_major(self, input):
        self.major = input
        c.execute("UPDATE profile SET major = " + "'" + self.major + "' WHERE uid = " + str(self.uid) + "")
        conn.commit()

    def update_secondMajor(self, input):
        self.secondMajor = input
        c.execute("UPDATE profile SET 2ndMajor = " + "'" + self.secondMajor + "' WHERE uid = " + str(self.uid) + "")
        conn.commit()

    def update_minor(self, input):
        self.minor = input
        c.execute("UPDATE profile SET minor = " + "'" + self.minor + "' WHERE uid = " + str(self.uid) + "")
        conn.commit()

    def update_location(self, input):
        self.location = input
        c.execute("UPDATE profile SET location = " + "'" + self.location + "' WHERE uid = " + str(self.uid) + "")
        conn.commit()

    def update_nickname(self, input):
        self.nickname = input
        c.execute("UPDATE profile SET nickname = " + "'" + self.nickname + "' WHERE uid = " + str(self.uid) + "")
        conn.commit()

    def update_cityOrgin(self, input):
        self.cityOrigin = input
        c.execute("UPDATE profile SET cityOrigin = " + "'" + self.cityOrigin + "' WHERE uid = " + str(self.uid) + "")
        conn.commit()

    def update_stateOrigin(self, input):
        self.gender = input
        c.execute("UPDATE profile SET stateOrigin = " + "'" + self.stateOrigin + "' WHERE uid = " + str(self.uid) + "")
        conn.commit()

    def update_countryOrigin(self, input):
        self.gender = input
        c.execute("UPDATE profile SET countryOrigin = " + "'" + self.countryOrigin + "' WHERE uid = " + str(self.uid) + "")
        conn.commit()

    def update_dorm(self, input):
        self.dorm = input
        c.execute("UPDATE profile SET dorm = " + "'" + self.dorm + "' WHERE uid = " + str(self.uid) + "")
        conn.commit()

    def update_music(self, input):
        self.music = input
        c.execute("UPDATE profile SET music = " + "'" + self.music + "' WHERE uid = " + str(self.uid) + "")
        conn.commit()

    def update_eats(self, input):
        self.eats = input
        c.execute("UPDATE profile SET eats = " + "'" + self.eats + "' WHERE uid = " + str(self.uid) + "")
        conn.commit()

    def update_about(self, input):
        self.about = input
        c.execute("UPDATE profile SET about = " + "'" + self.about + "' WHERE uid = " + str(self.uid) + "")
        conn.commit()
