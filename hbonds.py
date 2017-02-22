#!/usr/bin/env python
import string,sys
import math
import os

# from decimal import Decimal
# from array import *
temp = lw = la = output = xp = xn = yp = yn = coords = []
h1 = h2 = o1 = o2 = link = [None] * 10000
A  = 0
flag = nlines = 0

def dist(X,Y):
    x1 = X[1]
    x2 = Y[1]
    y1 = X[2]
    y2 = Y[2]
    z1 = X[3]
    z2 = Y[3]
    return 2*(x1-x2)*(y1-y2)*a*b*cosgamma + 2*(y1-y2)*(z1-z2)*b*c*cosalpha + 2*(x1-x2)*(z1-z2)*a*c*cosbeta + (x1-x2)*(x1-x2)*a*a + (y1-y2)*(y1-y2)*b*b + (z1-z2)*(z1-z2)*c*c


def init():
    x = [None] * 5000
    file = open(sys.argv[1],'r')
    for i in range(9):
        file.readline() # skip first 9 lines
    for i in range(N): # read in x, y, z coordinates 
        line = file.readline()
        words = [float(n) for n in line.split()]
        x.append(words)
    file.close()
    x = [a for a in x if a != None]
    dx = 1- x[0][2]
    dy = x[0][3]
    dz = x[0][4]
    for i in range(len(x)):
        x[i][0] = int(x[i][0])
        x[i][1] = int(x[i][1])
        x[i][2] = x[i][2] + dx
        x[i][3] = x[i][3] - dy
        x[i][4] = x[i][4] - dz
    return (x)

def ang(d1,d2,d3):# Note: square of the distances
    return math.degrees(math.acos((d1 + d2 - d3)/(2.0 * math.sqrt(d1) * math.sqrt(d2))))

def find(y,c):
    x=grab= grabxp = grabxn = grabyp = grabyn = grabxpyp = grabxnyn = grabxnyp = grabxpyn = [None] * 50000
    for i in range(len(c)):
        grab = ((c[i][1],c[i][2],c[i][3],c[i][4],c[i][0]))
        grabxp = ((c[i][1],c[i][2]+1,c[i][3],c[i][4],c[i][0]))
        grabxn = ((c[i][1],c[i][2]-1,c[i][3],c[i][4],c[i][0]))
        grabyp = ((c[i][1],c[i][2],c[i][3]+1,c[i][4],c[i][0]))
        grabyn = ((c[i][1],c[i][2],c[i][3]-1,c[i][4],c[i][0]))
        grabxpyp = ((c[i][1],c[i][2]+1,c[i][3]+1,c[i][4],c[i][0]))
        grabxpyn = ((c[i][1],c[i][2]+1,c[i][3]-1,c[i][4],c[i][0]))
        grabxnyp = ((c[i][1],c[i][2]-1,c[i][3]+1,c[i][4],c[i][0]))
        grabxnyn = ((c[i][1],c[i][2]-1,c[i][3]-1,c[i][4],c[i][0]))
        for j in range(len(y)):
            if grab[0] == y[j]:
                x[9*i+0]=grab
                x[9*i+1]=grabxp
                x[9*i+2]=grabxn
                x[9*i+3]=grabyp
                x[9*i+4]=grabyn
                x[9*i+5]=grabxpyp
                x[9*i+6]=grabxpyn
                x[9*i+7]=grabxnyp
                x[9*i+8]=grabxnyn
    file.close()
    return(x)

###############################################   Manual input starts here               ################################################
# rHS = string.split((raw_input('\natom ID of H_adsorbate : ')))                                                         ################                                                                                                         
# rOS = string.split((raw_input('atom ID of O_adsorbate : ')))                                                           ################                                                                                                       
# rHW = string.split((raw_input('atom ID of H_water     : ')))                                                           ################                                                                                                       
# rOW = string.split((raw_input('atom ID of O_water     : ')))                                                           ################                                                                                                       
                                                                                                                         ################                                         
