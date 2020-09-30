import requests
from bs4 import BeautifulSoup
import json
import sys 
import os



def data2_collector(inner_url):
    inner_soup = BeautifulSoup(requests.get(inner_url).content, "html.parser")
    # ---------------------------------------------names-------------------
    div_title_bar = inner_soup.find('div', id='titlebar')
    title_chi = div_title_bar.find('h1').text
    title_eng = div_title_bar.find('h2').text
    # ------------------------------------------------------end_names----------------------
    # -----------------------------------min max------------------------------------------
    rank_div = inner_soup.find_all('div', class_='ranktable_div')
    Max = rank_div[0].find('p').getText().rsplit("(", 1)[1].split("-")[1].replace(")", "")
    Min = rank_div[-1].find('p').getText().rsplit("(", 1)[1].split("-")[0]
    # --------------------------------------edn min max-------------------------------------
    data_2["position"].append({
        "id": ID,
        "max": Max,
        "min": Min,
        "chinese_name": title_chi,
        "english_name": title_eng
    })
print("bug found here")

# ------------------------------------------------------

def data3_collector(inner_url):
    inner_soup = BeautifulSoup(requests.get(inner_url).content, "html.parser")
    rank_div = inner_soup.find_all('div', class_='ranktable_div')
    for y in rank_div:
        name_short = y.find('h3').getText().split(' ', 1)
        point_salary = y.find('p').getText().rsplit("(", 1)
        data_3["all"].append({
            "id": ID,
            "max": point_salary[1].split("-")[1].replace(")", ""),
            "min": point_salary[1].split("-")[0],
            "chinese_name": name_short[0],
            "english_name": name_short[1].replace("(", "").replace(")", ""),
            "salary_desc": point_salary[0]
        })


# --------------------------------------------------------------------------------------
website_link="https://csradar.com"
Main_page_link="https://csradar.com/grade"
Main_soup=BeautifulSoup(requests.get(Main_page_link).content,"html.parser")
List_of_job=Main_soup.find_all('div',class_="categories-group")[1]
List_of_inLink=[]
for x in List_of_job.find_all('li'):
    # print(x.find('a').text+"----")
    List_of_inLink.append(website_link+x.find('a')['href'])
# -----------------------------------------------------------------------------------------

# ---------------------------declraing 2 json
data_2={"position":[]}
data_3={"all":[]}
# --------------------------------------------------end json
for x in range(len(List_of_inLink)):
    ID=List_of_inLink[x].rsplit("/",1)[1].lower()
    print(ID+"------"+str(len(List_of_inLink)-x))
    try:
        data2_collector(List_of_inLink[x])
    except:
        print("something went wrong in data2 "+str(x)+" "+List_of_inLink[x])
    try:
        data3_collector(List_of_inLink[x])
    except:
        print("something went wrong in data 3 col "+str(x)+" "+List_of_inLink[x])


with open("data_2.json",'w') as vishu:
    json.dump(data_2,vishu)
with open("data_3.json",'w') as vishu:
    json.dump(data_3,vishu)
