import requests
import os
import discord
from dotenv import load_dotenv
import json
import mysql.connector


load_dotenv()

mydb = mysql.connector.connect(
    host="localhost",
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database="debates")

mycursor = mydb.cursor()

url_part = "https://kutab.herokuapp.com/api/v1/tournaments/bp88team/rounds/1/pairings"

header = {"Authorization": os.getenv("TOKEN") } 
result = requests.get(url_part, headers = header).json()

teamid_list = []
id_list = []
teamdict = {}
adj_dict = {}

result = requests.get(url_part, headers = header).json()

#print(result)

#the code that gives team ids in a venue as a dictionary
i=0
for x in result:

   for y in range(4):
      string = (result[i].get("teams")[y].get("team"))
      teamid_list.append(string.split('/')[-1])
   
   teamdict[x.get('id')] = teamid_list[0:4]
   teamid_list.clear()
   i +=1
#print(teamdict)

#the code that gives personal ids of adjudicators in a venue as a dictionary
j=0
for a in result:
   chair_url = result[j].get("adjudicators").get("chair")
   id_list.append(chair_url.split('/')[-1])
   for b in (result[j].get("adjudicators").get("panellists")):
      id_list.append(b.split('/')[-1])
   for c in (result[j].get("adjudicators").get("trainees")):
      id_list.append(c.split('/')[-1])
   adj_dict[a.get('id')] = id_list[0:len(id_list)]
   id_list.clear()
   j +=1
#print(adj_dict)

#mycursor.execute("SELECT email FROM Participants WHERE id=18")



#for d in adj_dict:
#   for e in range(len(adj_dict[d])):
#      mycursor.execute("SELECT email FROM Participants WHERE id="+adj_dict[d][e]) 
#      result = mycursor.fetchall()
#      print(result)

