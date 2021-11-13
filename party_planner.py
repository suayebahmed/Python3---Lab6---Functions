
import math

def plan_party(f, c, p):
    total_can = (f + 1) * c
    num_pack = math.ceil(total_can / p)
    extra = (num_pack * p) - total_can

    print(f'{num_pack} {p}-pack(s) needed')
    print(f'{extra} extra can(s)')


def plan_party2(f, c, p):
    total_can = (f + 1) * c
    num_pack = math.ceil(total_can / p)
    return num_pack


friend = int(input('How many friends are you throwing this party for? '))
cans = int(input('How many cans will each person drink? '))
pack = int(input('How many cans are in each pack? '))

plan_party(friend, cans, pack)
return_value = plan_party2(friend, cans, pack)

print(f'Return value from plan_party2: {return_value}')
