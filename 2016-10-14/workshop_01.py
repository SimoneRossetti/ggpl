from larlib import *
l = [.2,.2,.2]
xp = [.1]
yp = [.1]
zp = [.5]
xt = [0]
yt = [.1]
zt = [-.5,.1]

i=0


while i<len(l):
	xp.append(-l[i])
	xp.append(.1)
	if i==0:
		xt.append(.05+l[i]+.1)
	elif i==len(l)-1:
		xt.append(l[i]+.15)
	else:
		xt.append(l[i]+.1)
	i=i+1
	
	

#xt = [.25,.25]
#yt = [.1,-1]
#zt = [-.5,.1]
#xt = QUOTE(xt)
#yt = QUOTE(yt)
#zt = QUOTE(zt)

#tRect = PROD([PROD([xt,yt]),zt])

xt = QUOTE(xt)
yt = QUOTE(yt)
zt = QUOTE(zt)
tRect = PROD([PROD([xt,yt]),zt])


xp = QUOTE(xp)
yp = QUOTE(yp)
zp = QUOTE(zp)
rectP = PROD([PROD([xp,yp]),zp])

mod = STRUCT([tRect,rectP])

VIEW(mod)

#Porco zio mo che devo fa ?
#(bx,bz) parametri della sezione trave
#(px,py) parametri sezione pilastro
#[dy1,dy2,..........] distanza tra i pilastri
#[hz1,hz2,..........]
#
#
#
#
#
#






