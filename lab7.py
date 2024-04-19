class GradingSystem:
    #def __init__(self):
        #self.average= GradingSystem.average()
        #self.classification=''

    def average(self):
        num=int(input("Enter the number of subjects:"))
        arr_scores=[]
        for i in range(num):
            input_score=int(input("Enter score:"))
            arr_scores.append(input_score)

        sum=0
        for i in arr_scores:
            sum=sum+i
        average=sum/len(arr_scores)
        print (average)
        return average

    def grading(self):
        avg=self.average()
        if avg > 90:
            print("FirstClass")
        elif avg >=70:
            print("Second class upper")
        elif avg >=60:
            print("Second lower class")
        elif avg <60 and avg >=50:
            print("pass")
        elif avg < 50:
            print("Fail")

myobj= GradingSystem()
#myobj.average()
myobj.grading()