#from flask import Flask, render_template, flash, request, url_for, redirect, session
#from content_management import Content
import MySQLdb #import escape_string as thwart
from datetime import datetime, date

from dbconnect import connection


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
    data = User(content)
    return data

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
        c.execute("UPDATE users SET email = " + "'" + self.email + "' WHERE id = " + str(self.uid) + "")
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


    #def change_gender(self, input):
    ##    c, conn = connection()
    #    content = c.execute("SELECT id FROM users WHERE email = " + "'" + self.email + "'")
    #    content = c.fetchone()
    #    #print(content)
    #    if content == None:
    #        print("Does not exist")
    #        return
    #    self.gender = input
    #    c.execute("UPDATE users SET gender = " + "'" + self.gender + "' WHERE email = '" + str(self.email) + "'")
    #    conn.commit()
#
    #def change_year(self, input):
    #    c, conn = connection()
    #    content = c.execute("SELECT id FROM users WHERE email = " + "'" + self.email + "'")
    #    content = c.fetchone()
        #print(content)
    #    if content == None:
    #        print("Does not exist")
    #        return
    #    self.year = input
    #    c.execute("UPDATE users SET year = " + "'" + self.year + "' WHERE email = '" + str(self.email) + "'")
    #    conn.commit()


    def write(self):
        c, conn = connection()
        string = "'" + self.first_name + "', '" + self.last_name + "', '" + self.email + "', '"  + self.birth_day + "', '"+ self.password + "'"
        c.execute("INSERT INTO users (uid, firstname, lastname, email, birthday, password) VALUES (NULL, " + string + ")")
        c.execute("INSERT INTO profile (uid) values (null)")
        print("processed")
        conn.commit()

    def print_user(self):
        print(self.uid)
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.birth_day)
        print(self.password)
