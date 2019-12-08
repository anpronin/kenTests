import math
import sys, getopt
import random
from math import sin
from math import cos
from math import atan
from math import asin
from math import sqrt

#comments

last = 1347
prb = int(input("Input Problem number:"))

#prb = int(sys.argv[1])
print ("Problem to solve:", prb, "\n", "Last was:", last)

miles2meters = 1609.34
feets2meters = 0.3048
g = 9.81
c = 3.e8
G = 6.67e-11
R = 8.31
TC = 273.15

a2r = math.pi/180.
r2a = 1./a2r

f2m = 0.0254 * 12
m2f = 1./f2m
pi = math.pi
mi2km = 1.6093

ans = -999
print("CALS for ", prb)

items = 5
factor = 0.4
arr = [0] * items
for i in range (0, items):
    ratio = 1. + random.uniform(-factor, +factor)
    if ( 0 == i): ratio = 1.0
    arr[i] = ratio

# 1 ########################
if( 143 == prb):
		km = 10900.
		par = km
		for r in arr:
			var = int(par * r)
			#Now calculation for ans
			ans = var/mi2km
			print ("I:=",i, "V:", var, "A:", int(ans))
		
if ( 151 == prb):
        l = 10.43
        w = 5.21
        h = 5.82
        ans = l * w * h * m2f ** 3
        par = l
        for i in range (0, items):
                ratio = 1. + random.uniform(-0.6, 0.6)
                if ( 0 == i): ratio = 1.0
                var = par * ratio
                ans = var * w * h * (m2f**3)
                print("I:", i, "V:", var, " A:", ans)

# 2 ########################
if ( 231 == prb):
        l = 96.
        rad = 49.
        par = l
        t = 2.* 60
        for r in arr:
                var = int(par * r)
                #Now calculation for ans
                ans = (2.*var + 2.*pi*rad)/t
                print ("V:", var, "A:", ans)
	        
if ( 239 == prb):
        t0 = 5.
        v0 = 8.
        t1 = 8.
        v1 = 12.
        par = v1
        for r in arr:
                var = int(par * r)
                #Now calculation for ans
                ans = (v0 + var) * (t1 - t0) /2.
                print ("V:", var, "A:", ans)
            
if (242 == prb):
        a = 3.5
        s = 30.
        par = s
        for i in range (0, items):
                ratio = 1. + random.uniform(-0.3, 0.3)
                if ( 0 == i): ratio = 1.0
                x = int(par * ratio)
                ans = math.sqrt(2.* a * x)
                print("VAR:", x, " ANS:", ans)

if ( 240 == prb):
        a = 10.8
        l = 400.
        par = l
        for r in arr:
                var = int(par * r)
                #Now calculation for ans
                ans = sqrt(2. * a * var)
                print ("V:", var, "A:", ans)

        
if ( 255 == prb):
        h = 41.
        ans = math.sqrt(2. * h/g)
        
if ( 255 == prb):
        h = 31.
        ans = math.sqrt(2. * h/g)

# 3 ###############################
        
if (306 == prb):
        x = 4.
        y = 7.
        par = 7
        for i in range (0, items):
                ratio = 1. + random.uniform(-0.6, 0.6)
                if ( 0 == i): ratio = 1.0
                var = int(par * ratio)
                ans = r2a * math.atan(x/var)
                print("VAR:", var, " ANS:", ans)

if( 309 == prb):
        v = 20.
        ang = 25.
        ans = v * math.cos(ang * a2r)

if ( 343 == prb):
        x1 = 3.
        y1 = 5.
        x2 = 7.
        y2 = -8.
        t = 2.
        d = math.sqrt ( (x1-x2)**2 + (y1 - y2)**2)
        ans = d/t

if( 350 == prb):
        V = 142.
        v = 16.
        ans = math.sqrt(V**2 - v**2)
        
# 4 ########################################

if ( 411 == prb):
        v = 12.
        ang = 20.
        par = v
        for r in arr:
                var = int(par * r)
                #Now calculation for ans
                vX = var * cos ( a2r * ang)
                vY = var * sin ( a2r * ang)
                t = 2. * vY /g;
                ans = t * vX
                print ("V:", var, "A:", ans)

if ( 413 == prb):
        h = 10.
        g = 10.
        par = h
        for r in arr:
                var = int(par * r)
                #Now calculation for ans
                ans = sqrt(2. * var/g)
                print ("V:", var, "A:", ans)

