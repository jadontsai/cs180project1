def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''
    
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
    
    bored_with_stars = False
    
    last_activity = None
    last_activity_duration = 0
    
    cur_time = 0
    
    last_finished = -1000

    global tired
    tired = False
    
    global previous_activity_duration
    previous_activity_duration = 0

    global previous_activity
    previous_activity = None

def prev_activity_duration():
    if last_activity == "resting" and (previous_activity != "resting" or previous_activity == None):
        previous_activity = last_activity
        previous_activity_duration = last_activity_duration
        return previous_activity_duration
    elif last_activity == "resting" and previous_activity == "resting":
        previous_activity = last_activity
        previous_activity_duration += last_activity_duration
        return previous_activity_duration
    
def tiredness():
    global tired
    global last_activity
    global last_activity_duration
    global previous_activity
    global previous_activity_duration
    if last_activity == "running" or "textbooks":
        tired = True
        return tired
    elif last_activity == None:
        tired = False
        return tired
    elif last_activity == "resting" and last_activity_duration >= 120:
        tired = False
        return tired
    elif last_activity == "resting" and previous_activity_duration <= 120:
        tired  = True
    elif last_activity == "resting" and previous_activity_duration >= 120:
        tired = False
        return tired
    else:
        return None


def star_can_be_taken(activity):
    global last_activity
    global bored_with_stars
    if last_activity == activity and bored_with_stars == False:
        return True
    else: 
        return False
    
def perform_activity(activity, duration):
    global cur_health
    global cur_hedons
    global last_activity_duration
    global last_activity
    last_activity = activity
    if activity == "running":
        if duration <= 180 and duration >= 0: #gains 3 health points every minute up to 180 minutes
            cur_health += (3*duration) 
            if (last_activity == "running" or "textbooks") and last_activity_duration <= 120:
                # loses 2 hedons IF NO STAR and IF tired, loses 2 hedons per minute
                cur_hedons -= 2 * duration 
                return cur_health, cur_hedons
            if (last_activity == "running") and last_activity_duration >= 120 and duration <= 10:
                cur_hedons += 2 * duration
                return cur_health, cur_hedons
            if (last_activity == "running") and last_activity_duration >= 120 and duration >= 10:
                cur_hedons += (2 * 10) - (2 * (duration - 10))
                return cur_health, cur_hedons
            if (tiredness() == False): #not tired
                return None
        elif duration >= 180: # gains 1 health point per minute over 180 minutes
            cur_health += (3 * 180 + (duration - 180))
            return cur_health
    elif activity == "textbooks":
        cur_health += 2 * duration
        if (tiredness() == True) and cur_star == None: # loses 2 hedons IF NO STAR and IF tired, loses 2 hedons per minute
                cur_hedons -= 2 * duration 
                return cur_health, cur_hedons
        return cur_health
    elif activity == "resting":
        cur_health = cur_health
        cur_hedons = cur_hedons
        return cur_health
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
    if activity == "running" and star_can_be_taken(activity) == True:
        cur_star = True
        
        return activity
    elif activity == "textbooks":
#something
        return
    elif activity == "resting":
#something
        return
    else:
        print("Invalid activity")
        return None

def most_fun_activity_minute():
    global cur_star_activity
    global cur_star
    #return activity with most hedons in one minute
    # not tired running returns 2 hpm
    # not tired textbook returns 1hpm
    #resting returns 0 always
    #tired turns negative
    # if tired AND no star, return resting
    # if tired and star for something, return the thing
    # if not tired,  and no star return running
    #if not tired, and star for something, return the thing
    if cur_star != None and cur_star_activity == "running":
        return "running"
        
    elif cur_star != None and cur_star_activity == "textbpoks":
        return "textbooks"
    
    elif cur_star == None and (last_activity == "resting" and last_activity_duration >= 180) or last_activity == None: #not tired
        return "running"
    elif cur_star == None and (last_activity == "resting" and last_activity_duration <= 180 or (last_activity == "running" or "textbooks")): # tired
        return "resting"
    


    
################################################################################
#These functions are not required, but we recommend that you use them anyway
#as helper functions

def get_effective_minutes_left_hedons(activity):
    '''Return the number of minutes during which the user will get the full
    amount of hedons for activity activity'''
    pass
    
def get_effective_minutes_left_health(activity):
    if activity == "running":
        return
    else:
        return None

def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    pass
            

def estimate_health_delta(activity, duration):
    pass
        
################################################################################
        
if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)    
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2           		
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)    
    offer_star("running")              
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)  
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10
