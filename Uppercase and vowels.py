class test():
    def __init__(self,strs):
        self.strs=strs

    def show(self):
        res=list(self.strs)
        u=0
        c=0
        vowels='aeiouAEIOU'
        for i in res:
            if i.isupper()==True:
                u=u+1
        for i in res:
            if i in vowels:
                c=c+1

        return (u,c)

n=input()
obj=test(n)
print(obj.show())
