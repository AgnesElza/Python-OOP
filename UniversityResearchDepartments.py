class Research:
    def __init__(self, id, topic, author, department):
        self.id = id
        self.topic = topic
        self.author = author
        self.dep = department


class University:
    def __init__(self, list):
        self.list = list

    def searchbytopic(self, s_topic):
        ret = []
        flag = 0
        for r in self.list:
            if r.topic == s_topic:
                ret.append(r)
                flag = 1
        if flag == 0:
            return None
        else:
            return ret

    def MaxResearchDepartment(
            self):  #Assuming no department have same number of researches
        depDict = {}
        for r in self.list:
            if r.dep in depDict:
                depDict[r.dep] = depDict[r.dep] + 1
            else:
                depDict[r.dep] = 1
        max_key = max(depDict, key=depDict.get)
        return max_key


if __name__ == '__main__':
    num = int(input("Total Records:"))
    objlist = []
    for i in range(num):
        id = int(input("ID:"))
        topic = input("Topic:")
        author = input("Author:")
        department = input("Department:")
        r = Research(id, topic, author, department)
        objlist.append(r)
    s_topic = input("Topic to be searched:")
    u = University(objlist)
    retlist = u.searchbytopic(s_topic)
    if retlist == None:
        print("No research in the given topic")
    else:
        for i in retlist:
            print("***Search results in the given topic***")
            print(i.id)
            print(i.topic)
            print(i.author)
            print(i.dep)
    print("Department with maximum number of researches:",u.MaxResearchDepartment())
