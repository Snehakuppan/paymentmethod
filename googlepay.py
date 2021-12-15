#googlepay
class googlepayapp:
    def __init__(self,n,p,e):
        self.name=n
        self.phoneno=p
        self.emailid=e
    def opengpay(self):
        print("google pay")
    def nameverification(self):
        if type(self.name ) ==str:
            if len(self.name)<=20:
                print("name verified")
            else:
                raise ValueError("the name should contain less than or equal to 20 letters")
        else:
            raise TypeError("name should be letters only")
    def phonenoverification(self):
        if type(self.phoneno) == str: 
            if len(self.phoneno)==10:
                if self.phoneno[0]=="9" or self.phoneno[0]=="8" or self.phoneno[0]=="7" or self.phoneno[0]=="6":
                    print("phone number verified")
                else:
                    print("enter a valid number")
            else:
                raise  ValueError("phone number should contain 10 numbers")
                 
        else:
            raise TypeError("entered value should be only integers")
    def emailidverification(self):
        if type(self.emailid )==str:
            if len(self.emailid)<=30:
                print("emailid verified")
            else:
                raise ValueError("emailid should contain less than or equal to 30 ")
        else:
            raise TypeError("emailid should either contain only alphanumerics or strings not numbers alone")
    def otp(self,code,otp):
        if otp==code:
            print("otp is verified")
        else:
            raise ValueError("otp entered is not correct")
    def bankverification(self):
        self.account=[]
        self.accountno=3456789012
        self.account.append(self.accountno)
        print(self.account)
        print("bank account is verified")
    def pancardverification(self):
        self.pan="DF23457890"
        if len(self.pan)==10:
            print("pancard verified")
        else:
            raise ValueError("invalid pan no")
    def setpin(self,number):
        self.pin=number
        if len(self.pin)==4 or len(self.pin)==6:
            print("pin is created")
        else:
            raise ValueError("invalid no for pin")
    def enterpin(self,match,pin):
        self.pin=pin
        self.match=match
        if self.pin==self.match:
            print("success")
        else:
            raise ValueError("pin doesn't match")
        
sneha=googlepayapp("snehakuppan","9123529686","SnehaKuppan@gmail.com")
sneha.opengpay()
sneha.nameverification()
sneha.phonenoverification()
sneha.emailidverification()
sneha.otp(9876,9876)
sneha.bankverification()
sneha.pancardverification()
sneha.setpin("789090")
sneha.enterpin(9090,9090) 
        
            
        
