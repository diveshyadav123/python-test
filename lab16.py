def average_student(**kwargs):
    sum=0

    for i in kwargs.values():
        sum= sum+i
        avg= sum/len(kwargs)
    return sum, avg

k = average_student(IT5014=60, IT7809=80, IT6798=50, IT5048=70)
print("Sum & average=", k)