print("PHYSICS FORMULA CALCULATOR FOR MECHANICS")

print("what do you want to calculate?")
print("1) velocity at time t")
print("2) displacement at time t")
print("3) velocity after s displacement")
print("4) force on an object")
print("5) Potential energy of object at height h")
print("6) Momentum")
print("7)Kinetic Energy")
print("8)Work Done")
print("9)Power")
print("10)Density")
print("11)Pressure")
print("12)Average speed")
print("13)Gravitational force")
print("14)Angular velocity")
print("15)Centripetal force")
print("16) Weight")
print("17) Acceleration")
print("18) Impulse")
print("19) Torque")
print("20) Escape Velocity")

q = int(input("Choose one option="))
print("enter all values in SI unit")

if q==1:
    u=float(input("enter initial velocity, u="))
    a=float(input("enter acceleration, a="))
    t=float(input("enter time, t="))

    v=u+a*t

    print("velocit =", v,"m/s")

elif q==2:
    u=float(input("enter initial velocity, u="))
    a=float(input("enter acceleration, a="))
    t=float(input("enter time, t="))

    s=u*t + (0.5)*(a*t**2.0)

    print("displacemt =", s,"m")

elif q==3:
    u = float(input("enter initial velocity, u="))
    a = float(input("enter acceleration, a="))
    s = float(input("enter displacement, s="))

    value = u**2 + 2*a*s

    if value < 0:
        print("No real solution exists.")
    else:
        v = value**0.5
        print("velocity is", v, "m/s")

elif q==4:
    m=float(input("enter mass, m="))
    a=float(input("enter acceleration, a="))

    f= m*a

    print("force =", f,"N")

elif q==5:
    m=float(input("enter mass, m="))
    h=float(input("enter height of object"))

    g = 9.8

    PE= m*g*h

    print("potential energy of object =", PE,"J")

elif q==6:
    m=float(input("enter mass, m="))
    v=float(input("enter velocity, v="))

    p= m*v

    print("momentum = ", p, "kg m/s")

elif q == 7:
    m = float(input("Enter mass, m = "))
    v = float(input("Enter velocity, v = "))

    ke = 0.5 * m * v**2

    print("Kinetic Energy =", ke, "J")

elif q == 8:
    f = float(input("Enter force, F = "))
    s = float(input("Enter displacement, s = "))

    w = f * s

    print("Work Done =", w, "J")

elif q == 9:
    w = float(input("Enter work done, W = "))
    t = float(input("Enter time, t = "))

    if t == 0:
        print("Time cannot be zero.")
    else:
        p = w / t
        print("Power =", p, "W")

elif q == 10:
    m = float(input("Enter mass, m = "))
    V = float(input("Enter volume, V = "))

    if V == 0:
        print("Volume cannot be zero.")
    else:
        rho = m / V
        print("Density =", rho, "kg/m^3")

elif q == 11:
    F = float(input("Enter force, F = "))
    A = float(input("Enter area, A = "))

    if A == 0:
        print("Area cannot be zero.")
    else:
        P = F / A
        print("Pressure =", P, "Pa")

elif q == 12:
    d = float(input("Enter distance = "))
    t = float(input("Enter time = "))

    if t == 0:
        print("Time cannot be zero.")
    else:
        avg_speed = d / t
        print("Average Speed =", avg_speed, "m/s")

elif q == 13:
    G = 6.674* 10**-11

    m1 = float(input("Enter first mass = "))
    m2 = float(input("Enter second mass = "))
    r = float(input("Enter distance between masses = "))

    F = G * m1 * m2 / r**2

    print("Gravitational Force =", F, "N")

elif q == 14:
    theta = float(input("Enter angular displacement (rad) = "))
    t = float(input("Enter time = "))

    if t == 0:
        print("Time cannot be zero.")
    else:
        omega = theta / t
        print("Angular Velocity =", omega, "rad/s")

elif q == 15:
    m = float(input("Enter mass = "))
    v = float(input("Enter velocity = "))
    r = float(input("Enter radius = "))

    if r == 0:
        print("Radius cannot be zero.")
    else:
        F = m * v**2 / r
        print("Centripetal Force =", F, "N")

elif q == 16:
    m = float(input("Enter mass, m = "))

    g = 9.8

    Fg = m * g

    print("Weight =", Fg, "N")

elif q == 17:
    u = float(input("Enter initial velocity, u = "))
    v = float(input("Enter final velocity, v = "))
    t = float(input("Enter time, t = "))

    if t == 0:
        print("Time cannot be zero.")
    else:
        a = (v - u) / t

        print("Acceleration =", a, "m/s^2")

elif q == 18:
    F = float(input("Enter force, F = "))
    t = float(input("Enter time, t = "))

    J = F * t

    print("Impulse =", J, "N·s")

elif q == 19:
    r = float(input("Enter lever arm distance, r = "))
    F = float(input("Enter force, F = "))

    tau = r * F

    print("Torque =", tau, "N·m")

elif q == 20:
    G = 6.674* 10**-11

    M = float(input("Enter mass of planet, M = "))
    R = float(input("Enter radius of planet, R = "))

    if R == 0:
        print("Radius cannot be zero.")
    else:
        ve = (2 * G * M / R) ** 0.5

        print("Escape Velocity =", ve, "m/s")

else:
    print("invalid value!")




