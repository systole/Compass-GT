import random
import string

#could be (string.ascii_uppercase + string.digits)
def n_num_gen(size, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#example 
# AC#103,N65437,2%,8h,VFR,02:08:06,05:37:05,95,R,7574,KHZL,06:08:06,09:37:05,85,R,7575,KPXE
# AC#108,N89069,97%,12h,IFR,12:27:36,17:29:33,210,R,4230,MMTC,18:27:36,23:29:33,200,R,4231,KBUR

#Generates a line of AI traffic flightplan(s) for inclusion in a .bgl file
def generate_traffic(flightplans, ac_lo, ac_hi):
    from random import getrandbits
    nav = "IFR" if not getrandbits(1) else "VFR"
    x = 1
    while x < flightplans:
        print("AC#" + str(random.randrange(ac_lo, ac_hi, 1)) + ",N"
            + n_num_gen(5) + "," + str(random.randrange(1, 100, 1))
            + "%" + str(random.randrange(2, 24, 2)) + 'h,' + nav)
        x+=1