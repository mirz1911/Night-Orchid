import ipapi

def program(arg):
    location = ipapi.location(ip = arg) 
    
    rs = location.items()
    return rs