##VC_tde USE only  @ logitech , Lorry RUi
##//////////usage://///////////////
## please install lib:   vc_hid-2021.3.10-py3-none-any.whl
##from vc_hid import vc_hid as hid
##test = hid.HID_class()
##flag,value=test.hidset(pid,setID,controlID,readnumber,anotherCMD)    ## flay ,0 means find. if -1 means never find
### return two data ,like : 0 [40, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
##flag1,value1=test.readhid(pid,readID,controlID,readnumber)  ## controlID means reportID,
### return two data ,like : 0 [41, 1, 0, 0, 4, 74, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # return defined by FW: this means FW version 1.1.0.74
##/////////////////////////////////////////
##VC_tde USE only  @ logitech , Lorry RUi
##

from vc_hid import vc_hid as hid

pid="89a"  ## this is Kong PID
pid1="867"  ## this is Meridain PID
mousepid="c332"
setID="28"
readID="29"
LED=""
mousebutton="a"
controlID=20
readnumber=20

test = hid.HID_class()




if(__name__)=="__main__":
    anotherCMD=[0,0,0,0]
    
    passflag,data=test.hidset(pid1,setID,controlID,readnumber,anotherCMD)
    print(passflag,data)

    
    passflag,data=test.readhid(pid1,readID,controlID,readnumber)  
    print(passflag,data)


    
##    passflag,data=test.hidset(pid,setID,controlID,readnumber,anotherCMD)
##    print(passflag,data)
##
##    
##    passflag,data=test.readhid(pid,readID,controlID,readnumber)  
##    print(passflag,data)
   


##    i = 0
##    while i < 10:
##        passflag,data=test.readhid(pid1,readID,1,readnumber)
##        print(passflag,data)
##        i += 1