if ( 444 == prb):
        v0 = 20.
        ang = 30.
        par = v0
        for r in arr:
                var = int(par * r)
                #Now calculation for ans
                ans = var * cos(a2r * ang)
                print ("V:", var, "A:", ans)

if ( 445 == prb):
        v0 = 20.
        ang = 30.
        par = v0
        for r in arr:
                var = int(par * r)
                #Now calculation for ans
                ans = var * sin(a2r * ang)/g
                print ("V:", var, "A:", ans)

# 5 #########################################

if ( 511 == prb):
        F = 120
        m = 30.
        par = m
        for r in arr:
                par = int(par * r)
                #Now calculation for ans
                ans = F/par
                print ("V:", par, "A:", ans)
        
if (515 == prb):
        m = 1200.
        vf = 27.
        dt = 10.
        ans = m * vf / dt
        par = vf
        for i in range (0, items):
                ratio = 1. + random.uniform(-0.6, 0.6)
                if ( 0 == i): ratio = 1.0
                var = int(par * ratio)
                ans = m * var / dt
                print("Index:", i, "VAR:", var, " ANS:", ans)
        
if (519 == prb):
        m = 3.
        M = 5.
        F = 32.
        par = F
        for r in arr:
                par = int(par * r)
                #Now calculation for ans
                a = par/(m + M)
                ans = a * M
                print ("V:", par, "A:", ans)

if (520 == prb):
        m = 3.
        M = 5.
        F = 32.
        par = F
        for i in range (0, items):
                ratio = 1. + random.uniform(-0.6, 0.6)
                if ( 0 == i): ratio = 1.0
                var = int(par * ratio)
                a = var / (m + M)
                ans = a * m
                print("Index:", i, "VAR:", var, " ANS:", ans)

if (551 == prb):
        m = 60.
        a = 2.
        par = m
        for r in arr:
                par = int(par * r)
                #Now calculation for ans
                ans = par * ( a + g)
                print ("V:", par, "A:", ans)

if (556 == prb):
        m = 30.
        ang = 27.
        par = ang
        for r in arr:
                par = int(par * r)
                #Now calculation for ans
                ans = m * g * cos(par * a2r)
                print ("V:", par, "A:", ans)

if (557 == prb):
        m = 4.
        a = 3.
        par = a
        for r in arr:
                par = 0.1*int(10*par * r)
                #Now calculation for ans
                ans = r2a * asin(par/g)
                print ("V:", par, "A:", ans)

# 6 #######################################
if (601 == prb):
        m = 55.
        mu = 0.3
        par = m
        for r in arr:
                par = int(par * r)
                #Now calculation for ans
                ans = par * mu *g
                print ("V:", par, "A:", ans)


if (602 == prb):
        m = 55.
        mu = 0.3
        F = 140.
        par = m
        for i in range (0, items):
                ratio = 1. + random.uniform(-0.6, 0.6)
                if ( 0 == i): ratio = 1.0
                var = int(par * ratio)

                ans = var * g * mu
                if(ans > F):
                        ans = F
                print("Index:", i, "VAR:", var, " ANS:", ans)
                
if (609 == prb):
        m = 20.
        mu = 0.4
        par = mu
        for r in arr:
                par = 0.01 * int (par * r * 100.0)
                #Now calculation for ans
                ans = g * par
                print ("V:", par, "A:", ans)

if (610 == prb):
        m = 20.
        mu = 0.4
        par = mu
        for r in arr:
                par = 0.01 * int (par * r * 100.0)
                #Now calculation for ans
                ans = r2a * atan(par)
                print ("V:", par, "A:", ans)

if (628 == prb):
        m = 60.
        ang = 4.8
        par = ang
        for r in arr:
                par = par * r
                #Now calculation for ans
                ans = m * g / ( 2. * sin ( a2r * par))
                print ("V:", par, "A:", ans)
if (632 == prb):
        m = 30.
        M = 50.
        par = M
        for r in arr:
                par = int(par * r)
                #Now calculation for ans
                F = g * ( par - m)
                ans = F/(par + m)
                print ("V:", par, "A:", ans)
if (633 == prb):
        m = 30.
        M = 50.
        h = 1.
        par = M
        for r in arr:
                par = int(par * r)
                #Now calculation for ans
                F = g * ( par - m)
                a = F/(par + m)
                ans = sqrt ( 2. * h/a)
                print ("V:", par, "A:", ans)
        
