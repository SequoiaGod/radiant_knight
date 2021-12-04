class Myclass:
    isss = 123
    def __init__(self,name,age,gender):
        self.name = name
        self.age =age
        self.gender = gender
        self.__init_ppt()

    def __init_ppt(self):
        print("hey")
    def fun(self):
        print("hello world")

my = Myclass("yan",18,"m")

my.fun()