# rHS = []                                                                                                               ################                                                   
# rOS = ['3']                                                                                                            ################                                                      
# rHW = ['5']                                                                                                            ################                                                      
# rOW = ['4']                                                                                                            ################                                                      
                                                                                                                         ################                                         
# rHS = [8,9]                                                                                                            ################                                                      
# rOS = [4,5]                                                                                                            ################                                                      
# rHW = [7]                                                                                                              ################                                                    
# rOW = [6]                                                                                                              ################                                                    
# if os.path.isfile("types"):                                                                                            ################                                                                      
rC = [2,3,4,5]                                                                                                           ################                                                       
rHS = [10,11]                                                                                                            ################                                                      
rOS = [6,7]                                                                                                              ################                                                    
rHW = [9]                                                                                                                ################                                                  
rOW = [8]                                                                                                                ################                                                  
                                                                                                                         ################                                         
fixedposcar = 0                                                                                                          ################                                                        
                                                                                                                         ################
###############################################   Manual input ends here               ##################################################
file = open(sys.argv[1],'r')
for i in range(3):
    file.readline() # skip first 3 lines
line = file.readline()
N = int(line)
file.readline() # skip the next line
line = file.readline()
words = string.split(line)
xlo_bound = float(words[0])
xhi_bound = float(words[1])
if len(words)==3:
    xy =  float(words[2])
else:
    xy = 0    # get xy value for the box
line = file.readline()
words = string.split(line)
ylo_bound =  float(words[0])
yhi_bound =  float(words[1])
if len(words)==3:
    xz =  float(words[2])
else:
    xz = 0    # get xz value for the box
line = file.readline()
words = string.split(line)
zlo =   float(words[0])
zhi =   float(words[1])
if len(words)==3:
    yz =  float(words[2])
else:
    yz = 0    # get yz value for the box
xlo = xlo_bound - min(0.0,xy,xz,xy+xz)
xhi = xhi_bound - max(0.0,xy,xz,xy+xz)
ylo = ylo_bound - min(0.0,yz)
yhi = yhi_bound - max(0.0,yz)
lx=xhi-xlo
ly=yhi-ylo
lz=zhi-zlo
a=lx
b=math.sqrt(ly*ly+xy*xy)
c=math.sqrt(lz*lz+xz*xz+yz*yz)
cosalpha = (xy*xz+ly*yz)/b/c
cosbeta = xz/c
cosgamma = xy/b
V = math.sqrt((1-cosalpha*cosalpha-cosbeta*cosbeta-cosgamma*cosgamma+2*cosalpha*cosbeta*cosgamma))*a*b*c
# print xlo, xhi, ylo, yhi,zlo, zhi, xy, xz, yz
print '--------------------------------------------------------------------------------------------------------'
print "lattice info: ", a, b, c, cosalpha, cosbeta, cosgamma, V
file.close
# ########################################################################################################################################################

coords = init() #reads in atoms coords
h1 = find (rHS,coords)
h2 = find (rHW,coords)
o1 = find (rOS,coords)
o2 = find (rOW,coords)
h1 = [x for x in h1 if x != None]
h2 = [x for x in h2 if x != None]
o1 = [x for x in o1 if x != None]
o2 = [x for x in o2 if x != None]

NH = (len(h1)+len(h2))/9
NHW = len(h2)/9
NHS = NH - NHW
NO = (len(o1)+len(o2))/9
NOW = len(o2)/9
NOS = NO - NOW

for i in range(len(h1)):
    for j in range(len(o1)):
        d = dist(h1[i],o1[j])
        if d <= 1.2:
            temp.append((o1[j],h1[i],round(d,8)))
temp=list(set(temp))
la=sorted(temp)
temp = []
for i in range(len(h2)):
    for j in range(len(o2)):
        d = dist(h2[i],o2[j])
        if d <= 1.2:
            temp.append((o2[j],h2[i],round(d,8)))
