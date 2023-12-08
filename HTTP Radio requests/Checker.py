#needed for url stuffs
import requests

#friendly welcome
print("Ey pal, mind passing us the link?")

#grabs input
In = input()

#reaches out to the url and records the status code
Status = requests.get(In, stream=True).status_code

##checks if the status is good or not
if Status >= 300:
    #bad status
    print("Sorry pal, server said %s"%(Status))
else:
    #good status
    print("ayyyy, server returned %s code"%(Status))