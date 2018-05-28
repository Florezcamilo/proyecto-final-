users=[]

def getusers():
    """
    """
    global users
    file = open ('users.txt','r')
    for line in file:
        line = line.replace('\n','')
        sub_list = line.split(',')
        users.append(sub_list)
    file.close()

def setsusers(users):
    """
    """
    w=0
    while w < len(users):
        i=0
        while i < len(users):
            j=0
            while j < len(users):
                p=0
                while p < len(users):
                    try:
                        if users[i][0] == users[j][0]:
                            if i == j:
                                pass
                            else:
                                if i > j:
                                    users.pop(j)
                                    break
                    except IndexError:
                        break
                    p+=1
                j+=1
            i+=1
        w+=1
        
getusers()
setsusers(users)
