#! /usr/bin/python3

from tkinter import N


def link_name():

    while True:

        link_name=input( "what will be the link name, link name should start with link_ : " )

        if link_name[:5]=='link_':

            shape_name()

            break

        else:

            print("Not a valid answer, try again.")

        

def shape_name():



        num=int(input("What shape you want to use:\n"

        "                      1 = Solid sphere\n"

        "                      2 = Solid cuboid\n"

        "                      3 = Solid cylinder "))

        

        

        if num == 1:

            solid_sphere()  

    

        elif num == 2:

            Solid_cuboid()

        

        elif num == 3:

            Solid_cylinder()



        

def solid_sphere(): 

        global d, e

        print("you choosed Solid sphere, give: mass, radius ")

        while True:

            d=input("now give, mass as decimal number: ")

            try:

                float(d)

                

                break

            except:

                print("Not a valid answer, try again. ")

        e=input("now give, radius as decimal number: ")

        inertia_solid_sphere()



def Solid_cuboid():

    global k, l, m , n

    print("you choosed Solid cuboid, give: width w, height h, depth d, and mass m")

    

    while True:

        

            k=input("now give, width w")

            

            l=input("now give, , height h, ")

            

            m=input("now give, depth d ")

                

            n=input("now give, mass m")

            try:

                int(k)

                int(l)

                int(m)

                int(n)

                break

            except:

                print("Not a valid answer, try again. ")

    inertia_Solid_cuboid()    

def Solid_cylinder():

    global p, r, s

    print("you choosed Solid cylinder, give: radius r, height h and mass m")

    

    while True:

            p=input("you choosed Solid cylinder, give: radius r, ")

            r=input("you choosed Solid cylinder, give: height h ")

            s=input("you choosed Solid cylinder, give: mass m ")

            try:

                int(p)

                int(r)

                int(s)

                break

            except:

                print("Not a valid answer, try again. ")

    inertia_Solid_cylinder()

def inertia_solid_sphere():

    global aa

    aa = 2/5*(float(d)*float(e)**2)





    ask_user()

def inertia_Solid_cuboid():

    

    a = 1/12*(float(n))*((float(l))**2 +(float(m)**2))

    b = 1/12*(float(n))*((float(k))**2 +(float(l)**2))

    c = 1/12*(float(n))*((float(k))**2 +(float(m)**2))

    print(a)

    print(b)

    print(c)

    ask_user()

def inertia_Solid_cylinder():

    x = 1/12*(float(s))*(3*(float(p))**2 + (float(r)**2))

    z= 1/2*(float(s))*(float(p))**2

    print(x)

    print(z)

    ask_user()

def ask_user():

    while True:

        c=input("Do you want to quit, then answer yes if you want to continue answer no: ")

        if c == "yes":

            break

        else:

            continue

    input("give a filename where to save, use .xml ending for filename: ")

    print()

    

    





















  



link_name()

a=('    <link name="link_leg1">\n'

"      <inertial>\n"

f'        <mass value="1.1"/>\n'

f'        <inertia ixx="{aa}" ixy="0.0" ixz="0.0" iyy="{aa}" iyz="0.0" izz="{aa}"/>\n'

"      </inertial>\n"

"      <visual>\n"

"        <geometry>\n"

'          <sphere radius="2.2"/>\n'

"        </geometry>\n"

"      </visual>\n"

"      <collision>\n"

"        <geometry>\n"

'          <sphere radius="2.2"/>\n'

"        </geometry>\n"

"      </collision>\n"

"    </link>\n")



with open("output.xml","a") as file:

    for i in a:

        file.write(i)

