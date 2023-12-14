from datetime import datetime, timedelta, date

def get_days_from_today(date):

    date_object = datetime.strptime(date, "%Y-%m-%d")
    ddd = date_object.date()

    currently_date = datetime.now()
    now = currently_date.date()
    timedelt = now - ddd
    t = timedelt.days
    print(t)
    
    return t
    
# date_object = datetime.strptime(new_date, "%Y-%m-%d")
# ddd = date_object.date()

# currently_date = datetime.now()
# now = currently_date.date()
# timedelt = now - ddd

# print (timedelt)
get_days_from_today("2020-10-09")













# print("+++++++++++++++++++++++")
# date_string = '2020-10-09'
# print (date_string,type)
# print("--1--------------------")
# date_str = date_string.split("-")
# print(date_str,type)
# print("---2-------------------")
# date_object = datetime.strptime(date_string, "%Y-%m-%d")
# print(date_object,type)
# print("---3-------------------")
# currently_date = datetime.now()
# print(currently_date,type)
# print("---4-------------------")
# print(currently_date - date_object)
# print("***********************")

# date_string = "21 June, 2018"

# print("date_string =", date_string)
# print("type of date_string =", type(date_string))

# date_object = datetime.strptime(date_string, "%d %B, %Y")

# print("date_object =", date_object)
# print("type of date_object =", type(date_object))