if (646 == prb):
        v = 5.
        r = 50.
        m = 2.
        par = r
        for r in arr:
                par = int(par * r)
                #Now calculation for ans
                R = par * 0.01
                ans = v * v / R
                print ("V:", par, "A:", ans)
        
if (647 == prb):
        v = 5.
        r = 50.
        m = 2.
        par = r
        for r in arr:
                par = int(par * r)
                #Now calculation for ans
                R = par * 0.01
                a = v * v / R
                at = sqrt(a * a + g * g)
                ans = at * m
                print ("V:", par, "A:", ans)


if (653 == prb):
        R = 600.
        v = 150.
        m = 70.
        par = v
        for r in arr:
                par = int(par * r)
                #Now calculation for ans
                a = par * par /R
                ans = m * ( a + g)
                print ("V:", par, "A:", ans)

if (654 == prb):
        v = 320.
        ratio = 7.
        par = v
        for r in arr:
                par = int(par * r)
                #Now calculation for ans
                ans = par * par / (g * (ratio - 1))
                print ("V:", par, "A:", ans)

# 7 #########################################        

if ( 726 == prb):
        A = 2.
        B = 4.
        VA = 4.
        arr1 = [2,3,4,5,6]
        for r in arr1:
                par = r
                #Now calculation for ans
                ans = VA * sqrt (A/(par * B))
                print ("V:", par, "A:", ans)
        
if ( 727 == prb):
        A = 4
        VA = 6.
        VB = 2
        R = 2.
        par = VA
        for r in arr:
                par = int(par * r)
                #Now calculation for ans
                ans = A * (par/VB)**2 /R
                print ("V:", par, "A:", ans)

if ( 733 == prb):
    W = 200.
    k = 2500.
    par = W
    for r in arr:
        par = int(par * r)
        #Now calculation for ans
        ans = 100.0*par/k
        print ("V:", par, "A:", ans)

if ( 734 == prb):
    W = 6.
    dx = 4.
    par = dx
    for r in arr:
        par = 0.1*int(10.*par * r)
        #Now calculation for ans
        ans = 2.* W / (0.01 * par)**2
        print ("V:", par, "A:", ans)

if ( 745 == prb):
    m = 1600.
    vi = 15.
    vf = 40.
    t = 4.
    par = m
    for r in arr:
        par = 10*int(0.1*par * r)
        #Now calculation for ans
        ans = par * ( vf ** 2 - vi **2)/(t*2000)
        print ("V:", par, "A:", ans)

# 8 ###############################

if ( 840 == prb):
    m = 8.
    s = 10.
    g = 10.
    par = s
    for r in arr:
        par = int(par * r)
        #Now calculation for ans
        ans = 4. * par
        print ("V:", par, "A:", ans)


# 9 ############################

if ( 918 == prb):
    m = .140
    h = 2.
    par = m
    for r in arr:
        par = 0.01*int(100 * par * r)
        #Now calculation for ans
        v = sqrt (2. * g * h)
        ans = par * v
        print ("V:", par, "A:", ans)

if ( 919 == prb):
    m = .140
    vi = 1.2
    vf = 1.
    par = m
    for r in arr:
        par = 0.001*int(1000 * par * r)
        #Now calculation for ans
        ans = par * (vi + vf)
        print ("V:", par, "A:", ans)

if ( 922 == prb):
    m = .330
    t = 1.3
    par = m
    for r in arr:
        par = 0.001*int(1000 * par * r)
        #Now calculation for ans
        vf = g * t
        ans = par * vf
        print ("V:", par, "A:", ans)

if ( 923 == prb):
    m = .330
    v = 0.15
    t = 0.0655
    par = m
    for r in arr:
        par = 0.001*int(1000 * par * r)
        #Now calculation for ans
        vf = v + g * t
        ans = par * vf
        print ("V:", par, "A:", ans)

if ( 927 == prb):
    m = 45.
    mv = 0.375
    M = 60.
    par = M
    for r in arr:
        par = int(par * r)
        #Now calculation for ans
        ans = mv * m / par
        print ("V:", par, "A:", ans)

if ( 928 == prb):
    m = 45.
    M = 60.
    v = 0.6
    par = M
    for r in arr:
        par = int(par * r)
        #Now calculation for ans
        ans = v / ( 1 + par/m)
        print ("V:", par, "A:", ans)

if ( 934 == prb):
    m = 750.
    vme = 20.
    M = 900.
    VMN = 15.
    par = M
    for r in arr:
        par = 10 * int(0.1* par * r)
        #Now calculation for ans
        ans = sqrt( (m*vme)**2 + (par* VMN)**2)/(m + par)
        print ("V:", par, "A:", ans)

