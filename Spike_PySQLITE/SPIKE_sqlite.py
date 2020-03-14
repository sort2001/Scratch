# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlite3
from sqlite3 import Error
import csv
import datetime

ScheduleNames = ['9-80A', '9-80B', '10-40', 'StdWW', 'PartTime']
DayNames = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', "Thursday", 'Friday']
AttTypes = ['Straight Time','Exempt Extended','PTO','Modified Time - Worked','Modified Time - Off']
SectionHeads = ['Andrew M Vandivort','JOEL RICHARD DIERKS','John P Gaines','Paul J Vollmer','Stephen S Johnson','Steven Arthur Ortmann']
InpHdr = ['Date','Name','Peoplesoft','Send CCtr','Prem Number','Charge Number','Charge Number Desc','Ext','Ext Desc','Activity Type','Att/Abs Type','Location Code','From','To','Activity','Activity Desc','Hours','Explanation','Status','Approved By','Approve']

class TC_Inputs(object):
    def __init__(self):
        self.filename = 'export_20171031165609.csv'
        
    def parseInput(self):
        with open(self.filename ) as csvfile:
            reader = csv.DictReader(csvfile,InpHdr)
            first = True
            for row in reader:
                if first==False:
                    if row['Att/Abs Type']!='':
                        print(row['Date'], row['Peoplesoft'], row['Att/Abs Type'], row['Hours'])
                        self.writeRecord(row)
                else:
                     first = False
                     
    def writeRecord(self, aRow):
        #sDate = datetime.datetime.strptime(aRow['Date'], '%m/%d/%y').date()       
        slist = aRow['Date'].split("/")
        rDate = datetime.date(int(slist[2]),int(slist[0]),int(slist[1]))       
        ppls = int(aRow['Peoplesoft'])
        sHours = aRow['Hours']
        if sHours[0] == "'":
            sHours = sHours[1:]
        hours = float(sHours)
            
        iType = -1
        attType = str(aRow['Att/Abs Type'])
        if attType.startswith(AttTypes[0]):
            iType = 0
        elif attType.startswith(AttTypes[1]):
            iType = 1
        elif attType.startswith(AttTypes[2]):
            iType = 2
        elif attType.startswith(AttTypes[3]):
            iType = 3
        elif attType.startswith(AttTypes[4]):
            iType = 4
            
        #select the record where date, id, attType
        cmd = '''SELECT hours FROM inputs WHERE 
        '''
        cur.execute('SELECT hours FROM inputs WHERE date = {d}, peoplesoft = {p}, type = {t}'.\
        format(d=rDate, p=ppls, t=iType))
        all_rows = c.fetchall()
        print('2):', all_rows)
        #if found
        if all_rows.len() > 0:
            #update hours
            cur.execute('UPDATE inputs SET hours = {h} WHERE date = {d}, peoplesoft = {p}, type = {t}'.\
            format(h=str(float(all_rows[0].hours) + hours), d=rDate, p=ppls, t=iType)
        #else
        #insert record

        
    def createInputs(self):
        try:
            print 'Creating inputs table'
            cur = self.conn.cursor()
            
            #Try to drop the table in case it's already there
            try:
                cmd = '''DROP TABLE inputs'''
                cur.execute(cmd)
                self.conn.commit()
                print 'Dropped table inputs'
            except Error as e1:
                #no action, it may have not been there
                print 'Table inputs not found'
                
            
            cmd = '''CREATE TABLE inputs(
                        id INTEGER PRIMARY KEY, 
                        date DATE,
                        peoplesoft INTEGER,
                        type INTEGER,
                        hours FLOAT)'''
            cur.execute(cmd)
            self.conn.commit()
            print 'Created table inputs'
        except:
            print 'Failed to create cursor.'

       
class Employee(object):
    def __init__(self, aName = ''):
        self.id = 0
        self.name = aName
        self.schedule = '9-80'
        self.custom = False
        self.expected = 40.0
        self.hours = [0,0,0,0,0,0,0]
        self.sectionHead = ''
        self.approvedForModTime = False
        self.email = ''
        self.phone = ''
    
class Model(object):
    def __init__(self):
        self.conn = None
        self.cur = None

    def createConnection(self, db_file = 'timecard.db'):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        
        try:
            self.conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

    def allEmps(self):
        res = None
        try:
            cur = self.conn.cursor()
            res = cur.execute("SELECT * FROM emps")
        except Error as e:
            print e
        return res
   
    def dumpEmps(self):
        try:
            cur = self.allEmps()
            for row in cur:
                print row
        except Error as e:
            print e
           
    def checkTable(self):
        ''' check to see if a critical table exists, if not it will need to be created
        employees
        authorizations
        '''
        try:
             cur = self.conn.cursor()
             cur.execute("SELECT * FROM emps")
        except Error as e:
            print(e)
            self.createEmployees()
            
    def createEmployees(self):
        try:
            print 'Creating emps table'
            cur = self.conn.cursor()
            
            #Try to drop the table in case it's already there
            try:
                cmd = '''DROP TABLE emps'''
                cur.execute(cmd)
                self.conn.commit()
                print 'Dropped table emps'
            except Error as e1:
                #no action, it may have not been there
                print 'Table emps not found'
                
            
            cmd = '''CREATE TABLE emps(
                        id INTEGER PRIMARY KEY, 
                        name TEXT,
                        schedule TEXT,
                        custom INTEGER,
                        expected FLOAT,
                        sectionHead TEXT,
                        approvedForModTime INTEGER,
                        email TEXT,
                        phone TEXT,
                        sa FLOAT,
                        su FLOAT,
                        mo FLOAT,
                        tu FLOAT,
                        we FLOAT,
                        th FLOAT,
                        fr FLOAT)'''
            cur.execute(cmd)
            self.conn.commit()
            print 'Created table emps'
            
            #Populate the table with 
            with open('10866_EmpRoster_v2.csv', 'r') as csvfile:
                employeeReader = csv.DictReader(csvfile, delimiter=',')
                for row in employeeReader:
                    sa = 0.0
                    su = 0.0
                    sched = row.get('Schedule')
                    if sched=='9-80A' or sched=='9-80B':
                        mo = 9.0
                        tu = 9.0
                        we = 9.0
                        th = 9.0
                        fr = 4.0
                    elif sched=='4-10':
                        mo = 10.0
                        tu = 10.0
                        we = 10.0
                        th = 10.0
                        fr = 0.0
                    elif sched=='StdWW':
                        mo = 8.0
                        tu = 8.0
                        we = 8.0
                        th = 8.0
                        fr = 8.0
                    else:
                        hrs = float(row.get('Expected'))/5.0
                        mo = hrs
                        tu = hrs
                        we = hrs
                        th = hrs
                        fr = hrs
                        
                    cmd = 'INSERT INTO emps (id, name, schedule, custom, expected, sectionHead, approvedForModTime, email, phone, sa, su, mo, tu, we, th, fr) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'
                    cur.execute(cmd, (row.get('ID'), row.get('Name'), sched, 0, row.get('Expected'), row.get('SectionHead'), 0, row.get('Email'), row.get('Phone'), sa, su, mo, tu, we, th, fr) )
  
                self.conn.commit()
            csvfile.close()
            
        except Error as e:
            print(e)

    def closeConnection(self):
        if self.conn != None:
            self.conn.close()

def main():
    
    inp = TC_Inputs()
    inp.parseInput()
    
    '''
    db = Model()
    db.createConnection()
    if db.conn != None:
        db.checkTable()
        db.dumpEmps()
        
    db.closeConnection()
    '''
    
if __name__=='__main__':
    main()
    