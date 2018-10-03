import datetime
#
# jaar = input("In welk jaar ben je geboren? ")
# maand = input("In welke maand ben je geboren? ")
# dag = input("Op welke dag ben je geboren? ")
#
# date1 = str(maand)+"/"+str(dag)+"/"+str(jaar)
# vandaag = datetime.date.today()
# # print(vandaag - date1)
# print(vandaag)
#
# print("Dan ben je dus geboren op: {}".format(date1))
# print("Je verjaardag is dus over {} dagen.")

# day, month, year = eval(input("Please enter day, month, year numbers: "))

def print_header():
    print('----------------------')
    print('    CALCULATE DAYS')
    print('----------------------')
    print()

def get_birthday_from_user():
    print("Wanneer ben je geboren? ")
    year = int(input("Year [YYYY]: "))
    month = int(input("Month [MM]: "))
    day = int(input("Dag [DD]: "))
    birthday = datetime.date(year, month, day)
    return birthday

def compute_days_between_dates():
    pass

def print_birthday_information():
    pass

def main():
    print_header()
    bday = get_birthday_from_user()
    now = None
    number_of_days = compute_days_between_dates()
    print_birthday_information()


main()
