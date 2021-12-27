m = input ("enter the value of Mass (kg) : ")   
v = input ("enter the  value of velocity (m/s): ")  
t = input ("enter the  value of time (sec): ")  
# a = input ("enter the  value of acceleration: ")   

m = int(m)
v = int(v)
t = int(t)
# a = int(a)

Force = (m*v)/t                      # mass x velocity / time
# Force2 = m*a
print("Force is", Force)
# print("Force2 is", Force2)
