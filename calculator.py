def calc(num1,num2,kgrne):
    if kgrne==1:
        c=num1+num2
        print("sum",c)
    elif kgrne==2:
        c=num1-num2
        print("diff",c)
    elif kgrne==3:
        c=num1*num2
        print("multi",c)
    elif kgrne==4:

        c=num1/num2
        try:
             print("division",c)
        except Exception as e:
            print(e)
    else:
        print("not aviable")
def main():
    while True:
        print("what do you want to do")
        print("1.add")
        print("2.sub")
        print("3 multi")
        print("4.division")
        k=int(input("k grne ho:"))
        num1=float(input("enter num1"))
        num2=float(input("enter num2"))
        
        ans=calc(num1,num2,k)
        again=input("do you want to continule")
        if again!='y':
            break
if __name__=="__main__":
    main()
 



        