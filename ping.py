import os

def doping (host):
        hostname = host
        response = os.system("ping -c 3 "  + str(hostname))
        print (response)
        answer = response
        return answer