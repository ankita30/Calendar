"""User friendly calendar to enter, edit or delete an event in the calendar"""

#Import strfttime: forentering current time
#Import datetime: validate any input date
from time import sleep, strftime
from datetime import datetime

name = "Ankita"
calendar = {}

#function to validate entered date
def validate_date(d):
    try:
        datetime.strptime(d, '%m/%d/%Y')
        return True
    except ValueError:
        return False
      
#welcome function       
def welcome():
  print "Welcome %s \n Calendar opening..." % name
  sleep(1)
  print "Today is %s \n Current time: %s" % (strftime("%A %B %d, %Y"), strftime("%H:%M:%S"))
  sleep(1)
  print "What would you like to do?"

#Event function to add, update, view or delete an event
def start_calendar():
  welcome()
  start=True
  while start:
    #Enter option:
    user_choice = raw_input("Please enter A to add, U to update, V to view, D to Delete, X to exit")
    user_choice = user_choice.upper()
    
    #Option to view the Calendar:
    if user_choice == 'V':
      if len(calendar.keys()) == 0:
        print "Calendar is empty!"
      else:
        print calendar
    
    #Option to update an event
    elif user_choice == 'U':
      date= raw_input("What date you want to update (MM/DD/YYYY): ")
      if validate_date(date):
        update = raw_input("Enter the update: ")
      	calendar[date] = update
      	print "The update was succssfull!"
      	print calendar
      else:
        print "Entered date is invalid!"
        continue
    
    #Option to add an event:
    elif user_choice == 'A':
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if not(validate_date(date)) or int(date[6:]) < int(strftime("%Y")):
        print "Entered date is invalid!"
        try_again = raw_input("Try Again? Y for Yes. N for No")
        try_again = try_again.upper()
        if try_again == 'Y':
          continue
        else:
          start = False
          break
      event = raw_input("Enter event: ")
      calendar[date] = event
      print "Event was successfully added!"
      print calendar
    
    #Option to delete an event:
    elif user_choice == 'D':
      if len(calendar.keys()) == 0:
        print "Calendar is empty!"
      else:
        event = raw_input("What event would you like to delete: ")
        event_validate=True
        for date in calendar.keys():
          if calendar[date] == event:
            del calendar[date]
            print "Event was successfully deleted!"
            print calendar
            event_validate = False
        if event_validate == True:
          print "Incorrect event was specified!"
    
    #Option to exit:
    elif user_choice == 'X':
      start = False
    else:
      print "Invalid command"
      continue

#Calendar function to build the calendar!
start_calendar()


