import psutil
print "\"pid\""",""\"laddr\""",""\"raddr\""",""\"status\""
dictionary = dict()
for c in  psutil.net_connections(kind="tcp"):
    laddr = "%s@%s" % (c.laddr)
    raddr = ""
    if c.raddr and c.laddr:
        if str(c.pid) not in dictionary.keys():
            list1 = [0]
            list1[0] = 1
            dictionary[str(c.pid)] = list1
            raddr = "%s@%s" % (c.raddr)
            string = "\""+ str(c.pid) + "\"" +","+"\""+laddr+"\""+","+"\""+raddr+"\""+","+"\""+c.status+"\""
            list1.append(string)
        else:
            list1[0] = list1[0] + 1
            dictionary[str(c.pid)] = list1
            raddr = "%s@%s" % (c.raddr)
            string = "\""+ str(c.pid) + "\"" +","+"\""+laddr+"\""+","+"\""+raddr+"\""+","+"\""+c.status+"\""
            list1.append(string)


for key, value in sorted(dictionary.items(), key=lambda e: e[1][0], reverse = True):
    for i in range(1,len(value)):
        print value[i]
