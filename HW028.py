from datetime import date
import calendar

def get_days_in_month(month, year):
    
    num_days = calendar.monthrange(year, month)[1]
    
    print("Number of days is",num_days)  
get_days_in_month(2, 2025)