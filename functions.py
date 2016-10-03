def beef():
    print('functions are cool')


def bitcoin_to_usd(btc):
    amount = btc * 527
    return amount

# beef()
# amount = bitcoin_to_usd(3.85)
# print(amount)
#

# default variables

def getgender(sex='unknown'):
    if sex is 'm':
        sex = 'male'
    elif sex is 'f':
        sex = 'female'
    print(sex)


# getgender('m')
# getgender('f')
# getgender()

#Keyword arguments

def dumb_sentence(name="Mark", action="ate", item="tuna"):
    print(name, action, item)

dumb_sentence()
dumb_sentence('Sally', 'farts', 'gently')
dumb_sentence(item='awesome', action="is")

#