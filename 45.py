class Main:
    def met(self,arg1,arg2 = 0):
        if arg2 == 0:
            print("THE VALUE OF ARG1 IS: ",arg1)
        else:
            print("THE VALUES OF ARG1 AND ARG2 ARE: ", arg1,arg2)

obj=Main()
obj.met(10)
obj.met(10,20)