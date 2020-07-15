class Song(object):
    def sing_me_a_song(self,a):
        for line in a:
            print(line)


happy_bday = Song()
happy_bday.sing_me_a_song(["wo"])




#init函数  区别是在实例化的时候需要加入函数的参数
class Sing(object):
    def __init__(self, b):
        self.b = b

    def sing_me_a_song(self):
        for line in  self.b:
            print(line)




sing_bday = Sing(["i","love","you"])
sing_bday.sing_me_a_song()