import os 
import csv
import json
#from utils.helpers import get_file_path
from pathlib import Path


def get_login_csv(csv_file="data_login.csv"):

    #csv_file = get_file_path(csv_file, "data")
    
    current_file = os.path.dirname(__file__) #el archivo donde estoy
    csv_file = os.path.join(current_file,"..","data","archivos",csv_file)
    #../Data/data_login.csv=> rel
    csv_file = os.path.abspath(csv_file)


    casos = []

    with open(csv_file, newline="") as h:
        read = csv.DictReader(h)

        for i in read:
            username = i["username"]
            password = i["password"]
            login_example = i["login_example"].lower() == "true"
            casos.append((username,password,login_example))

    return casos

def get_login_json(json_file="data_login.json"):
    current_file = os.path.dirname(__file__)
    json_file = os.path.join(current_file,"..","Data",json_file)
    #../Data/data_login.csv > rlativo qe se tien que transfrmar en absoluto
    json_file = os.path.abspath(json_file)

    casos = []

    with open(json_file) as j:
        datos = json.load(j)

        for i in datos:
            username = i["username"]
            password = i["password"]
            login_example = i["login_example"]
            casos.append()

    return casos


