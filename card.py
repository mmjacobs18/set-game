class Card:
    def __init__(self,color,shape,shade,number):
        self.color=color
        self.shape=shape
        self.shade=shade
        self.num=number

    def __str__(self):
        return "{"+self.color +  "/" +  self.shape + "/" + self.shade + "/" + str(self.num)+"}"
