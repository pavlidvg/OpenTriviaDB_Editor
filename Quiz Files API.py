import time

import requests
import json

#get the API call
res = requests.get("https://opentdb.com/api_category.php")
category_list = res.json()

categories = len(category_list["trivia_categories"])#number of categories

#declarations, dont know if needed :(
category_id = ""
numquestions = 0
for i in range(categories):
    category_id = str(category_list["trivia_categories"][i]["id"])
    res = requests.get("https://opentdb.com/api_count.php?category="+category_id)
    res = res.json()
    numquestions = res["category_question_count"]["total_question_count"]

    if numquestions > 50:
        res = requests.get("https://opentdb.com/api.php?amount=50&category="+category_id)
        res = res.json()

    else:
        print("went here for id:"+str(category_id))
        res = requests.get("https://opentdb.com/api.php?amount="+str(numquestions)+"&category=" + category_id)
        res = res.json()

    fix_name = str(category_list["trivia_categories"][i]["name"]).replace(":","_") #removes the ":" because windows doesnt allow it in file names
    with open(str(category_id)+"-"+fix_name+'.oq', 'w') as json_out:
        json.dump(res, json_out, indent=2)
        print("Created category:"+str(category_id))
    time.sleep(1)








