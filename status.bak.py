import MySQLdb as db

def index():
	user="%"
	conn = db.connect(host="10.4.3.68",passwd="password",user="root",db="oj")
	cursor = conn.cursor()
	cursor.execute("select sid,username,problemid,status,score from submission where username like %sorder by sid desc",(user,))
	temp_string = ""
	for i in cursor:
		if i[3]=="Accepted":
			temp_string+= "<tr class=\"acc\">"
		else:
			temp_string+= "<tr class=\"nacc\">"
		temp_string+= "<td>"+str(i[0])+"</td>"
		temp_string+= "<td>"+str(i[1])+"</td>"
		temp_string+= "<td>"+str(i[2])+"</td>"
		temp_string+= "<td>"+str(i[3])+"</td>"
		temp_string+= "<td>"+str(i[4])+"</td>"
		temp_string+="</tr>"
	f = open("sutatus.html").read()
	return f % (temp_string,)
f=open("status.html","w")
f.write(index())
