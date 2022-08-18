import random as rand
import numpy as np #not used

pick = [0,0,0]
result = ['lose','win','lose'];

print('masukan berapa kali iterasi');
t = int(input());
print(t);
win = 0;
lose= 0;
for x in range (t):
    rand.shuffle(result);
    winner_on_unpicked=0;
    for y in range (1,3):
        if result[y] == 'win':
            pick[y]='tochoose';
            winner_on_unpicked = 1;
        else:
            pick[y] = 'openlose'
    print(x);
    print(result);
    print(pick);
    if winner_on_unpicked==0:
        final_pick = rand.randint(1, 2);
    else:
        final_pick = pick.index('tochoose');
    if result[final_pick]=='win':
        print('you win!!');
        win=win+1;
        print(win);
        print("\n");
    else:
        print('you lose!!');
        lose = lose + 1;
        print(lose);
        print("\n");
print('hasil akhir\n');
print(win);
print("\n");
print(lose);








