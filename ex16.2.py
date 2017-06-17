from datetime import date

def age():
    """Calculates age from given birthday.
    """
    bday = []
    s = input("Enter birthday(yyyy, mm, dd): \n")
    t = s.split(",")
    for i in t:
        bday.append(int(i))
          
    bday = date(*bday)
    d = next_bday(bday) 
    year = (date.today() - bday).days // 365
    print("{}years".format(year))
    print("days, hours, minutes, seconds to your next birthday")
    print(d)
    


def next_bday(birthday):
    """Calculates time to next birthday.
    
    Returns the number of days, hours, minutes, seconds to next birthday.
    
    birthday: datetime date object
    """
    today = date.today()
    
    if birthday.month < today.month:
        birthday = birthday.replace(year=today.year+1)
    else:
        birthday = birthday.replace(year=today.year)
    
    return birthday-today
    

def current_date():
    """Prints the current date and day of the week.
    """
    today = date.today()    
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    index = today.weekday()
    print(weekdays[index], today)
    
    
if __name__ == "__main__":
    current_date()
    age()