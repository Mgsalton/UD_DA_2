import sys
import time
import datetime
import numpy as np
import pandas as pd

from datetime import date
 
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

'''
Imports various modules that are used by functions in the program.

     sys      -  used in the getcity(), getmonth(), and getday() functions
                 to allow for program termination using sys.exit().
     time     -  used in the user_stats() function to calculate age from
                 a given year.
     datetime -  see above.
     
     pandas   -  used to create a configurable dataframe from imported 
                 CSV documents.
                 
 from datetime import date - used to calculate age in the user_stats()
                             function by determining today's date.
                             
 CITY_DATA = {dictionary}  - imports data from external files.
'''

def intro():
     '''
     This is the first function called by main() below and presents an introduction
     to the user. It takes no arguments and returns nothing.
     '''
     # Font courtesy of:
     # http://patorjk.com/software/taag/#p=display&h=1&v=2&f=Graceful&t=Bike%20Sharing
     # Font type: Graceful
     print("""  
     **************************************************************************
     *     ____  __  __ _  ____    ____  _  _   __   ____  __  __ _   ___     *
     *    (  _ \(  )(  / )(  __)  / ___)/ )( \ / _\ (  _ \(  )(  ( \ / __)    *
     *     ) _ ( )(  )  (  ) _)   \___ \) __ (/    \ )   / )( /    /( (_ \    *
     *    (____/(__)(__\_)(____)  (____/\_)(_/\_/\_/(__\_)(__)\_)__) \___/    *
     *                           _  _  ____   __                              *
     *                          / )( \/ ___) / _\                             *
     *                          ) \/ (\___ \/    \                            *
     *                          \____/(____/\_/\_/                            *
     *                                                                        *
     *          Welcome to this bike sharing program! Your choices are:       *
     *                                                                        *
     *                 Chicago | Washington | New York City                   *
     **************************************************************************""")
        
def getcity():
    
    '''
    getcity() is the second function called by main() and is designed 
    to take input from the user. It is in this function that the user decides
    which of the three cities--Chicago, Washington, or New York City--they'd like
    to choose from.
    
    Args:
        (str) city - the name of the city the user wants to analyze.
        (str) selection - a Y/N choice that determines whether the program ends.
        
    Returns:
         city - the name of the city the user wants to analyze.
    '''
    
    # A While loop that continues until a valid city is selected, 
    # or the program is terminated by the user.
    # The .lower() function ensures that user entry is entered in lower case,
    # which helps with logic later on (chicago is preferable to ChiCaGo etc.).
    
    while True:
        city = str(input("\nPlease enter your city from the choices above, or press Q to quit: \n")).lower()
    
    # If the city entered by the user matches the list below, return the city name back to main().
    
        if city in ["chicago", "washington", "nyc",
                    "new york", "new york city"]:
            return city
            break
    
    # To terminate the program, the user can also press Q to intiate a sys.exit() shutdown.
    # The pass argument will skip the logic if anything aside from [y, yes] is input.
    
        elif city in ["q", "quit"]:
            selection = str(input("\nAre you sure? Y/N: ")).lower()
            if selection in ["y", "yes"]:
                sys.exit("Ending program...")
            else:
                pass
     
     # If the contents of the list--or Q(uit)--aren't entered, present this message and loop back.           
        else:
            print("\nPlease input Chicago, Washington, or New York City.")

def getmonth():
    '''
    getmonth() is the third function called by main() and is designed to retrieve the
    months ranging from January-June (as per the CSV) that the user wants to analyze.
    It also includes an 'All' catch-all filter that can be used with a Pandas dataframe later.
    
    Args:
        (str) month - the name of the month(s) the user wants to analyze.
        (str) selection - a Y/N choice that determines whether the program ends.
        
    Returns:
        month - the name of the month(s) the user wants to analyze.
    '''
    
    # The same functionality as the getcity() function above.
    
    while True:
        print("\n***********************************************************************")
        print("\nMonth Selection: January | February | March | April | May | June | All")
        print("\n***********************************************************************")
        month = str(input("\nPlease enter a month from the list above, or press Q to quit: \n")).lower()

        if month in ["january", "february", "march",
                     "april", "may", "june"]:
                     return month
                     break
        
        elif month == "all":
            return month
            break

        elif month in ["q", "quit"]:
            selection = str(input("\nAre you sure? Y/N: ")).lower()
            if selection in ["y", "yes"]:
                sys.exit("Ending program...")
            else:
                pass
                
        else:
            print("\nPlease enter a valid month between January and June.")

