from flask import Flask, render_template
import sqlite3
import webbrowser

conn = sqlite3.connect('Add-recipe.db')
c = conn.cursor()
print("Connected to database successfilly")

c.execute('''CREATE TABLE Recipe (
            R_id INT AUTO_INCREMENT PRIMARY KEY,
            RName TEXT,
            Ingredients TEXT,
            Instructions TEXT
            )
           ''')
print("Table created successfully");


conn.close()