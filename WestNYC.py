import requests
import random
import string
import json
import time


print ('Created by @thenorthcop https://twitter.com/TheNorthCop')
print ('///////////////////////////////////////////////////////')
    


def sending():

    with open("names.txt", "r") as f:
        lines = f.readlines()

    url = 'https://manage.kmail-lists.com/subscriptions/subscribe?a=Qmfm7G&g=Q468Mg'

    RF = random.choice(lines)
    RL = random.choice(lines) 
    
    name_extra = ''.join(random.choice(string.digits))
    name_extra2 = ''.join(random.choice(string.digits))
    name_extra3 = ''.join(random.choice(string.digits))
    name_extra4 = ''.join(random.choice(string.digits))
    Firstname = RF
    Lastname = RL
    
    Email = 'put email here' + '+' + name_extra + name_extra2 + name_extra3 +'@gmail.com'  #change the value that says 'put email here', dont include the @gmail.com and leave the ''
   
    Size = '9' #change size here
    
    data = {
    
        'k8789a8e588f36bf522d0f24a53805327': Email,
		'k169d59f89d4d6519617a660b32b6695a': Firstname,
        'k9c364e249686c0c90a6558c31862ef21': Lastname,
        'k411af701ac56c3593160da27cb153048': Size

    }

    requests.post(url, allow_redirects=False, data= data)
    
    print (' Entered raffle for: First Name = {} Last Name = {} Size = {} Email = {}'.format(Firstname, Lastname, Size, Email))



def main():
    while(True):
        sending()
        time.sleep(1)
        
    return

if __name__ == "__main__":
    main()
