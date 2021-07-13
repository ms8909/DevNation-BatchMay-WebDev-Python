import pickle

class Index:
    def __init__(self, name):
        self.name = name
        self.msgs = []
        self.index = {}
        self.total_msgs = 0
        self.total_words = 0

    def get_total_words(self):
        return self.total_words

    def get_msg_size(self):
        return self.total_msgs

    def get_msg(self, n):
        return self.msgs[n]

    # implement
    def add_msg(self, m):
        self.msgs.append(m)
        self.total_msgs+=1


    def add_msg_and_index(self, m):
        self.add_msg(m)
        line_at = self.total_msgs - 1
        self.indexing(m, line_at)

    # implement
    def indexing(self, m, line_at):
        words_array = m.split(' ') ### For example : Input "Hello worlds this is" Output : ["Hello","worlds","this","is"]

        for i in range(len(words_array)):
            if words_array[i] not in self.index: ## self.index = {}
                self.index[words_array[i]] = [] ## self.index["Hello"] = []
                self.index[words_array[i]].append(line_at) ## [0]
        return

    ### {"hello",[0,1],"world",[1]}


    # implement: query interface

    def search(self, term):
        indices = self.index[term]

        msgs = []
        for i in indices:
            message = (self.msgs[int(i)])
            line_num = i
            temp_tuple = (line_num,message)

        msgs.append(temp_tuple)
        return msgs




if __name__ == "__main__":

        name ="hassan"
        obj = Index(name)
        obj.add_msg_and_index("What is this thing called mohsin")
        obj.add_msg_and_index("What is mohsin")
        answer = obj.search("mohsin")
        print(answer)

