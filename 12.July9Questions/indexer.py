

class Index:
    def __init__(self,name):
        self.name=name
        self.msgs=[]
        self.index={}
        self.total_msgs=0
        self.total_words=0

    def get_total_words(self):
        return self.total_words
    
    def get_total_msgs(self):
        return self.total_msgs

    def get_msg(self,n):
        return self.msgs[n]

    def add_msg(self,msg):
        self.msgs.append(msg)
        self.total_msgs+=1
        arr=msg.split()
        wordsCount=len(arr)
        self.total_words+=wordsCount

    def add_msg_and_indexing(self,msg_2):
        self.add_msg(msg_2)
        lineNo=self.total_msgs-1
        self.indexing(msg_2,lineNo)

    def indexing(self,msg_3,LineNo):
        self.index[LineNo]=msg_3
    
    def search(self,term):
        msgs=[]
        for i in range(self.total_msgs):
            arr=self.index[i].split()
            for z in (arr):
                if(z==term):
                    msgs.append((i,self.index[i]))
                    break
        return msgs

        


obj=Index('Hello')

obj.add_msg_and_indexing('I am here')
obj.add_msg_and_indexing('I am a good boy ')
obj.add_msg_and_indexing('yoo Man am?')

ans=obj.search('am')
print(ans)