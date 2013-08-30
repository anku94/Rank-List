import Acc
RD=Acc.RL
def D2S(Dic, key):
    Astr="<tr>"
    Astr+="<td>"+key+" "+"</td>"
    b=Dic[key]
    Astr+="<td>"+b[0]+"</td>"
    Astr+="<td>"+str(b[1]+b[2]+b[3]+b[4]+b[5])+" "+"</td>"#Add all question numbers
    Astr+="<td>"
    for i in range(1,6):#range(x,y) where y=No.Questions+1
        if b[i]!=0:
            Astr+="P"+str(i)+" "
    Astr+="</td><td>"+str(b[-2]*100.0/b[-1])[:5]+"</td></tr>"
    Total=b[1]+b[2]+b[3]+b[4]+b[5]#Add all question numbers
    Acc=b[-2]*100.0/b[-1]
    return [Astr, Total, Acc]
RL=[]
for i in RD.keys():
  RL.append(D2S(RD, i))
RL.sort(key=lambda x: x[1]*100 + x[2], reverse=True)
#print RL[2]
for i in range(len(RL)):
    print RL[i][0][:4]+"<td>"+str(i+1)+"</td>"+RL[i][0][4:]
