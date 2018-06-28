'''try:
    import tanya
    a=[1,2,3]
    print(a[3])
except ZeroDivisionError:
    print("number is divisible by 0")
except IndexError:
    print("index error doesnt exist")
except ImportError:
    print("import error")
else:
    print(a)
finally:
    print("i will execute")'''

'''class AgeError(Exception):
    pass
try:
    a=int(input("enter age"))
    if(a<18):
        raise AgeError
except AgeError:
    print("please enter integer")
else:
    print("you are eligible")'''

