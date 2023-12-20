def turn_time24(new_times, new_addtime): # Turn all times inputed into 24 Hour Clock
    am_or_pm = new_times.split() # Splits to remove the :
    orginal_addtime = int(new_addtime.replace(':',''))
    orignal_time = int(am_or_pm[0].replace(':',''))

    if am_or_pm[1] == 'PM': # Checks to see if it is PM and adds 1200 to the time if so
        orignal_time = orignal_time + 1200
    
    final_time = orginal_addtime+orignal_time 
    return(final_time,orginal_addtime) # Sends back the updated orginal time and the add_time in 24 Hour Form

def days_of_week(date,days_to_pass): # Check to see how many days pass in a given week
    week=['sunday','monday','tuesday','wednesday','thursday','friday','saturday'] # Format the Week as a list
    starting_date=date.lower()
    
    if starting_date in week: # Find the current day's index
        current_day = week.index(starting_date) 
    
    new_current_day = current_day+days_to_pass # Set the days to pass with the current day's index

    if new_current_day > 7: # Checks to see if new_current_day is more than 7 days
        new_current_day=new_current_day-7
    if new_current_day == 7: # If new_current_day is 7 it resets the week back to sunday
        new_current_day = 0

    if days_to_pass > 7: # Checks to see the days_to_pass is longer than a week if it is it divides to see how many weeks need to pass
        days_to_weeks=days_to_pass//7
        new_days_to_pass = days_to_pass-(days_to_weeks*7)
        new_current_day=current_day+new_days_to_pass
        if new_current_day > 7: #Does the same logic as before but only if its more than 1 week
            new_current_day=new_current_day-7
        if new_current_day == 7:
            new_current_day = 0

    return(week[new_current_day]) # Returns the day of week after the days have passed




def add_time(base_time,add_moretime,day=None): # Takes time in AM and PM, a time change, and optional day of week, then outputs the new time, days passed, and day of week if needed
    
    hourtime = turn_time24(base_time,add_moretime) # Sends the times and returns them as 24 Hour Clock Time
  
    if hourtime[0] >= 2400: # Checks to see if the added time of base_time and add_moretime is greater than 24 Hours     
        days =  hourtime[0]/2400 # Returns how many days pass 
        
        fixed_time = (int(days)*2400)-hourtime[0] # Returns time remaining after removing Hours for Days passed

        if fixed_time < 0: # Makes sure that the only time returned is always a +Integer
            fixed_time=fixed_time*-1

        if fixed_time <= 2400 and fixed_time >= 2360: # This corrects the amount of days passed if the time goes over 24:00 Hours
            days=days+1
            fixed_time=fixed_time-2360

        
        
        if fixed_time <= 1159: # Checks to see if the newly adjusted time is AM 
            am_pm='AM'
        elif fixed_time >= 1160: # Checks to see if the newly adjusted time is PM and then reduces the 24 Hour Clock by 12 Hours
            am_pm='PM'
            fixed_time=fixed_time-1200

        if len(str(fixed_time)) == 4: # Checks to see if the length of the 24 Clock is 4 Digits to pull the last 2
            end_of_time = int((str(fixed_time))[-2:])
        elif len(str(fixed_time)) == 3: # Checks to see if the length of the 24 Clock is 3 Digits to pull the last 2
            end_of_time = int((str(fixed_time))[-2:])
        else: # WIP If the length is less than 2 return time that needs to be checked 
            end_of_time = fixed_time
            fixed_time=fixed_time+1200

        if end_of_time >= 60: # Checks the last 2 Digits in the time and if it is > 60 add a day and adjust the time to represent an hour increase
            days=days+1
            fixed_time=(100+fixed_time)-60
        if days < 2: # If days only increases by 1
            days_int = '(next day)'
        else: # If days increases by more than 1
            days_int = '('+ str(int(days))+' days later)'
              
        if day != None: # If a day of the week is entered return the correct day of week based off time passed 
            current_day = days_of_week(day,int(days))
        
        if hourtime[1] == 0: # If the time inputed is 0 the output will not change
            fixed_time=hourtime[0]

    else:
        if hourtime[0] <= 1159: # Checks to see if the adjusted time is AM
                am_pm='AM'
                
                if hourtime[1] < 60:
                    end_of_time = hourtime[1]
                elif len(str(hourtime[1])) >= 3:
                    end_of_time = int((str(hourtime[1]))[-2:])

        elif hourtime[0] >= 1160: # Checks to see if the adjusted time is PM
                am_pm='PM' 
                
                if hourtime[0]>=1160 and hourtime[0]<=1200: # Specifically looks if the time goes over 11:59 AM to just 12:00+ PM and corrects the time
                    fixed_time=hourtime[0]-1160
                    fixed_time=fixed_time+1200
                else:
                    fixed_time = hourtime[0]-1200

                if fixed_time < 0: # Makes sure that the only time returned is always a +Integer
                    fixed_time=fixed_time*-1

                if fixed_time < 60:
                    end_of_time = fixed_time

                elif len(str(fixed_time)) >= 3:
                    end_of_time = int((str(fixed_time))[-2:])
                
        if end_of_time >= 60: # Checks the last 2 Digits in the time and if it is > 60 add a day and adjust the time to represent an hour increase
                fixed_time=(100+fixed_time)-60

        days=0
        if day != None: # If there are no days of the week inputed then the days passed doesn't need to update
            current_day = days_of_week(day,int(days))

        if hourtime[1] == 0: # If the time inputed is 0 the output will not change
            fixed_time=hourtime[0]


    
    string_hour_time=str(fixed_time) # Converts the final time into a string

    if len(string_hour_time) == 3: # Formats the string based on how long it is
        formatedtime=string_hour_time[:1]+':'+string_hour_time[1:]
    else:
        formatedtime=string_hour_time[:2]+':'+string_hour_time[2:]

    if day == None and days == 0: # If no days passed and the input isn't requesting days then it formats based on that
        new_time=formatedtime+' '+am_pm
        return(new_time)
    elif day == None and days > 0: # If a day does pass this makes sure it prints how many days passed
        new_time=formatedtime+' ' +am_pm+' ' + days_int
        return(new_time)
    elif day != None and days == 0: # Checks to make sure no days pass and formats based on the current day
        new_time=formatedtime+' '+am_pm+', '+current_day.capitalize()
        return(new_time)
    else: # Checks to see how many days passed and formats based on the current day after the days passed 
        new_time=formatedtime+' ' +am_pm+', '+current_day.capitalize()+' '+days_int
        return(new_time)