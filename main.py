import keyboard, os, random

def check(e):
    key = e.event_type + e.name
    return key

print('Введи количество бочонков')
N = int(input('>>'))
MasBarrel = [i for i in range(1, N+1)]
print(MasBarrel)
for i in range(0, N-1):
    keyboard.wait('enter')
    RandBarrel = random.randint(0, len(MasBarrel)-1)
    print(MasBarrel[RandBarrel])
    MasBarrel.pop(RandBarrel)
    if len(MasBarrel) == 1:
        print('\n', MasBarrel[0], sep='')
os.system('pause')