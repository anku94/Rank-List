import RLv3
import re
RL=RLv3.Dic
Acc=RLv3.AccTest
#print Acc
def filt(x):
    match=re.search(r'201[1|0].....', x)
    if match:
        m2=re.search(r'Accepted', x)
        if m2:
            return False
        else:
            return True
    else:
        return False
ni=[]
acc2=filter(filt, Acc)
for i in range(len(acc2)):
    roll=acc2[i].split("<td>")[2][:-5]
    try:
	RL[roll][-1]+=1
    except:
	   pass

#for i in RL.keys():
#    print RL[i]


