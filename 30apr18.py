import random
import time
#123440
#123430 123540
#         123530 123630 123730 123830 123920 123040
#         123521 125421 163421 723430 tire 
#12345
#  Add and subtract for 22??
#  1234 on 1324 = 22
#  1-1=0
#  2-3!=0
#  3-2=1
#  4-3=0
#  1324-1234=90
#  1234 on 4231
#  Add = odd and even nums
def lst(guess):
    if guess != "99":
        print (guess)
    return


#123422
#123421
#123420
#123413
#123412
#123411
#123410
#123404
#123403
#123402
#123401
#123400
geslist=[]
#  guess=
def menu1(selektion):
    gn=0
    print('\n' * 5)
    print()
    print('Guess number ',gn, 'is ..  ',guess)
    print('        MENU')
    print('_______________________')
    print(ca)
    print(cb)
    print(cd)
    print(ce)
    print(cf)
    print(cg)
    print(ch)
    print(ci)
    print(cj)
    print(ck)
    print(cl)
    print(cm)
    print(cn)
    print(co)
    print('_______________________')
    print()
    res = input('Choose which bulls/hits answer is yours...')
    print(res)
# below, a to j res is the letter shadows for randomizing
a=b=c=d=e=f=g=h=i=j=res=""
rl=lres=0
HIST=''
gn=0
ca=cb=cc=cd=ce=cf=cg=ch=ci=cj=ck=cl=cm=cn=co=9
# below is stus lists for cols and digits
outlist=[]
d1c1=d2c1=d3c1=d4c1=d5c1=d6c1=d7c1=d8c1=d9c1=d0c1=''
d1c2=d2c2=d3c2=d4c2=d5c2=d6c2=d7c2=d8c2=d9c2=d0c2=''
d1c3=d2c3=d3c3=d4c3=d5c3=d6c3=d7c3=d8c3=d9c3=d0c3=''
d1c4=d2c4=d3c4=d4c4=d5c4=d6c4=d7c4=d8c4=d9c4=d0c4=''
bulllist=[]
hitlist=[]
notinthiscollist=[]

# print('outlist is ',outlist)
ns=["0","1","2","3","4","5","6","7","8","9"]
# print(ns)
a=ns[1];b=ns[2];c='3';d='4';e='5';f='6';g='7';h='8';i='9';j='0'
#  random.shuffle(ns) 
# print(ns)
a=ns[1];b=ns[2];c=ns[3];d=ns[4];e=ns[5];f=ns[6];g=ns[7];h=ns[8];i=ns[9];j=ns[0]
#  print(a,b,c,d,e,f,g,h,i,j)
guess=a+b+c+d
#  print(guess)
lstges=a+b+c+d+''
def pls(linestoblank):
    print('\n' * linestoblank)
pls(3)
guessnum = 0
print('GUESSES                 YOUR RESPONSE')
print('__________________________________')

def compute(guess,res):
    lst(guess)
    global HIST,guessnum,lstges,attempts
    attempts = 0
    lstges += ''
    guessnum += 1
    print('       Guess#',guessnum,guess,end='')
    res=input('  ')
    lres=len(res)
    if lres != 2:
        print ('Your response must be 2 numbers ie 12, or 40, or 22')
        attempts += 1
        if attempts > 3:
            pass
    if res == '40':
        print('Game over !')


    HIST = (HIST + guess)#
    HIST = (HIST + res)
    return res
#  pls(3)
gn=0
# uncomment 2 below to go the 1234 way
#ns=["0","1","2","3","4","5","6","7","8","9"]
#a=ns[1];b=ns[2];c=ns[3];d=ns[4];e=ns[5];f=ns[6];g=ns[7];h=ns[8];i=ns[9];j=ns[0]
guess=a+b+c+d
compute(guess,res)
#  #  print('HIST now is ',HIST)
#  Start 4th digit series
if HIST == a+b+c+d+'30':
    guess = a+b+c+e
    compute(guess,res)
if HIST == a+b+c+d+'30'+a+b+c+e+'30':
    bulllist.append (a+b+c)
    # print('The bull list is ',bulllist)
    hitlist.append(d+e)
    # print('the hitlist is ' ,hitlist)
    guess = a+b+c+f
    compute(guess,res)
    #  print('HIST is up to ',HIST)
