import mysql.connector
import os, requests, sys, csv
from dotenv import load_dotenv

load_dotenv()

headers = {"Authorization": os.getenv("TABBYCAT_TOKEN")}
mydb = mysql.connector.connect(
    host="localhost",
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database="debate")

mycursor = mydb.cursor()   
#venue_id = room["venue"].split("/")[-1]
sql = "select VenueName, zoom_link from Venues where VenueID = %s"
val = ("28",)
mycursor.execute(sql,val)
venue_info = mycursor.fetchone()
print(venue_info)

# sql = "select team from participants where  name = 'independent' "
# mycursor.execute(sql)
# sql = "select name, institution from participants where unique_id = %s"
# val = ("817485",)
# mycursor.execute(sql, val)
# myresult= mycursor.fetchall()
# print("myresult")
# print(myresult)
# print("end")
# for x in myresult:
#     print("Ses")
#     print(x)
