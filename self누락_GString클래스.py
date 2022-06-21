#전역 변수
str = "Not Class Member"

#클래스를 정의
class GString:
    def __init__(self):
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #약간의 버그(실수)
        print(self.str)

g = GString()
g.set("First Message")
g.print()