if ( 935 == prb):
    m = 750.
    vmn = 20.
    M = 900.
    VME = 15.
    par = M
    for r in arr:
        par = 10 * int(0.1* par * r)
        #Now calculation for ans
        pe = par * VME
        pn = m * vmn
        ans = r2a * atan(pn/pe)
        print ("V:", par, "A:", ans)

if ( 941 == prb):
    m = 320.
    v = 1.25
    M = 270.
    par = M
    for r in arr:
        par = int(par * r)
        #Now calculation for ans
        ans = v * (2. * m)/(m + par)
        print ("V:", par, "A:", ans)

if ( 942 == prb):
    m = 320.
    v = 1.25
    M = 270.
    par = M
    for r in arr:
        par = int(par * r)
        #Now calculation for ans
        ans = v * (m - par)/(m + par)
        print ("V:", par, "A:", ans)

if ( 957 == prb):
    m = 1000.
    v = 10.
    rate = 40.
    par = rate
    for r in arr:
        par = int(par * r)
        #Now calculation for ans
        ans = par * v / m
        print ("V:", par, "A:", ans)

if ( 958 == prb):
    m = 7.5
    v = 300.
    t = 0.4
    n = 8
    par = t
    for r in arr:
        par = 0.02*int(50*par * r)
        #Now calculation for ans
        ans = n * 0.001 * m * v / par
        print ("V:", par, "A:", ans)

# 10 #######################
if ( 1007 == prb):
    ang = 30.0
    arr = [59.1, 60.2, 72.2, 80.4, 89.3]
    for par in arr:
        #Now calculation for ans
        ans = 2. * g * par
        print ("V:", par, "A:", ans)

if ( 1017 == prb):
    w = 1.52
    par = w
    for r in arr:
        par = 0.01*int(100 *par * r)
        #Now calculation for ans
        ans = 2. * pi / par
        print ("V:", par, "A:", ans)

if ( 1018 == prb):
    r = 210
    par = r
    for r in arr:
        par = int(par * r)
        #Now calculation for ans
        ans = 2. * pi * par /60.
        print ("V:", par, "A:", ans)

if ( 1019 == prb):
    wi = 10.0
    wf = 6.3
    t = 5.0
    par = t
    for r in arr:
        par = 0.1* int(10 * par * r)
        #Now calculation for ans
        ans = (wi - wf)/par
        print ("V:", par, "A:", ans)

if ( 1020 == prb):
    wi = 15.0
    wf = 33.3
    a = 3.45
    par = a
    for r in arr:
        par = 0.01* int(100 * par * r)
        #Now calculation for ans
        ans = (wf - wi)/par
        print ("V:", par, "A:", ans)

if ( 1026 == prb):
    t = 8.36
    R = 4.65
    par = R
    for r in arr:
        par = 0.01* int(100 * par * r)
        #Now calculation for ans
        ans = 2 * pi * par / t
        print ("V:", par, "A:", ans)

if ( 1033 == prb):
    R = 10.
    m = 1.0
    arr = [1.0, 2.0, 3.0, 4.0]
    for par in arr:
        #Now calculation for ans
        ans = 1e6 * (0.001*m) * (2.*pi*par / 60.)**2 * (R*0.01)
        print ("V:", par, "A:", ans)

if ( 1048 == prb):
    R = 10.
    m = 3.
    w = 3.5
    arr = [ 10, 9, 8, 11, 12]
    for r in arr:
        par = r 
        #Now calculation for ans
        ans = 0.5 * 0.5 * m * (0.01 * par)**2 * w**2
        print ("V:", par, "A:", ans)

if ( 1049 == prb):
    R = 120.
    m = 0.449
    w = 3.6
    arr = [ 120, 110, 100, 90, 80]
    for r in arr:
        par = r 
        #Now calculation for ans
        ans = 0.5 * (1./12.) * m * (0.01 * par)**2 * w**2
        print ("V:", par, "A:", ans)

if ( 1055 == prb):
    L = 15.7
    arr = [15.7, 15.0, 13, 14.6, 12.0]
    for par in arr:
        #Now calculation for ans
        ans = sqrt(3. * g / (0.01 * par) )
        print ("V:", par, "A:", ans)

