# coding : utf-8 

import csv
import json
import requests 

fichier = "lobbyclimat.csv"

url = "http://jhroy.ca/uqam/lobby.json"

entete = {
    "User-Agent":"Eliane Gosselin - cours de journalisme",
    "From":"gosselin.eliane@uqam.ca"
}

req = requests.get(url,headers=entete)

# print(req)

# int("objet")

# vraiobjet = int(objet)


# n = 0

# nombres = list(range(0,71998))

# for nb in nombres:
#     n += 1
#     infos = []

if req.status_code != 200:
    print("Ça ne fonctionne pas!")
lobbies = req.json()
    # lobbyfr = req.json()
    # # print(lobbyfr["fr_client_org_corp_nm"])
    # print(lobbyfr[""])
    # else:
        # print(lobbies["registre"][0][0]["comlog_id"])
        # print(lobbies["registre"][0][0]["fr_client_org_corp_nm"])
        # print(lobbies["registre"][0][0]["en_client_org_corp_nm"])
        # print(lobbies["registre"][0][0]["client_org_corp_num"])
        # print(lobbies["registre"][0][0]["date_comm"])
        # print(lobbies["registre"][0][1][1]["objet"])
        # print(lobbies["registre"][0][1][1]["objet_autre"])
        # print(lobbies["registre"][0][2][0]["institution"])
        # print(len(lobbies["registre"]))
for chaque in lobbies["registre"]: 
    infos = []
    nomfr = chaque[0]["fr_client_org_corp_nm"]
    nomen = chaque[0]["en_client_org_corp_nm"]
    num = chaque[0]["client_org_corp_num"]
    date = chaque[0]["date_comm"]
    objet = chaque [1][0]["objet"]
    objetautre = chaque [1][0]["objet_autre"]
    institutionA = chaque [2][0]["institution"]

    infos.append(nomfr)
    infos.append(nomen)
    infos.append(num)
    infos.append(date)
    infos.append(objet)
    infos.append(objetautre)
    infos.append(institutionA)

    # print(infos)
    if "limat" in objet:
        infosvrai = []
        infosvrai.append(nomfr)
        infosvrai.append(nomen)
        infosvrai.append(num)
        infosvrai.append(date)
        infosvrai.append(objet)
        infosvrai.append(objetautre)
        infosvrai.append(institutionA)
        
        print(infosvrai)
        # print("~"*71998)
        dead = open(fichier,"a")
        obies = csv.writer(dead)
        obies.writerow(infosvrai)

    

    

        # elif "limat" in objetautre:
        #     infosvrai2 = []
        #     infosvrai2.append(nomfr)
        #     infosvrai2.append(nomen)
        #     infosvrai2.append(num)
        #     infosvrai2.append(date)
        #     infosvrai2.append(objet)
        #     infosvrai2.append(objetautre)
        #     infosvrai2.append(institutionA)

        #     print(infosvrai2)


    

    # x = [lobbies]
    # y = list(range(0,72000))
    # x.extend(y)
    # print(x) 


# print(registre)

