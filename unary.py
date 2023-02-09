#SOLVED !!!!EINSELF
satz = 'C C'
asci = []
liste = list(satz)
for i in liste:
    asci.append(format(ord(i),'07b'))
final_string = ''
buffero = 0
bufferi = 0
stringer = ''
for i in range(len(asci)) :
    stringer =str(asci[i])
    for number in stringer :
        if number == '0' :
            if bufferi == 0 :
                buffero += 1
            else :
                final_string += ('0' + ' ' + (bufferi*'0' + ' '))
                bufferi = 0
                buffero += 1
        else :
            if buffero == 0:
                bufferi += 1
            else :
                final_string += ('00' + ' ' + (buffero*'0') + ' ')
                buffero = 0
                bufferi += 1
if buffero > 0 :
    final_string += ('00' + ' ' + (buffero*'0') + ' ')
if bufferi > 0 :
    final_string += ('0' + ' ' + (bufferi*'0') + ' ')

final = final_string[0:-1]
print(final)
