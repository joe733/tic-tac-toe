# Tic Tac Toe

def play(cur_player,aa,ab,ac,ba,bb,bc,ca,cb,cc):
    print(f'\n{cur_player}:')
    print_table(aa,ab,ac,ba,bb,bc,ca,cb,cc)
    place_coin(int(input("Enter the location:")))
    print_table(aa,ab,ac,ba,bb,bc,ca,cb,cc)




def print_table(aa,ab,ac,ba,bb,bc,ca,cb,cc) -> None:
    # print table
    print(
        """
                |       |
          {aa}  | {ab}  | {ac}
         _______|_______|_______
                |       |
          {ba}  | {bb}  | {bc}
         _______|_______|_______
                |       |
          {ca}  | {cb}  | {cc}
                |       |
        """.format(
            aa=aa.ljust(2).rjust(4), ab=ab.ljust(2).rjust(4), ac=ac.ljust(2).rjust(4),
            ba=ba.ljust(2).rjust(4), bb=bb.ljust(2).rjust(4), bc=bc.ljust(2).rjust(4),
            ca=ca.ljust(2).rjust(4), cb=cb.ljust(2).rjust(4), cc=cc.ljust(2).rjust(4),
        )
    )



# print_table('0','1','2','3','0','1','2','3','4')

player_1 = 'x'
player_2 = 'o'
print('Player 1 - x')
print('Player 2 - o')
temp = int(input("Select Player: "))
coins=['x','y']
if(temp=="1"):
    cur_player=player_1
else:
    cur_player=player_2

while True:
    play(cur_player,aa,ab,ac,ba,bb,bc,ca,cb,cc)
    if hasone():
        print(cur_player)
        exit()  

aa='1'
ab='2'
ac='3'
ba='4'
bb='5'
bc='6'
ca='7'          
cb='8'
cc='9'