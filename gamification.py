def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''
    global star_time
    star_time = 0
    
    global star_time_2
    star_time_2 = 0
    
    global star_time_delta
    star_time_delta = 0
    
    global star_time_delta_2 
    star_time_delta_2 = 0
    
    global star_time_3
    star_time_3 = 0

    global star_time_delta_3
    star_time_delta_3 = 0

    global placeholder

    placeholder = None

    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration
    
    global last_finished
    global bored_with_stars
    
    global cur_star, cur_star_activity
    cur_hedons = 0
    cur_health = 0
    
    cur_star = None
    cur_star_activity = None
    
    bored_with_stars = None
    
    last_activity = None
    last_activity_duration = 0
    global previous_activity_1
    previous_activity_1 = None
    global run_duration



    run_duration = 0
    
    global previous_activity_duration_1

    previous_activity_duration_1 = 0
    cur_time = 0
    
    last_finished = -1000

    global tired
    tired = False
    
    global previous_activity_duration
    previous_activity_duration = 0

    global previous_activity
    previous_activity = None

def prev_activity_duration(): #only measures tiredness
    global last_activity
    global last_activity_duration
    global previous_activity
    global previous_activity_duration
    if last_activity == "resting" and (previous_activity != "resting" or previous_activity == None):
        previous_activity = last_activity
        previous_activity_duration = last_activity_duration
        return previous_activity_duration
    elif last_activity == "resting" and previous_activity == "resting":
        previous_activity = last_activity
        previous_activity_duration += last_activity_duration
        return previous_activity_duration
    elif last_activity != "resting":
         previous_activity_duration = 0


def tiredness():

    global tired, placeholder
    global last_activity
    global last_activity_duration
    global previous_activity
    global previous_activity_duration
    global cur_time
    

    prev_activity_duration()
    if previous_activity_duration < 120 and last_activity == "resting":
        tired = True
        return True

    elif (last_activity == "running" or last_activity == "textbooks") and (placeholder != None):
        tired = True
        return True
    else:
        return False


def star_can_be_taken(activity):
    global last_activity
    global bored_with_stars
    global cur_time
    global star_time, star_time_2, star_time_3, star_time_delta, star_time_delta_2, star_time_delta_3, placeholder

    if star_time != 0 and star_time_3 == 0: # if this isn't the first star specifically second
        star_time_2 = cur_time #say star2 offered at 20
        star_time_delta = star_time_2 - star_time
    elif star_time == 0:
        star_time = cur_time

    if star_time_delta != 0 and star_time_2 == cur_time: #just in case
        star_time_3 = cur_time
        star_time_delta_2 = star_time_3 - star_time_2
    if star_time != 0 and star_time_3 != 0:
        star_time_3 = cur_time
        star_time_delta_3 = star_time_3 - star_time_2
    if star_time_delta + star_time_delta_2 + star_time_delta_3 < 120 and star_time_3 != star_time_2: #so that two zeros dont add up
        bored_with_stars = True
        return False
    elif star_time_delta + star_time_delta_2 + star_time_delta_3 >= 120:
        bored_with_stars = False
        star_time_delta = 0
        return True
    elif star_time_3 == star_time_2:
        bored_with_stars = False
        return True

def running_activity(activity, duration):
    global previous_activity_1
    global previous_activity_duration_1
    if activity == "running":
        if previous_activity_1 == "running":
           # previous_activity_duration_1 = duration
            return True
        else:
            previous_activity_1 = "running"
            previous_activity_duration_1 = duration
    if activity != "running":
         previous_activity_1 = None
         previous_activity_duration_1 = 0


def perform_activity(activity, duration):
    global cur_health
    global cur_hedons
    global last_activity_duration
    global last_activity
    global cur_time, cur_star
    global previous_activity, previous_activity_duration, previous_activity_1, previous_activity_duration_1
    global run_duration
    global placeholder
    last_activity = activity
    previous_activity = last_activity
    cur_time += duration
    running_activity(activity, duration)
    if activity == "running":
        if previous_activity_1 == "running":
            run_duration = previous_activity_duration_1 + duration
            if run_duration <= 180: #gains 3 health points every minute up to 180 minutes
                cur_health += (3*duration)
            if run_duration > 180:
                 cur_health += (3*(180-previous_activity_duration_1)) + run_duration - 180  

        if previous_activity != "running":
             run_duration = 0
            
        if (tiredness() == True) and cur_star != "running":
                # loses 2 hedons IF NO STAR and IF tired, loses 2 hedons per minute
                cur_hedons -= 2 * duration 
        if (tiredness() == False) and duration <= 10: #not tired
                cur_hedons += duration*2
        if (tiredness() == False) and duration > 10: #not tired
                cur_hedons += 20 - (duration-10)*2
        
        if (tiredness() == False) and duration > 10 and cur_star == "running": #not tired
                cur_hedons += 50 - (duration-10)*2
                cur_star = None
        if (tiredness() == False) and duration <= 10 and cur_star == "running": #not tired
                cur_hedons += 5 * duration
                cur_star = None
        if (tiredness() == True) and duration <= 10 and cur_star == "running": # tired
                cur_hedons +=  duration
                cur_star = None

        if (tiredness() == True) and duration > 10 and cur_star == "running": # tired
                cur_hedons +=  10 - (2 * (duration - 10))
                cur_star = None

    if activity == "textbooks":
        cur_health += 2 * duration
        if (tiredness() == True) and cur_star != "textbooks": 
                cur_hedons -= 2 * duration
        if (tiredness() == False) and cur_star == "textbooks" and duration > 20: 
                cur_hedons += 40 - duration
                cur_star = None
        if (tiredness() == False) and cur_star == "textbooks" and duration <= 20: 
                cur_hedons += duration
                cur_star = None
 
    if activity == "resting":
        cur_health = cur_health
        cur_hedons = cur_hedons
    
    if activity == ("running" or "textbooks"):
         placeholder = "something"
    else:
        return None
    
def get_cur_hedons():
    global cur_hedons
    return(cur_hedons)

def get_cur_health():
    global cur_health
    return(cur_health)
    
def offer_star(activity):
    global last_activity
    global cur_star
    global cur_star_activity
    if activity == "running" and star_can_be_taken(activity) == True:
        cur_star = "running"
        cur_star_activity = "running"
        return cur_star
    elif activity == "textbooks" and star_can_be_taken(activity) == True:
        cur_star = "textbooks"
        cur_star_activity = "textbooks"
        return cur_star
    else:
        star_can_be_taken(activity)
        return None

def most_fun_activity_minute():
    global cur_star_activity
    global cur_star
    global tired
    #return activity with most hedons in one minute
    # not tired running returns 2 hpm
    # not tired textbook returns 1hpm
    #resting returns 0 always
    #tired turns negative
    # if tired AND no star, return resting
    # if tired and star for something, return the thing
    # if not tired,  and no star return running
    #if not tired, and star for something, return the thing
    if cur_star == "running" and cur_star_activity == "running":
        return "running"
        
    elif cur_star == "textbooks" and cur_star_activity == "textbooks":
        return "textbooks"
    
    elif cur_star == None and tiredness() == False: #not tired

        return "running"
    elif cur_star == None and tiredness() == True: # tired
        return "resting"
            
if __name__ == '__main__':
    initialize()
