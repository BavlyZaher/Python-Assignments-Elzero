#1
def get_score(**get):
    for name,progress in get.items():
        print(f"{name} => {progress}")
get_score(Math=90, Science=80, Language=70)
get_score(Logic=70, Problems=60)

#2
def get_people_scores(name="Unknown",**dict):
    if name=="Unknown":
        for name1,progress in dict.items():
            print(f"{name1} => {progress}")
    elif len(dict)== 0:
      print(f"Hello {name} You Have No Scores To Show")
    else:
        print(f"Hello {name} This Is Your Score Table:")
        for name1,progress in dict.items():
            print(f"{name1} => {progress}")
get_people_scores("Osama", Math=90, Science=80, Language=70)
get_people_scores("Mahmoud", Logic=70, Problems=60)
get_people_scores(Logic=70, Problems=60)
get_people_scores("Ahmed")

#3
scores_list = {
    "Math": "90",
    "Science": "80",
    "Language": "70"
}
def get_the_scores(name="Unknown", **scores):
    if name=="Unknown":
        for name1,progress in scores.items():
            print(f"{name1} => {progress}")
    elif len(scores)== 0:
        print(f"Hello {name} You Have No Scores To Show")
    else:
        print(f"Hello {name} This Is Your Score Table:")
        for name1,progress in scores.items():
            print(f"{name1} => {progress}")
get_the_scores("Osama", **scores_list)
get_the_scores("Osama")
get_the_scores(**scores_list)

