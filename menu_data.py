communication_board = {
    "Main Menu": {
        "Food & Drink": None,
        "Comfort": None,
        "Environment Control": None, 
        "Emergency": None
    },
    
    "Food & Drink": {
        "I want Water": None,
        "I am Hungry": None,
        "I want Coffee": None,
        "Back": "BACK"
    },

    "Comfort": {
        "I am in Pain": None,
        "I need Bathroom": None,
        "I want to Sleep": None,
        "Adjust Position": None,
        "Back": "BACK"
    },

    "Environment Control": {
        "Turn Light ON": "LIGHT_ON",  
        "Turn Light OFF": "LIGHT_OFF", 
        "Fan ON": "FAN_ON",           
        "Fan OFF": "FAN_OFF",        
        "Heater ON": "HEATER_ON",      
        "Heater OFF": "HEATER_OFF",   
        "AC ON": "AC_ON",              
        "AC OFF": "AC_OFF",             
        "Back": "BACK"
    },

    "Emergency": {
        "Call Doctor": None,
        "I can't breathe": None,
        "Help Me": None,
        "Back": "BACK"
    }
}

def get_menu_items(menu_name):
    if menu_name in communication_board:
        return list(communication_board[menu_name].keys())
    return []

def get_arduino_command(category, item):
    try:
        return communication_board[category][item]
    except KeyError:
        return None