temp=list(set(temp))
lw=sorted(temp)
# for i in range(len(la)):
#     print la[i]
# print len(la)
# for i in range(len(lw)):
#     print lw[i]
# print len(lw)

#########################################################################################################################################################
print '--------------------------------------------------------------------------------------------------------'
if fixedposcar == 0:
    print('export ALL FIXED POSCAR coordinates')
else:
    print('export PARTIAL RELAXED POSCAR coordinates')
####################   To change, fixedposcar = 1    will give    all fixed flags '
#                                 fixedposcar = 0    will give    partailly fixed flags '
print('Found Total Number of atoms: %d' % N)
print '________________________________________________________________________________________________________'
print('O_acceptor      O_donar        O-O_Dist              A-H_Dist         AHD_Angle             ADH_Angle ')
print '________________________________________________________________________________________________________'
fo1 = fo2 =temp = []

for i in range(len(o1)):
   for j in range(len(o2)):
        do1o2 = dist(o1[i] , o2[j])  
        if do1o2 <= float(12.25):
           for l in range(len(h2)):
               do2h2 = dist(o2[j],h2[l])
               if do2h2<=1.3:
                    do1h2 = dist(o1[i] , h2[l])
                    A1 = ang( do1o2 , do1h2, do2h2)
                    A2 = ang( do2h2 , do1h2, do1o2)
                    # if A2>=120:  
                    if A1<=30 and A2>=120:# and do1h2<=6.25:                     
                        link.append((o1[i][4],o2[j][4]))
                        temp.append((o1[i][4] , o2[j][4] , round(math.sqrt(do1o2),8), round(math.sqrt(do1h2),8) , round(A2,8), round(A1,8)  ))
           for l in range(len(h1)):
               do1h1 = dist(o1[i],h1[l])
               if do1h1<=1.3:
                    do2h1 = dist(o2[j] , h1[l])
                    # print do1h1,do1o2,do2h1
                    A1 = ang( do1o2 , do2h1, do1h1 )
                    A2 = ang( do1h1 ,do2h1, do1o2 )
                    # if  A2>=120:
                    if  A1<=30 and A2>=120:# and do2h1<=6.25:
                        link.append((o2[j][4], o1[i][4]))
                        temp.append(( o2[j][4], o1[i][4] ,  round(math.sqrt(do1o2),8) , round(math.sqrt(do2h1),8), round(A2,8), round(A1,8)  ))

temp=list(set(temp))
temp=sorted(temp)
temp = [x for x in temp if x != None]
link=list((set(link)))
link=sorted(link)
link = [x for x in link if x != None]
if link!=[]:
    fo1, fo2 = zip(*link)
i=0
for x in fo1:
    if fo1.count(x)==1:
        print '   ', temp[i][0], "    I      ", temp[i][1],  "         %.8f    " %temp[i][2], "     %.8f      " %temp[i][3]," %.8f" %temp[i][4],'     ', "    %.8f      " %temp[i][5]
    if fo1.count(x)==2:
        print '   ', temp[i][0], "    II     ", temp[i][1],  "         %.8f    " %temp[i][2], "     %.8f      " %temp[i][3]," %.8f" %temp[i][4],'     ', "    %.8f      " %temp[i][5]
    if fo1.count(x)==3:
        print '   ', temp[i][0], "    III    ", temp[i][1],  "         %.8f    " %temp[i][2], "     %.8f      " %temp[i][3]," %.8f" %temp[i][4],'     ', "    %.8f      " %temp[i][5]        
    i=i+1   

if i!= len(temp):
    print "warning"

# for i in range(len(temp)):
#     print '   ', temp[i][0], "          ", temp[i][1],  "         %.8f    " %temp[i][2], "     %.8f         " %temp[i][3]," %.8f" %temp[i][4],'  ', "    %.8f   " %temp[i][5]
print '________________________________________________________________________________________________________'
print 'Total hydrogen bond(s) btw water and the adsorbate:  %d\n' % (i)


