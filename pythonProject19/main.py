class with_replacement:
    def create(self):
        self.a = int(input('The size of your dictionary :'))
        self.dict = {}
        return "Dictionary created with size of : ", self.a

    def insert(self, value):
        if len(self.dict) != self.a:
            key = value % self.a
            self.dict[key] = value
            return self.dict

    def find(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            return "Key Not Found"

    def remove(self, key):
        if key in self.dict:
            del self.dict[key]
            return self.dict
        else:
            return "key Not Found"


a = with_replacement()
a.create()
#--The size of your dictionary: 10
#('Dictionary created with size of : ', 10)
a.insert(10)
#--{0: 10}
a.insert(21)
#--{0: 10, 1: 21}
a.insert(30)
#--{0: 30, 1: 21}
a.find(2)
#--'Key Not Found'
a.find(1)
#--21
a.remove(0)
#--{1: 21}


class without_replacement:
    def create(self):
        self.a = int(input('The size of your dictionary :'))
        self.dict = {}
        return "Dictionary created with size of : ", self.a

    def insert(self, value):
        if len(self.dict) != self.a:
            key = value % self.a
            if key in self.dict:
                no = self.dict[key]
                no.append(value)
            else:
                self.dict[key] = [value]
            return self.dict

    def find(self, key, value):
        if key in self.dict:
            if value in self.dict[key]:
                return "Value is present at that key : ", [str(key) + ":" + str(value)]
            else:
                return "Value at that key Not Found"
        else:
            return "Key Not Found"

    def remove(self, key, value):
        if key in self.dict:
            if value in self.dict[key]:
                rem = self.dict[key]
                rem.remove(value)
                del self.dict[key]
                self.dict[key] = rem
            else:
                return "Value at that key is not there"
            return self.dict
        else:
            return "key Not Found"


b = without_replacement()
b.create()
#--'The size of your dictionary: 10'
#('Dictionary created with size of : ', 10)

b.insert(20)
#--{0: [20]}
b.insert(10)
#--{0: [20, 10]}
b.insert(30)
#--{0: [20, 10, 30]}
b.find(0, 20)
#--('Value is present at that key : ', ['0:20'])
b.find(0, 50)
#--'Value at that key Not Found'
b.remove(0, 10)
#--{0: [20, 30, 40]}
