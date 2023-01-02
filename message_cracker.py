import time,string

message="Please enter message here"

for i in range(len(message)):
    for j in string.ascii_letters:
        print(message[0:i]+j)
        time.sleep(0.005)
        if j == message[i]:
            break
        
    
    