if ( 1056 == prb):
    ang = 30.0
    arr = [15.7, 15.0, 13, 14.6, 12.0]
    for par in arr:
        #Now calculation for ans
        ans = sqrt(3. * g * (1-cos(a2r * ang)) / (0.01 * par ) )
        print ("V:", par, "A:", ans)

# 11 #############################

if ( 1112 == prb):
    m = 8.
    arr = [0.55, 0.50, 0.45, 0.6, 0.65]
    for par in arr:
        #Now calculation for ans
        ans = par * m * g
        print ("V:", par, "A:", ans)

if ( 1113 == prb):
    m = 8.
    ang = 30.
    arr = [0.55, 0.50, 0.45, 0.6, 0.65]
    for par in arr:
        #Now calculation for ans
        ans = par * m * g * cos(a2r * ang)
        print ("V:", par, "A:", ans)

if ( 1114 == prb):
    m = 15.
    R = 1.5
    arr = [0.3, 0.4, 0.5, 0.2, 0.6]
    for par in arr:
        #Now calculation for ans
        ans = m * g * R/par
        print ("V:", par, "A:", ans)

if ( 1115 == prb):
    m = 15.
    R = 1.5
    arr = [220, 200, 210, 190, 250]
    for par in arr:
        #Now calculation for ans
        ans = m * g * R/par
        print ("V:", par, "A:", ans)

if ( 1122 == prb):
    m = 82.
    R = 5.
    arr = [1.6, 1.5, 1.7, 1.8, 2.0]
    for par in arr:
        #Now calculation for ans
        ans = 0.001 * m * g * (R - par)/par
        print ("V:", par, "A:", ans)

if ( 1123 == prb):
    m = 82.
    R = 5.
    arr = [1.6, 1.5, 1.7, 1.8, 2.0]
    for par in arr:
        #Now calculation for ans
        ans = 0.001 * m * g * R /par
        print ("V:", par, "A:", ans)

if ( 1137 == prb):
    m = 350.
    I = 6.e-6
    F = 2.5
    arr = [1.35, 1.25, 1.5, 1.0, 2.0]
    for par in arr:
        #Now calculation for ans
        M = 0.001 * m + I/(par * 0.01)**2
        ans = F/M
        print ("V:", par, "A:", ans)

if ( 1153 == prb):
    m1 = 1.
    m2 = 1.
    m3 = 2.
    x = 3.3
    y = 1.8
    arr = [3.25, 3.0, 2.5, 3.5, 3.1]
    for par in arr:
        #Now calculation for ans
        I = (m1 + m2) * y**2
        ans = 0.5 * I * par**2
        print ("V:", par, "A:", ans)

if ( 1154 == prb):
    m1 = 1.
    m2 = 1.
    m3 = 2.
    x = 3.3
    y = 1.8
    arr = [3.25, 3.0, 2.5, 3.5, 3.1]
    for par in arr:
        #Now calculation for ans
        I = (m2 + m3) * x**2
        ans = 0.5 * I * par**2
        print ("V:", par, "A:", ans)

# 12 ###########################

if ( 1206 == prb):
    cM = 2.0
    cR = 2.0
    arr = [59.1, 60.2, 72.2, 80.4, 79.3]
    for par in arr:
        #Now calculation for ans
        ans = par * g * cM/(cR) ** 2;
        print ("V:", par, "A:", ans)

if ( 1207 == prb):
    crho = 1.0
    cR = 2.0
    arr = [59.1, 60.2, 72.2, 80.4, 79.3]
    for par in arr:
        #Now calculation for ans
        ans = par * g * cR * crho;
        print ("V:", par, "A:", ans)

if ( 1215 == prb):
    arr = [4.9, 3.1, 2.0, 1.0, 7.5]
    for par in arr:
        #Now calculation for ans
        ans = sqrt(g/par) - 1.0
        print ("V:", par, "A:", ans)

if ( 1216 == prb):
    mk = 1e22
    R = 1.75e6
    arr = [7.4, 5.5, 3.5, 8.9, 6.0]
    for par in arr:
        #Now calculation for ans
        ans = G * mk * par /R**2
        print ("V:", par, "A:", ans)

if ( 1221 == prb):
    R1 = 2.0e7
    R2 = 3.0e7
    arr = [18,17,16,19,15]
    for par in arr:
        #Now calculation for ans
        ans = par * (R2/R1)**1.5
        print ("V:", par, "A:", ans)
        
