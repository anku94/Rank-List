import urllib2
import urllib
numProb=7
#req=urllib2.urlopen('http://10.4.3.68/oj/judge')
req=urllib2.urlopen('http://web.iiit.ac.in/~ankush.jain/status.html')
length=req.read()
length=length.split()
def sieve(x):
  if x.find('acc')!=-1:
    if x.find('Compile')==-1:
      if x.find('Exited')==-1:
        return x
def sieve2(x):
  if x.find('acc')!=-1:
    return x
def removeTags(x):
  for i in range(len(x)):
    if x[i]=='<':
      x=x[:i]
      return x
      break
for i in range(len(length)):
  if length[i].find('Wrong')!=-1:
    length[i]=length[i]+length[i+1]
records=map(sieve2, length)
records=filter(lambda x:x!=None, records)
records=map(lambda x:x.split('<td>'), records)
show=int(removeTags(records[0][1]))+100
show=str(show)
values={'start':'0','show': show}
data=urllib.urlencode(values)
req=urllib2.urlopen('http://web.iiit.ac.in/~ankush.jain/status.html')
#req=urllib2.urlopen('http://web.iiit.ac.in/~ankush.jain/rranklistnjw.html')
#f=open("Temp","w")
#f.write(str((re2q.read().split())))
#temp testing
#file=open('rr')
#length=file.read()


#temp over
length=req.read()
length=length.split()
AccTest=length
for i in range(len(length)):
  if length[i].find('Wrong')!=-1:
    length[i]=length[i]+length[i+1]
  elif length[i].find('Time')!=-1:
    length[i]=length[i]+length[i+1]+length[i+2]
records=map(sieve, length)
records=filter(lambda x:x!=None, records)
records=map(lambda x:x.split('<td>'), records)
for i in range(len(records)):
  records[i]=[removeTags(records[i][1]), removeTags(records[i][2]), removeTags(records[i][3]), removeTags(records[i][4]), removeTags(records[i][5])]

list=['Ankush Jain']
Dic={}
for i in range(numProb):
  list.append(0)
for i in range(len(records)):
  if Dic.has_key(records[i][1])==False:
    Dic[records[i][1]]=['Ankush Jain', 0, 0, 0, 0, 0, 0, 0, 0, 0]#Change According to number of questions, number of zeroes is numQ + 2
  ls=Dic[records[i][1]]
  pNo=records[i][2]
  pNo=pNo[1:]
  pNo=int(pNo)
  NewMarks=int(records[i][4])
  OldMarks=Dic[records[i][1]][pNo]
  if NewMarks > OldMarks:
    Dic[records[i][1]][pNo]=NewMarks

mem=open('Team')
mem=mem.read()
mem=mem.split('\n')
mem=map(lambda i: mem[i].split('\t'), range(len(mem)))
mem=filter(lambda x: x!=[''], mem)
dic2={}
for i in range(len(mem)):
	dic2[mem[i][0]]=mem[i][1]
llen=map(lambda x: len(x), dic2.values())
llen.sort(reverse=True)
lmax=llen[0]

def strext(astr):
  add=' '*(lmax-len(astr))
  astr=astr+add
  return astr
for i in Dic.keys():
	Dic[i][0]=strext(dic2[i])

try:
    del Dic['test']
except KeyError:
    pass

#Insert number of successful submissions in dictionary

for i in Dic.keys():
    count=Dic[i].count(100)
    Dic[i][-2]=count
    Dic[i][-1]=count
    #print Dic[i]