temp=[]
for i in range(len(lw)):
    for j in range(len(link)):
        if lw[i][0][4] == link[j][0] or lw[i][0][4] == link[j][1]:
            temp.append(lw[i][0][4])
            temp.append(lw[i][1][4])
temp=list(set(temp))

# identifying the total number of atoms as N and write corresponding poscar
output1 = open('POSCAR', 'w')
header1 = """                             
   8.41590000000000     
     1.0000000000000000    0.0000000000000000    0.0000000000000000
     0.5000000095058164    0.8660253995413444    0.0000000000000000
     0.0000000000000000    0.0000000000000000    Z
   Pt   C    O    H 
    27     3     NO     NH
Selective dynamics
Direct"""
output1.writelines((header1.replace("NO" ,str(NO)).replace("NH" , str(NH)).replace("Z" , str(c/8.4159)),'\n'))

output2 = open('POSCAR_expbg', 'w')
header2 = """                             
   8.41590000000000     
     1.0000000000000000    0.0000000000000000    0.0000000000000000
     0.5000000095058164    0.8660253995413444    0.0000000000000000
     0.0000000000000000    0.0000000000000000    Z
   Pt     O     H 
    27     NO     NH
Selective dynamics
Direct"""
output2.writelines((header2.replace("NO" ,str(NOW)).replace("NH" , str(NHW)).replace("Z" , str(c/8.4159)),'\n'))

output3 = open('POSCAR_imp', 'w')
header3 = """                            
   8.41590000000000     
     1.0000000000000000    0.0000000000000000    0.0000000000000000
     0.5000000095058164    0.8660253995413444    0.0000000000000000
     0.0000000000000000    0.0000000000000000    Z
   Pt   C    O    H 
    27   3    NO    NH
Selective dynamics
Direct"""
output3.writelines((header3.replace("NO" ,str(len(temp)/3+NOS)).replace("NH" , str(2*len(temp)/3+NHS)).replace("Z" , str(c/8.4159)),'\n'))

output4 = open('POSCAR_impbg', 'w')
header4 = """                             
   8.41590000000000     
     1.0000000000000000    0.0000000000000000    0.0000000000000000
     0.5000000095058164    0.8660253995413444    0.0000000000000000
     0.0000000000000000    0.0000000000000000    Z
   Pt     O     H 
    27    NO    NH
Selective dynamics
Direct"""
output4.writelines((header4.replace("NO" ,str(len(temp)/3)).replace("NH" , str(2*len(temp)/3)).replace("Z" , str(c/8.4159)),'\n'))

for i in range(len(coords)):
    grab = [coords[i][1],coords[i][2],coords[i][3],coords[i][4]]
    if fixedposcar == 0:
        tail = 'F     F     F\n'
        if i+1 <= 27:
            print >> output1, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,
            print >> output2, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,
            print >> output3, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,
            print >> output4, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,
        elif ( i+1  < 34 or  i+1  > N-(N-27-3-NO-NHW)):
            tail = 'T     T     T\n'
            print >> output1, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,
            print >> output3, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,
        else:
            if ((i+1) in temp):
                tail = 'T     T     T\n'
                print >> output1, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,
                print >> output2, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,
                print >> output3, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,
                print >> output4, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,
            else:
                tail = 'F     F     F\n'
                print >> output1, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,
                print >> output2, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,

    elif fixedposcar == 1:
        tail = 'F     F     F\n'
        if  i+1  <= 27:
            print >> output1, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,
            print >> output2, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,
            print >> output3, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,
            print >> output4, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,

        elif ( i+1  < 34 or  i+1  > N-(N-27-3-NO-NHW)):
            print >> output1, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,
            print >> output3, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,

        else:
            if ((i+1) in temp):
                print >> output1, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,
                print >> output2, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,
                print >> output3, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,
                print >> output4, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,

            else:
                print >> output1, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,
                print >> output2, "%.8f    " % grab[1], "%.8f    " % grab[2] , "%.8f    " % grab[3], '        ' , tail,

output1.close
output2.close
output3.close
output4.close