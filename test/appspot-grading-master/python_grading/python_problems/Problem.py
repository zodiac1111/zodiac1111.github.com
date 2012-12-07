class Problem:
    def __init__(self,intro,test,init=""):
        self.intro=intro
        self.test=test
        self.init=init
    def __repr__(self):
        return "hello"
    def short_intro(self):
        short_enough = self.intro.split('\n')[0].replace('</a>','')
        if len(short_enough) > 150:
            short_enough = short_enough[0:120] + "..."
        return short_enough
