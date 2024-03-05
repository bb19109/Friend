class 宇哲:

    def __init__(self, 拐氣, 英雄聯盟, 寶寶, 酪梨, 別人很屌, 隊友的怒氣值,積分,FB):
        self.拐氣 = 拐氣  
        self.英雄聯盟 = 英雄聯盟
        self.寶寶 = 寶寶
        self.酪梨 = 酪梨
        self.別人很屌 = 別人很屌
        self.隊友的怒氣值 = 隊友的怒氣值
        self.積分 = 積分
        self.FB = FB

    def 看到別人很屌(self, 別人很屌):
        print("這不是我，我超爛")

    def 看到酪梨(self, 酪梨, 寶寶):
        if 寶寶 == 酪梨:
            return("這我寶寶" + 酪梨)
        else:
            return("不符合我胃口")

    def 這把我C(self, 英雄聯盟, 積分):
        print("這把我C")
        積分 +=1
        return 積分
        
    def 講小G8話拐到隊友(self, 拐氣, 隊友的怒氣值,英雄聯盟):
        if (拐氣 >= 隊友的怒氣值)and(英雄聯盟 == True):
            print("好啦，我C咩")
            宇哲.這把我C()
        else:
            print("說說而已啦")

    def FBTag(self,FB,寶寶):
        if FB == 寶寶:
            print("@王聖凱 我寶寶")
            print("發到DC")

        if FB == "很屌的人事物":
            宇哲.看到別人很屌
            print("@王聖凱 這不是我")
        
        print("聖凱的FB充滿一堆通知")


            
            


