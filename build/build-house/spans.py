# Simple-span rafter/joist calc per NDS-style allowable stress, DF-L No.2 & SPF No.2 (NDS Supplement Table 4A ref values)
import math
SIZES = {"2x6":(1.5,5.5,1.3),"2x8":(1.5,7.25,1.2),"2x10":(1.5,9.25,1.1),"2x12":(1.5,11.25,1.0)}
SP = {"DF-L No.2":(900,1.6e6),"SPF No.2":(875,1.4e6),"Hem-fir No.2":(850,1.3e6)}
def span(size, sp, oc, LL, DL, defl, CD):
    b,d,CF = SIZES[size]; Fb,E = SP[sp]
    S=b*d*d/6; I=b*d**3/12
    Fbp = Fb*CF*1.15*CD
    w = (LL+DL)*oc/12/12  # lb/in
    Lb = math.sqrt(8*Fbp*S/w)
    wl = LL*oc/12/12
    Ld = (384*E*I/(5*wl*defl))**(1/3)
    return min(Lb,Ld)/12
def fmt(ft):
    inch=int(ft*12); return f"{inch//12}′-{inch%12}″"
if __name__=="__main__":
    for sz in SIZES:
        print("floor 40/10 L360 16oc DF", sz, fmt(span(sz,"DF-L No.2",16,40,10,360,1.0)))
    for LL in (20,30,50,70):
        for sz in SIZES:
            print("rafter",LL,"/10 L180 24oc DF", sz, fmt(span(sz,"DF-L No.2",24,LL,10,180,1.15)), "16oc", fmt(span(sz,"DF-L No.2",16,LL,10,180,1.15)))
