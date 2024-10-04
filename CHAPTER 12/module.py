
def myfunction():
    print("hello world ")


if __name__=="__main__":
    #if this code directely excuated by running form original file code will be wriiten not show in import file module ok 
    print("this code is directely run by original file ")
    myfunction()
    print(__name__)