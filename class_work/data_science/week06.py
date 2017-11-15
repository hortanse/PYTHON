#!/usr/bin/env python
import sqlite3
import xlrd

conn = sqlite3.connect('contracts_2015.db')
curs = conn.cursor()

curs.execute("""
CREATE TABLE contractors (
id integer primary key autoincrement,
global_vendor_name text)
""")

curs.execute("""
CREATE TABLE contracts (
id integer primary key autoincrement,
department text,
actions integer,
dollars float,
contractor_id)
""")

path = "Top_100_Contractors_Report_Fiscal_Year_2015.xlt"
"""
Open and read an Excel fisle
"""
book = xlrd.open_workbook(path)
names = set()

"""
put all of the global_vendor name into a set names
"""
sheet_names = book.sheet_names()
for department in sheet_names:
    sheet = book.sheet_by_name(department)
    for row in range(sheet.nrows - 1):
        global_vendor_name = sheet.cell(row+1, 0).value
        names.add(global_vendor_name)

"""
populate contractors table
and sore the global_vendor_name into a dictionary
vendor_name
"""
vendor_names = dict()
for i, name in enumerate(names):
    vendor_names[name] = i
    contractor_name = name
    qry = '''INSERT INTO contractors(global_vendor_name) VALUES (?)'''
    curs.execute(qry, (contractor_name,))

"""
populate contracts table
"""
for department in sheet_names:
    sheet = book.sheet_by_name(department)
    for row in range(sheet.nrows -1):
        row1 = row + 1
        global_vendor_name = sheet.cell(row1, 0).value
        actions = sheet.cell(row1, 1).value
        dollars = sheet.cell(row1, 2).value
        qry = '''INSERT INTO contracts(department, actions,
            dollars, contractor_id)
            VALUES (?,?,?,?)'''
        curs.execute(qry, (department, actions, dollars,
			   vendor_names[global_vendor_name]))

conn.commit()
curs.close()
conn.close()