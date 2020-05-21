import  OOP.Robots.Robot as Robot
import  OOP.Robots.Soldier as Soldier
import  OOP.Robots.Spy as Spy

t1000 = Robot.Robot('t1000','soldier',525,2015,['land', 'water'])

t1000.pasport()

print(t1000.get_element)

t4 = Soldier.Soldier('t1000','soldier',525,2015,['land', 'water'],2)
t4.pasport()
print(t4.get_weapon_category)

print()


sp  = Spy.Spy('bond', 'spy',100,2014,['all'], 'saboteur')
sp.pasport()



ls ='abcd!!&{}[[[2344210-=+'
cod =sp.encryption(ls)
print('cod ',cod)

decod = sp.decryption()
print('decod',decod)

print((10**17)%21)