if ( 1222 == prb):
    R1 = 6.0e7
    T1 = 12.
    arr = [16,17,18,19,15]
    for par in arr:
        #Now calculation for ans
        ans = R1 * ( par/T1 ) ** (2./3.) * 1e-7
        print ("V:", par, "A:", ans)

if ( 1238 == prb):
    R1 = 25e6
    V1 = 12.e3
    R2 = 95.e6
    M = 5.97e24
    arr = [12, 13, 11, 14, 15]
    for par in arr:
        #Now calculation for ans
        dE = 2.* G * M * (1./R1 - 1./R2)
        ans = sqrt((par * 1.e3)**2 - dE)
        print ("V:", par, "A:", ans)

if ( 1239 == prb):
    R1 = 40.e6
    V1 = 10.e3
    V2 = 9.1e3
    M = 5.97e24
    arr = [10, 9.5, 8.5, 8.0, 7.5]
    for par in arr:
        #Now calculation for ans
        R2 = 1/R1 + 1./(2. * G * M)*(V2**2 -(par * 1e3)**2)
        ans = 1./(R2 * 1e7)
        print ("V:", par, "A:", ans)

# 13 #########################

if ( 1309 == prb):
    arr = [32.8, 29.5, 18.5, 28.0, 17.5]
    for par in arr:
        #Now calculation for ans
        ans = 1.e5 * 1./(par * 1e3)
        print ("V:", par, "A:", ans)

if ( 1310 == prb):
    arr = [76.0, 67.0, 88.0, 80, 55.0]
    for par in arr:
        #Now calculation for ans
        ans = (par/60.)
        print ("V:", par, "A:", ans)

if ( 1328 == prb):
    m = 0.25
    arr = [0.64, 0.46, 0.5, 0.35, 0.9]
    for par in arr:
        #Now calculation for ans
        ans = m * (2.*pi)**2/par**2
        print ("V:", par, "A:", ans)

if ( 1329 == prb):
    m = 0.15
    arr = [3.58, 3.85, 4.5, 9.1, 7.5]
    for par in arr:
        #Now calculation for ans
        ans = 2.* pi * sqrt (m/par)
        print ("V:", par, "A:", ans)

if ( 1330 == prb):
    W = 22.3
    arr = [2.7, 5.0, 7.2, 4.0, 3.0]
    for par in arr:
        #Now calculation for ans
        ans = par**2 * (2.*pi)**2 * (W/g)
        print ("V:", par, "A:", ans)

if ( 1332 == prb):
    m = 0.35
    N = 100.
    arr = [48.9, 84.9, 32.1, 25.0, 13.0]
    for par in arr:
        #Now calculation for ans
        T = par/N
        k = m * (2.*pi/T)**2
        ans = 100.* m * g/k
        print ("V:", par, "A:", ans)

if ( 1338 == prb):
    m = 1.53
    f = 1.95
    arr = [7.5, 5.7, 6.0, 9.0, 4.5]
    for par in arr:
        #Now calculation for ans
        k = m * (2. * pi * f)**2
        ans = 0.5 * k * (1e-2 * par)**2
        print ("V:", par, "A:", ans)

if ( 1343 == prb):
    L = 0.64
    arr = [2.6, 6.2, 4.0, 5.1, 3.5]
    for par in arr:
        #Now calculation for ans
        ans = L * (2. * pi/par)**2
        print ("V:", par, "A:", ans)

if ( 1344 == prb):
    T = 2.0
    arr = [11.3, 13.1, 9.0, 4.1, 3.5]
    for par in arr:
        #Now calculation for ans
        ans = g * (T/par)**2.
        print ("V:", par, "A:", ans)

if ( 1346 == prb):
    m = 28.
    arr = [67, 66, 65, 64, 68]
    for par in arr:
        #Now calculation for ans
        T = 2. * pi * sqrt ( par/g)
        ans = T/4.
        print ("V:", par, "A:", ans)

if ( 1347 == prb):
    arr = [2.0, 1.5, 2.5, 3.0, 3.5]
    for par in arr:
        #Now calculation for ans
        ans = g * (par/(2.*pi))**2
        print ("V:", par, "A:", ans)

# 14 #########################

if ( 1410 == prb):
    lam = 750
    arr = [700, 800, 750, 850, 820]
    for par in arr:
        #Now calculation for ans
        vel = par * 1000./3600.
        length = lam * 1000.
        ans = vel/length
        print ("V:", par, "A:", ans)

if ( 1411 == prb):
    arr = [3., 4., 5., 6., 2.]
    for par in arr:
        #Now calculation for ans
        ans = par * par * g / (2 * pi)
        print ("V:", par, "A:", ans)

