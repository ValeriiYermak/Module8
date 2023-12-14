from datetime import datetime


def get_str_date(date):
    
    d = datetime.fromisoformat(date.replace('Z', '+00:00'))
    sort = datetime.strftime(d, "%A %d %B %Y")
    
    return sort

get_str_date('2021-05-27 17:08:34.149Z')
    

# Напишіть функцію get_str_date(date), яка перетворюватиме дату з бази даних у 
# форматі ISO '2021-05-27 17:08:34.149Z' у вигляді наступного рядка 
# 'Thursday 27 May 2021' - день тижня, число, місяць та рік. 
# Перетворене значення функція повертає під час виклику.}