def getday():
    
    '''
    getday() is the fourth function called by main() and is designed to retrieve the
    day(s) the user wants to analyze.
    
    Args:
        (str) i - this variable is where user input is stored temporarily. 
        (str) day - this variable contains the actual day after logic has been applied.
        (str) selection - a Y/N choice that determines whether the program ends.
    
    Returns:
        day - the name of the day(s) the user wants to analyze.
    '''
    
    # This While loop utilizes eception handling to catch inputs that aren't strings.
    # It was very useful in early versions of the code that took user inputs
    # as an int before converting them into a string. 
    while True:
       try:
           print("\n***********************************************************************")
           print("\nDay Selection: Mon | Tue | Wed | Thur | Fri | Sat | Sun | All")
           print("\n***********************************************************************")
           i = str(input("\nPlease enter a day from the list above, or press Q to quit: \n")).lower()
    
    # The ValueError exception pertains to inputs that don't match the variable type(string in this case)
       except ValueError:
           print("\n!! Please enter a day between Mon-Sun.")

    # If the shortened user input (like mon or tue) is detected, it will be converted to the
    # full name (monday or tuesday). This was a choice geared towards the user; entering sat is
    # far quicker than saturday (etc.) when entering text.
       else:      
           if i == "mon":
               day = "monday"
               return day
               break
           elif i == "tue":
               day = "tuesday"
               return day
               break
           elif i == "wed":
               day = "wednesday"
               return day
               break
           elif i == "thur":
               day = "thursday"
               return day
               break
           elif i == "fri":
               day = "friday"
               return day
               break
           elif i == "sat":
               day = "saturday"
               return day
               break
           elif i == "sun":
               day = "sunday"
               return day
               break
           elif i == "all":
               day = "all"
               return day
               break
           elif i in ["q", "quit"]:
               selection = str(input("\nAre you sure? Y/N: ")).lower()
               if selection in ["y", "yes"]:
                   sys.exit("Ending program...")
               else:
                   pass
           else:
               print("\n!! Please enter a number between 1 and 7.") 
  
def load_df(city, month, day):

    '''
    The load_df() function takes the returned variables from the previous three functions
    (city, month, and day) and uses the Pandas module to create a customized dataframe so 
    that large amounts of data can be analyzed quickly.
    
    Args:
        (str) city - selects the CSV file to be imported: chicago, washington, or new york city.
        (str) month - imports the user's choice of month from the getmonth() function
        (str) day - imports the user's choice of day from the getmonth() function
        
    Returns:
        df - this variable contains the dataframe that is passed back to main() for analysis.
    '''
    
    # Loads the selected data file into a dataframe. If the chosen city is Chicago, the program
    # will load chicago.csv etc.
    df = pd.read_csv(CITY_DATA[city])

    # Converts the Start Time column to datetime.
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extracts month and day of week from Start Time to create new columns.
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

    # Filters by month if applicable; if it's not set to 'all' then this will execute
    if month != 'all':
        # Use the index of the months list to get the corresponding int.
        months = ['january', 'february', 'march',
                 'april', 'may', 'june']
        month = months.index(month) + 1

        # Filters by month to create the new dataframe.
        df = df[df['month'] == month]

    # Filter by day of week if applicable; if it's not set to 'all' then this will execute
    if day != 'all':
        # Filter by day of week to create the new dataframe.
        df = df[df['day'] == day.title()]

    return df
 