if HIST == a+b+c+d+'30'+a+b+c+e+'30'+a+b+c+f+'30':
    guess = (a+b+c+g)
    compute(guess,res)
    #  print('HIST is up to ',HIST)
if HIST == a+b+c+d+'30'+a+b+c+e+'30'+a+b+c+f+'30'+a+b+c+g+'30':
    guess = a+b+c+h
    compute(guess,res)
    #  print('HIST is up to ',HIST)
if HIST == (a+b+c+d+'30'+a+b+c+e)+'30'+a+b+c+f+'30'+a+b+c+g+'30'+a+b+c+h+'30':
    guess = a+b+c+i
    compute(guess,res)
    #  print('HIST is up to ',HIST)
if HIST == a+b+c+d+'30'+a+b+c+e+'30'+a+b+c+f+'30'+a+b+c+g+'30'+a+b+c+h+'30'+a+b+c+i+'30':
    print()
    print('your number is ',a,b,c,j)

#  End 4th digit series

#  start 3rd digit series
if HIST == a+b+c+d+'30'+a+b+c+e+'20':
    guess = a+b+f+d
    compute(guess,res)
    #  print('HIST is up to ',HIST)
if HIST == a+b+c+d+'30'+a+b+c+e+'20'+a+b+f+d+'30':
    guess = a+b+g+d
    compute(guess,res)
    #  print('HIST is up to ',HIST)
if HIST == a+b+c+d+'30'+a+b+c+e+'20'+a+b+f+d+'30'+a+b+g+d+'30':
    guess = a+b+h+d
    compute(guess,res)
    #  print('HIST is up to ',HIST)    
if HIST == a+b+c+d+'30'+a+b+c+e+'20'+a+b+f+d+'30'+a+b+g+d+'30'+a+b+h+d+'30':
    guess = a+b+i+d
    compute(guess,res)
    #  print('HIST is up to ',HIST)
if HIST == a+b+c+d+'30'+a+b+c+e+'20'+a+b+f+d+'30'+a+b+g+d+'30'+a+b+h+d+'30'+a+b+i+d+'30':
    guess = a+b+j+d
    print('Your secret number is....',guess)
#  End of 3rd digit series 


# start of 2nd digit series
if HIST == a+b+c+d+'30'+a+b+c+e+'20'+a+b+f+d+'20':
    guess = a+g+c+d
    compute(guess,res)
    #  print('HIST is up to ',HIST)
if HIST == a+b+c+d+'30'+a+b+c+e+'20'+a+b+f+d+'20'+a+g+c+d+'30':
    guess = a+h+c+d
    compute(guess,res)
    #  print('HIST is up to ',HIST)
if HIST == a+b+c+d+'30'+a+b+c+e+'20'+a+b+f+d+'20'+a+g+c+d+'30'+a+h+c+d+'30':
    guess = a+i+c+d
    compute(guess,res)
    #  print('HIST is up to ',HIST)
if HIST == a+b+c+d+'30'+a+b+c+e+'20'+a+b+f+d+'20'+a+g+c+d+'30'+a+h+c+d+'30'+a+i+c+d+'30':
    guess = a+j+c+d
    print('Your secret is out. The number is......',guess)
#end of 2nd digit series

#  Start of 1st digit series
if HIST == a+b+c+d+'30'+a+b+c+e+'20'+a+b+f+d+'20'+a+g+c+d+'20':
    guess = h+b+c+d
    compute(guess,res)
    #  print('HIST is up to ',HIST)
if HIST == a+b+c+d+'30'+a+b+c+e+'20'+a+b+f+d+'20'+a+g+c+d+'20'+h+b+c+d+'30':
    guess = i+b+c+d
    compute(guess,res)
    #  print('HIST is up to ',HIST)
if HIST == a+b+c+d+'30'+a+b+c+e+'20'+a+b+f+d+'20'+a+g+c+d+'20'+h+b+c+d+'30'+i+b+c+d+'30':
    guess = j+b+c+d
    print('Your secret is out. The number is......',guess)
# end of 1st digit

if HIST == a+b+c+d+'30'+a+b+c+e+'21':
    guess = a+b+e+d
    compute(guess,res)
if HIST == a+b+c+d+'30'+a+b+c+e+'21'+a+b+e+d+'21':
    guess = a+e+c+d
    compute(guess,res)
