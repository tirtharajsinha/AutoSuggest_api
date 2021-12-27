import requests
import xml.etree.ElementTree as ET
import json


def find_sugg(query, w="all"):
    data = []
    count = 0
    myroot = fetch_suggestions(query)
    for root in myroot:
        for x in root:
            if w != "all":
                if count >= w:
                    break
            data.append(x.attrib["data"])
            count += 1
    return data


def fetch_suggestions(query):
    x = requests.get("https://www.google.com/complete/search?q={}".format(query))
    data = x.text
    myroot = ET.fromstring(data)
    return myroot


def fetch_sugg(query, count="all"):
    x = requests.get(
        "https://www.google.com/complete/search?client=hp&sugexp=msedr&gs_rn=62&gs_ri=hp&cp=1&gs_id=9c&xhr=t&q={}".format(
            query
        )
    )
    data = x.text
    data = json.loads(data)
    all = []
    for d in data[1]:
        all.append(d[0])
    if count == "all":
        return all
    else:
        try:
            return all[:count]
        except:
            return all
