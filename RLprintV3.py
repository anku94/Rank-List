import Acc
RD=Acc.RL
nQ=7
def D2S(Dic, key):
    Total=0
    Astr="<tr>"
    Astr+="<td>"+key+" "+"</td>"
    b=Dic[key]
    for i in range(1, nQ+1):
        Total+=b[i]
    Astr+="<td>"+b[0]+"</td>"
    Astr+="<td>"+str(Total)+" "+"</td>"#Add all question numbers
    Astr+="<td>"
    for i in range(1,nQ+1):#range(x,y) where y=No.Questions+1
        if b[i]!=0:
            Astr+="P"+str(i)+" "
    Astr+="</td><td>"+str(b[-2]*100.0/b[-1])[:5]+"</td></tr>"
    Acc=b[-2]*100.0/b[-1]
    return [Astr, Total, Acc]
RL=[]
for i in RD.keys():
  RL.append(D2S(RD, i))
RL.sort(key=lambda x: x[1]*100 + x[2], reverse=True)
for i in range(len(RL)):
    print RL[i][0][:4]+"<td>"+str(i+1)+"</td>"+RL[i][0][4:]
