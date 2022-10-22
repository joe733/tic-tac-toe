# Tic Tac Toe


player_1 = 'x'
player_2 = 'o'
print('Player 1 - x')
print('Player 2 - 0')
current_player = int(input("Select Player: "))



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



print_table('0','1','2','3','0','1','2','3','4')