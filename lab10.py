def percentage(*args):
    sum=0
    for i in args:
        sum=sum+i
    avg= sum/len(args)
    print("Average=", avg)

    if avg >40:
        print("Pass")
    else:
        print("Fail")

percentage (20, 45, 40, 25)