#print("hello")
#pick by default the z and Z 
#if not pick the first character as morse code . _
#we will not be performing the de-coding as this is hashing but we will do an integrity check of length \
#once we have the which is not required in de hashing esnse as we cannot revert it so even to confirm we need to passs the same value to be hashed
import hashlib
def mrsc(tmpc):
    if tmpc.isalpha():
        dot=tmpc.lower()
        dash=tmpc.upper()
    else:
        dot='z'
        dash='Z'
    return dot,dash
#t1,t2=mrsc('c')
#print(t1,t2)
def dbenc(dot,dash,chenc):
    #this will have the db 
    #https://en.wikipedia.org/wiki/Morse_code
    if int(chenc) == 1:
        tmp=dot+dash+dash+dash+dash
    elif int(chenc) == 2:
        tmp=dot+dot+dash+dash+dash
    elif int(chenc) == 3:
        tmp=dot+dot+dot+dash+dash
    elif int(chenc) == 4:
        tmp=dot+dot+dot+dot+dash
    elif int(chenc) == 5:
        tmp=dot+dot+dot+dot+dot
    elif int(chenc) == 6:
        tmp=dash+dot+dot+dot+dot
    elif int(chenc) == 7:
        tmp=dash+dash+dot+dot+dot
    elif int(chenc) == 8:
        tmp=dash+dash+dash+dot+dot
    elif int(chenc) == 9:
        tmp=dash+dash+dash+dash+dot
    else:
        tmp=dash+dash+dash+dash+dash
    
    return tmp

def mrsencd():
    hashencd="i wanna hash this data yolo"
    dott,dasht=mrsc(hashencd[0])#here pass the data you wanna hash , its first element
    #print(dott,dasht)
    n=len(hashencd)#we are gonna hash this length and attach to the hashencd and then pass it to the sha1 (for length extension attack)
    n=str(n)
    hn=""
    for i in n:
        htmp=dbenc(dott,dasht,i)
        hn=hn+htmp
    finalhashencd=hashencd+" "+hn
    #print(hn,n,finalhashencd,M.H)
    #this will run with the digits to be encoded and pass this concatinated string to hash funnel
    sha1_builtin(finalhashencd) #final hash post preventive tech
    #the following hash is for just the string without length prevention attack and see its different from the one
    #sha1_builtin(hashencd)
def sha1_builtin(datatocrypt):
    #datatocrypt="yolo"
    sh1=hashlib.sha1()
    sh1.update(bytes(datatocrypt,'UTF-8'))#in this we pass bytes of data not string , either by bytes()using UTF-8 encoding scheme or b''
    #sh1.update(b'yolo')
    print(sh1.hexdigest())
    #print(sh1.digest())

mrsencd()