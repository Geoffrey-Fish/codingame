#SOLVED  after so much time has passed.at least a month.lol
def tempfinder(t):
    maxi = 0
    mini = 0
    if t == [] :
        return 0
    elif 0 in t :
        return 0
    for i in range(len(t)) :
        if t[i] > 0 and maxi == 0 :
            maxi = t[i]
        elif t[i] > 0 and t[i] < maxi :
            maxi = t[i]
        elif t[i] < 0 and mini == 0 :
            mini = t[i]
        elif t[i] < 0 and t[i] > mini :
            mini = t[i]
    if mini != 0 and maxi != 0 :
        if abs(mini) < maxi :
            return mini
        else :
            return maxi
    elif mini == 0 :
        return maxi
    else :
        return mini

        print(mini)
        print(maxi)
e = [-9,-8,-5,-3,-1,34,29,15,12,2,3,7,57]
print(tempfinder(e))

