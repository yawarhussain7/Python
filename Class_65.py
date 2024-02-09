print("Topic: Static Method ")

class tatic:

    def __init__(self,num):

        self.num = num

    def add_to_num(self,num):

        self.num = self.num + num
        return self.num

    # static method 
    @staticmethod
    def add(a):
        return a + 4

s = tatic(5)

print(s.num)

print(s.add_to_num(5))
print(s.add(4))
print(tatic.add(5))