if HIST == a+b+c+d+'30'+a+b+c+e+'21'+a+b+e+d+'21'+a+e+c+d+'21':
    guess =e+b+c+d
    print('Got it:',e,b,c,d)

if HIST == a+b+c+d+'30'+a+b+c+e+'20':
    guess = a+b+f+d
    compute(guess,res)
if HIST == a+b+c+d+'30'+a+b+c+e+'20'+a+b+f+d+'21':
    guess = a+f+c+d
    compute(guess,res)
if HIST == a+b+c+d+'30'+a+b+c+e+'20'+a+b+f+d+'21'+a+f+c+d+'21':
    guess = f+b+c+d
    print('Got this one!...',f,b,c,d)

if HIST == a+b+c+d+'30'+a+b+c+e+'20':
    guess = a+b+f+d
    compute(guess,res)














# start of 22
#  print(guess,HIST)

if HIST == a+b+c+d+'22': # only guess digits need arranging
    guess = a+e+f+g
    compute(guess,res)


if HIST == a+b+c+d+'22'+a+e+f+g+'01': #  a is hit
    guess = e+b+h+j
    compute(guess,res)


if HIST == a+b+c+d+'22'+a+e+f+g+'01'+e+b+h+j+'01' : # a and b are hits
    guess = b+a+c+d
    print(guess,' is your number')

# end of a, b hits changed to bulls

if HIST == a+b+c+d+'22'+a+e+f+g+'01': #  a is hitl
    guess = e+b+h+j
    compute(guess,res)


if HIST == a+b+c+d+'22'+a+e+f+g+'01'+e+b+h+j+'10' : # a is hit, b is bull
    guess = e+f+c+i
    compute(guess,res)



if HIST == a+b+c+d+'22'+a+e+f+g+'01'+e+b+h+j+'10'+e+f+c+i+'10' : # a is hitl, b is bull,c is bull
    guess = d+b+c+a
    print('you have  ',guess)


if HIST == a+b+c+d+'22'+a+e+f+g+'01'+e+b+h+j+'10'+e+f+c+i+'01' : # a is hitl, b is bull,c is bull
    guess = c+b+a+d                                               # c is a hit
    print('you have  ',guess)



# ca=30;cb=22;cn=55
# selektion=(ca,cb,cc,cd,ce,cf,cg,ch,ci,cj,ck,cl,cm,cn)
#         menu1(selektion)

if HIST == e+f+g+h+'22':
    guess = e+f+h+g
    compute(guess,res)





if HIST == a+b+c+d+'13':
    guess = a+b+c+e
    compute(guess,res)


if HIST == a+b+c+d+'12':
    guess = a+b+c+e
    computeguess,res


if HIST == a+b+c+d+'11':
    guess = a+b+c+e
    compute(guess,res)



if HIST == a+b+c+d+'10':
    guess = a+b+c+e
    compute(guess,res)


if HIST == a+b+c+d+'04': #  only arrange the 4 hits
    guess = a+b+c+e
    compute(guess,res)


if HIST == a+b+c+d+'03':
    guess = a+b+c+e
    compute(guess,res)


if HIST == a+b+c+d+'02':
    guess = a+b+c+e
    compute(guess,res)


if HIST == a+b+c+d+'01':
    guess = a+b+c+e
    compute(guess,res)



if HIST == a+b+c+d+'00': #start 5678 and 90 subs
    guess = e+f+g+h
    compute(guess,res)

if HIST == a+b+c+d+'00'+e+f+g+h+'22':
    guess = e+f+h+g
    compute(guess,res)

if HIST == a+b+c+d+'00'+e+f+g+h+'22'+e+f+h+g: 
    guess = e+f+h+g
    compute(guess,res)

if HIST == a+b+c+d+'00'+e+f+g+h+'22'+e+f+h+g+'04': 
    guess = f+e+g+h
    print('Your num is ',guess)


if HIST == a+b+c+d+'00'+e+f+g+h+'22'+e+f+h+g+'13':
    guess = e+h+f+g
    print('It is ',guess)

if HIST == a+b+c+d+'00'+e+f+g+h+'22'+e+f+h+g+'13'+e+h+f+g+'13': # ?????????
    guess = e+g+f+h
    print('It is   ',guess)












# Wait for 1 seconds
# time.sleep(1)