if ( 1412 == prb):
    T = 100.
    L = 6.
    arr = [700, 600, 800, 500, 400]
    for par in arr:
        #Now calculation for ans
        m = par * 0.001
        rho = m/L
        ans = sqrt(T/rho)
        print ("V:", par, "A:", ans)

if ( 1413 == prb):
    F = 140.
    L = 15.
    arr = [0.545, 0.4, 0.6, 0.3, 0.7]
    for par in arr:
        #Now calculation for ans
        T = par
        v = L/T
        rho = F/(v**2) 
        ans = rho * L
        print ("V:", par, "A:", ans)

if ( 1418 == prb):
    arr = [7.22, 6.11, 5.01, 8.22, 4.56]
    for par in arr:
        T = 2. * pi/par
        ans = T
        print ("V:", par, "A:", ans)

if ( 1420 == prb):
    arr = [6.00, 5.00, 11.00, 0.60, 4.00]
    for par in arr:
        ans = par
        print ("V:", par, "A:", ans)

if ( 1427 == prb):
    L0 = 1.
    arr = [20, 10, 15, 11, 13, 7]
    for par in arr:
        ans = 100. + 20. * math.log10(L0/par)
        print ("V:", par, "A:", ans)

if ( 1428 == prb):
    dB = 70.
    arr = [76, 60, 5, 55, 70]
    for par in arr:
        ans = dB + 10 * math.log10(par)
        print ("V:", par, "A:", ans)

if ( 1430 == prb):
    F0 = 80.
    c = 343.
    arr = [30, 20, 10, 40, 50]
    for par in arr:
        vo = par
        vs = 0
        F1 = F0 * (c + vo)/ ( c + vs)
        ans = F1
        print ("V:", par, "A:", ans)

if ( 1432 == prb):
    F0 = 80.
    c = 343.
    arr = [30, 20, 10, 40, 50]
    for par in arr:
        vo = -par
        vs = 0
        F1 = F0 * (c + vo)/ ( c + vs)
        ans = F1
        print ("V:", par, "A:", ans)

if ( 1439 == prb):
    L = 3.
    c = 343.
    arr = [490, 400, 500, 1000, 2000]
    for par in arr:
        f = par
        dx = c/f
        ans = dx/2
        print ("V:", par, "A:", ans)

if ( 1440 == prb):
    L = 3.
    c = 343.
    arr = [390, 200, 250, 3000, 5000]
    for par in arr:
        f = par
        dx = c/f
        ans = dx/4
        print ("V:", par, "A:", ans)

# 15 #########################

if ( 1510 == prb):
    F = 50
    P = 8.e4
    arr = [P, 7e4, 6e4, 9e4, 1e5]
    for par in arr:
        #Now calculation for ans
        S = F/par
        ans = 100.*math.sqrt(4 * S/pi)
        print ("V:", par, "A:", ans)

if ( 1511 == prb):
    M = 100
    m = 5
    p = 8e5
    w = 2.0
    arr = [M, 90, 80, 110, 70]
    for par in arr:
        #Now calculation for ans
        F = (m + par) * g/2.
        S = F/p
        L = S/(w*1e-2)
        ans = L*100    
        print ("V:", par, "A:", ans)

if ( 1513 == prb):
    h = 111
    rho = 1e3
    arr = [h, 110, 109, 112, 108]
    for par in arr:
        #Now calculation for ans
        ans = rho*g*par*1e-6  
        print ("V:", par, "A:", ans)

if ( 1520 == prb):
    hA = 7.
    hB = 20.0
    hC = 13.
    rho = 800.
    rhoW = 1e3
    arr = [hB, 21, 22, 19, 17]
    for par in arr:
        #Now calculation for ans
        dP = par * rhoW - (hC * rho + hA * rhoW  )
        ans = dP * g * 0.01
        print ("V:", par, "A:", ans)

if ( 1523 == prb):
    H = 25
    rho = 1e3
    RHO = 13.6e3
    arr = [H, 27, 30, 10, 12]
    for par in arr:
        #Now calculation for ans
        h = par * (RHO-rho)/rho
        ans = h /100.
        print ("V:", par, "A:", ans)

if ( 1524 == prb):
    H = 25
    rho = 1e3
    RHO = 820
    arr = [H, 27, 30, 10, 12]
    for par in arr:
        #Now calculation for ans
        h = par * (RHO-rho)/rho
        ans = h /100.
        print ("V:", par, "A:", ans)