def time_stats(df):
    '''
    time_stats is called from main() and takes the dataframe (df) as an argument; it is
    designed to print the most popular month, day, and hour from the values
    contained in the dataframe.
    
    Args:
        (list) lib_month - contains a string array for months of the year.
        (list) lib_suffix - contains a string array of suffixes (nd, st etc.)
        (str)append_day - prints a suffix to make the output more presentable.
        (str)append_time - prints a defined AM or PM suffix for the time value.
        (flt)p_hour - calculates the mode of the hour column, and stores it
        (flt)p_month - calculates the mode of the month column, and stores it
        (flt)p_day - calculates the mode of the day column, and stores it
        
    Returns:
        None.
    '''
    # Converts the data contained in the 'Start Time' column in the dataframe
    # to a different format.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
     
     
    df['hour'] = df['Start Time'].dt.hour     
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
     
    # Each variable stores the most frequent value from each
    # respective column, and selects the first position from each.
    p_hour = df['hour'].mode()[0]      
    p_month = df['month'].mode()[0]    
    p_day = df['day'].mode()[0]
     
    # The if statement below detects the returned month by number (1-6)
    # and then converts these numbers to names using the logic below.
     
    # Month names are stored in the lib_month library, and accessed by
    # accessing their location via the [0-5] statement.
    lib_month = ["January", "February", "March",\
                   "April", "May", "June"]
     
    if p_month == 1:
        p_month = lib_month[0]
         
    elif p_month == 2:
        p_month = lib_month[1]
         
    elif p_month == 3:
        p_month = lib_month[2]
         
    elif p_month == 4:
        p_month = lib_month[3]
         
    elif p_month == 5:
        p_month = lib_month[4]
             
    elif p_month == 6:
        p_month = lib_month[5]
         
    # The lib_suffix library contains strings that are accessed and printed
    # alongside output as long as they fulfill the logic conditions below.
    lib_suffix = ["AM", "PM", "nd", "rd", "th", "st"]
             
    if (p_day == 1 or p_day == 21 or p_day == 31):
        append_day = lib_suffix[5]
             
    elif (p_day == 2 or p_day == 22):
        append_day = lib_suffix[2]
             
    elif (p_day == 3 or p_day == 23):
        append_day = lib_suffix[3]
             
    else:
        append_day = lib_suffix[4]
     
    # To make the output slightly more presentable, the following logic
    # was applied to append an AM or PM to the returned time based on
    # whether it was after, equal to, or before 12.
    if p_hour >= 12:
        append_time = lib_suffix[1]
    elif p_hour < 12:
        append_time = lib_suffix[0]
     
    # The results are printed here to avoid congesting the main() function.
    print("\n***********************************************************************")
    print("\nMonth, day, and time stats")
    print("\n***********************************************************************")
    print("\nThe most popular month was:",p_month)
    print("\nThe most popular day was the:", p_day,append_day)
    print("\nThe most popular time was:", p_hour,append_time)
     

def station_stats(df):
    
    '''
    This function takes the dataframe as an argument and analyzes the columns
    relating to start stations, end stations, the total number of bike users per station,
    and the amount of times stations were frequented by users.
    
    Args:
        start_counts - holds the top 10 most frequented start stations.
        popular_start - holds the most used start station overall.
        end_counts - holds the top 10 most frequented end stations.
        popular_end - holds the most used end station overall.
        frequency - outputs the top 20 start-to-end station list.
        
    Returns:
        None.    
    '''
    
    # value_counts() takes the total number of people at each start station,
    # while [:10] outputs the top 10 stations based on these values.
    start_counts = df['Start Station'].value_counts()[:10]
    
    # mode() finds the most frequently occuring start station and outputs it to 
    # the popular_start variable.
    popular_start = df['Start Station'].mode()[0]
    
    # The following lines do the same for the destination (end) stations.
    end_counts = df['End Station'].value_counts()[:10]
    popular_end = df['End Station'].mode()[0]
    
    # The frequency variable groups the start and end station columns, finds the
    # the maximum values between each, then sorts the top 20 outputs in descending order.
    
    frequency = df.groupby(['Start Station', 'End Station']).size()\
    .reset_index(name='Count')\
    .sort_values(by='Count', ascending=False).head(20)
    
    # As above, so below... This avoids congestion of main().
    print("\n***********************************************************************")
    print("\nStation usage stats")
    print("\n***********************************************************************")
    print("\nThe most popular starting station was:\n\n",popular_start)
    print("\nThe most popular ending station:\n\n",popular_end)
    print("\nUsers at each start station:\n\n",start_counts)
    print("\nUsers at each end station:\n\n",end_counts)
    print("\nMost frequently used station combinations:\n\n",frequency)

