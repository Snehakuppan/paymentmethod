#phonepe
import googlepay



class phonepe(googlepay.googlepayapp):
    def __init__(self,n,p,e):
        super().__init__(n,p,e)
        self.name=n
        self.phoneno=p
        self.emailid=e
    def openphonepe(self):
        print("phone pe")
priya=phonepe("priyak","9087654321","priyaramkumar@gmail")
priya.openphonepe()
priya.nameverification()
priya.phonenoverification()
priya.emailidverification()
priya.otp(9876,9876)
priya.bankverification()
priya.pancardverification()
priya.setpin("7890")
priya.enterpin(9091,9091)

googlepay2=[{"name":"sneha","gpayno or upiid":9123529686,"type":"personal","transaction":"sucessful"},
            {"name":"ahmed","gpayno or upiid":"ahmed@okaxis","type":"business&bills","transaction":"declined"},
            {"name":"akshitha","gpayno or upiid":8667422287,"type":"personal","transaction":"sucessful"},
            {"name":"amma","gpayno or upiid":9940249686,"type":"business&bills","transaction":"sucessful"},
            {"name":"amritha","gpayno or upiid":6379098872,"type":"personal","transaction":"declined"},
            {"name":"anithaakka","gpayno or upiid":7092467908,"type":"business&bills","transaction":"sucessful"},
            {"name":"anniamma","gpayno or upiid":"sarada@oksbi","type":"personal","transaction":"sucessful"},
            {"name":"anu","gpayno or upiid":9445861900,"type":"personal","transaction":"sucessful"},
            {"name":"arunaakka","gpayno or upiid":6374304710,"type":"personal","transaction":"sucessful"},
            {"name":"ashikdisys","gpayno or upiid":6382421835,"type":"personal","transaction":"sucessful"},
            {"name":"avinasanna","gpayno or upiid":9384644269,"type":"personal","transaction":"failed"},
            {"name":"babytrisha","gpayno or upiid":7338828373,"type":"personal","transaction":"declined"},
            {"name":"bharathdisys","gpayno or upiid":9884412975,"type":"personal","transaction":"sucessful"},
            {"name":"barathiakka","gpayno or upiid":"barathi@oksbi","type":"personal","transaction":"sucessful"},
            {"name":"bavana","gpayno or upiid":7299903042,"type":"personal","transaction":"sucessful"},
            {"name":"benazer","gpayno or upiid":7010656843,"type":"personal","transaction":"failed"},
            {"name":"charu","gpayno or upiid":"charu@okcbi","type":"personal","transaction":"sucessful"},
            {"name":"dad","gpayno or upiid":9940507735,"type":"personal","transaction":"sucessful"},
            {"name":"deepthi","gpayno or upiid":9790823577,"type":"personal","transaction":"declined"},
            {"name":"dhanvarshini","gpayno or upiid":8056267526,"type":"personal","transaction":"declined"},
            {"name":"dineshdisys","gpayno or upiid":"dinesh@okhdfc","type":"personal","transaction":"sucessful"},
            {"name":"dineshbro","gpayno or upiid":8939215952,"type":"personal","transaction":"sucessful"},
            {"name":"divyaaka","gpayno or upiid":6380848540,"type":"personal","transaction":"declined"},
            {"name":"divyaschool","gpayno or upiid":8428230524,"type":"personal","transaction":"failed"},
            {"name":"gajalakshmi","gpayno or upiid":"gajalakshmi@oksbi","type":"personal","transaction":"sucessful"},
            {"name":"gayu","gpayno or upiid":9962482108,"type":"personal","transaction":"sucessful"},
            {"name":"gopika","gpayno or upiid":7338802855,"type":"personal","transaction":"sucessful"},
            {"name":"haritha","gpayno or upiid":9125286952,"type":"personal","transaction":"sucessful"},
            {"name":"hema","gpayno or upiid":"hema@oksbi","type":"personal","transaction":"sucessful"},
            {"name":"honeybee","gpayno or upiid":7010476992,"type":"personal","transaction":"sucessful"},
            {"name":"indhudisys","gpayno or upiid":"indhu@okhdfc","type":"personal","transaction":"sucessful"},
            {"name":"ishwarya","gpayno or upiid":"iswarya@okhdfc","type":"personal","transaction":"sucessful"}]
for i in googlepay2:
    for j,k in i.items():
        print(f"{j}:{k}")
            



        
            