if ( 1533 == prb):
    L = 10
    R = 5.
    h = 8.
    rho = 1e3
    arr = [L, 8, 9, 11, 12]
    for par in arr:
        #Now calculation for ans
        S = par * R
        p = rho * h * 10
        F = p * S
        ans = F * 1e-6
        print ("V:", par, "A:", ans)

if ( 1537 == prb):
    w = 12
    h = 4.0
    v = 2.5
    W = 9.
    H = 8.0
    arr = [v, 2.6, 2.4, 2.0, 1.0]
    for par in arr:
        #Now calculation for ans
        k = (W * H)/(w * h)
        V = par/k
        ans = V
        print ("V:", par, "A:", ans)

if ( 1538 == prb):
    w = 15
    h = 8.
    v = 2.5
    rho = 1e3
    arr = [v, 2.6, 2.4, 2.0, 1.0]
    for par in arr:
        #Now calculation for ans
        rate = w*h*par*rho*1e-5
        ans = rate
        print ("V:", par, "A:", ans)

# 16 #########################

if ( 1623 == prb):
    alpha = 17e-6
    L = 30
    W = 45
    H = 10
    T0 = 0
    T1 = 100
    arr = [T1, 90, 110, 80, 120]
    for par in arr:
        #Now calculation for ans
        k = 3 * alpha
        V = L * W * H
        dT = par - T0
        dV = V * k * dT
        ans = dV
        print ("V:", par, "A:", ans)

if ( 1626 == prb):
    alpha = 24e-6
    T0 = 0.
    T1 = 300.
    rho = 2.7e3
    arr = [T1, T1 + 100, T1 - 100, T1 + 200, T1 - 200]
    for par in arr:
        #Now calculation for ans
        k = 3 * alpha
        R = rho * (1 - k * (par - T0))
        ans = R
        print ("V:", par, "A:", ans)

# 17 #########################

if ( 1714 == prb):
    V = 20.
    n = 2.
    T = 30.
    arr = [T, T+10, T - 10, T+ 20, T +30]
    for par in arr:
        #Now calculation for ans
        p = n * R * (par + TC)/(V*1e-3)
        ans = p/1000.
        print ("V:", par, "A:", ans)

if ( 1715 == prb):
    V = 15.
    n = 3.
    P = 250
    arr = [P, P + 20, P * 2., P/2, P + 100]
    for par in arr:
        #Now calculation for ans
        T = (1e3 * par) * (V * 1e-3) /( n * R)
        ans = T
        print ("V:", par, "A:", ans)

# 18 #########################

if ( 1831 == prb):
    n = 1.7
    dT = 23.
    arr = [dT, dT+10, dT - 10, dT + 20, dT + 30]
    for par in arr:
        #Now calculation for ans
        Cp = (3/2  + 1) * R
        ans = n * Cp * par
        print ("V:", par, "A:", ans)

if ( 1832 == prb):
    n = 12
    Q = 700
    arr = [Q, Q/2, Q * 2, Q + 100, Q + 200]
    for par in arr:
        #Now calculation for ans
        Cv = n * (3/2) * R
        ans = par / Cv
        print ("V:", par, "A:", ans)

if ( 1840 == prb):
    Tc = 300
    Th = 500
    arr = [Th, 600, 650, 700, 400]
    for par in arr:
        #Now calculation for ans
        nu = (par - Tc)/par
        ans = nu
        print ("V:", par, "A:", ans)

if ( 1841 == prb):
    nu = 35.
    Th = 700
    arr = [Th, Th  + 50, Th * 1.1, Th - 100, Th + 200]
    for par in arr:
        #Now calculation for ans
        Tc  = par * ( 1 - nu * 0.01)
        ans = Tc
        print ("V:", par, "A:", ans)
        
if ( 1854 == prb):
    Tc = -20.
    Th = 20
    P = 25
    arr = [P, 35, 30, 45, 10]
    for par in arr:
        #Now calculation for ans
        dS = 1e3*(par/(Tc + TC) - par/(Th + TC))
        ans = dS
        print ("V:", par, "A:", ans)

if ( 1855 == prb):
    Tc = -20.
    Th = 20
    P = 25
    arr = [P, 35, 30, 45, 10]
    for par in arr:
        #Now calculation for ans
        dS = 1e3*(par/(Tc + TC))
        ans = dS
        print ("V:", par, "A:", ans)
        
print ("problem solved:", prb)