def user_stats(df, city):
    
    '''
    This function takes the dataframe (df) along with the city varaible as arguments,
    and prints information pertaining to the users of the bike share system.
    
    Args:
        usr_type - holds the total number of users and subscribers.
        usr_gender - holds the total number of males and females.
        today - used to calculate age; holds today's date
        oldest_year - holds the maximum birth year from the dataframe.
        youngest_year - holds the minimum birth year from the dataframe.
        average_year - holds the most frequent birth year from the dataframe.
        (flt)youngest_usr - result of a calculation for the youngest user.
        (flt)oldest_usr - result of a calculation for the oldest user.
        (flt)average_usr - result of a calculation for the average age.
    
    Returns:
        None.
    '''
    # Since Washington does not contain gender or age data in the CSV, this IF statement
    # was used to filter out Washington for the gender and age calculations.
    if city in ["chicago", "new york city"]:
        usr_type = df['User Type'].value_counts()
        usr_gender = df['Gender'].value_counts()
        
        # A variety of calculations to determine min, max, and average ages.
        today = date.today()
        oldest_year = df['Birth Year'].max()
        youngest_year = df['Birth Year'].min()
        average_year = df['Birth Year'].mode()
        youngest_usr = (today.year - oldest_year)
        oldest_usr = (today.year - youngest_year) 
        average_usr = (today.year - average_year)

        print("\n***********************************************************************")
        print("\nUser stats")
        print("\n***********************************************************************")
        print("\nUser type:\n\n",usr_type)
        print("\nUser gender:\n\n",usr_gender)
        print("\nAverage age:\n\n",average_usr)
        print("\nYoungest recorded user:\n\n",youngest_usr)
        print("\nOldest recorded user:\n\n",oldest_usr)
    
    # If washington is selected, this code runs instead--offering a subset of the user stats.
    elif city in ["washington"]:
       
        usr_type = df['User Type'].value_counts()
        print("\n***********************************************************************")
        print("\nUser stats **Warning - Washington has no gender or age data**")
        print("\n***********************************************************************")
        print("\nUser type:\n\n",usr_type)
    

def duration_stats(df):
    '''
    This function prints the total amount of time that users travelled from the start station,
    along with average times for good measure.
    
    Args:
        total_time - holds the total trip duration from each start station.
        average_time - holds the average trip duration from each start station.
        
    Returns:
        None.
    '''
    # Calculates the total trip duration by station, and sorts by descending values.
    total_time= df.groupby('Start Station')['Trip Duration'].sum()\
    .reset_index(name='Total Time')\
    .sort_values(by='Total Time', ascending=False)
    
    # Calculates the average trip duration by station, and sorts by descending values.
    average_time = df.groupby('Start Station',)['Trip Duration'].mean()\
    .reset_index(name='Average Time')\
    .sort_values(by='Average Time', ascending=False)
    
    print("\n***********************************************************************")
    print("\nDuration stats")
    print("\n***********************************************************************")
    print("\nTotal time per station:\n\n ", total_time)
    print("\nAverage time per station:\n\n ", average_time)
    
    
def main(): 
    '''
    The starting point of the program, encased in a While loop to ensure the code repeats
    itself until the user decides to terminate it. Calls the functions required to obtain
    a choice of city, month, and day from the user alongside a cascade of functions to 
    analyze the bike share data.
    
    Args:
        (str)city - holds the value of the city from the getcity() function
        (str)month - holds the value of the month from the getmonth() function
        (str)day - holds the value of the day from the getday() function
        (str)restart - if set to no at the end, the program will terminate.
   
    Returns:
        None.
    '''
    # Code will continue to loop until the while loop is broken.
    while True:
        
        # Calls the intro() function to present a welcome screen.
        intro()
        
        # Calls the getcity() function to retrieve user input.
        city = getcity()
        
        # Converts 'nyc' or 'new york' to new york city
        if city in ["nyc", "new york"]:
            city = "new york city"
        
        # If no action is required, pass.
        else:
            pass
    
        print("\nYour selected city is: {}.".format(city))
        
        # Calls the getmonth() function to retrieve user input.
        month = getmonth()
    
        print("\nYour selected month is: {}.".format(month))
    
        # Calls the getday() function to retrieve user input.
        day = getday()
    
        # Prints a result of the user's choices.
        print("\n***********************************************************************")
        print("\nYour final selection is: ")
        print("\nCity: {} | Month: {} | Day: {}".format(city, month, day))
        print("\n***********************************************************************")
        
        print("\nCalculating stats...")
    
        # Each function related to the data analysis is run in sequence.
        df = load_df(city, month, day)
    
        time_stats(df)
        
        station_stats(df)
        
        user_stats(df, city)

        duration_stats(df)
    
        #This message will run at the end of each session, and can be used to terminate the program.
        print("\n***********************************************************************")
        restart = str(input("\nWould you like to restart the program? Y/N:\n")).lower()
        if restart in ["n", "no"]:
            print("\nYou'll be back...")
            break
        else:
            print("\n\n\n")
            pass

# A requisite declaration to ensure that this is the running program.        
if __name__ == "__main__":
    main()