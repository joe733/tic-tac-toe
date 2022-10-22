# Two player game!
# Author: Jovial Joe Jayarson

from dataclasses import dataclass
import os


@dataclass
class Player:
    one = 'Player 1'
    two = 'Player 2'
    now = one

    def switch(self):
        self.now = self.two if self.now == self.one else self.one

        
player = Player()


@dataclass(frozen=True, slots=True)
class Coin:
    x = 'X'
    o = 'O'

    def __contains__(self, value) -> bool:
        if value in {self.x, self.o}:
            return True
        return False


coin = Coin()


@dataclass
class Table:
    aa = '1'
    ab = '2'
    ac = '3'
    ba = '4'
    bb = '5'
    bc = '6'
    ca = '7'
    cb = '8'
    cc = '9'   

    def place_coin(self, loc: int) -> None:
        if loc not in range(1, 10):
            raise RuntimeError('Location not on board')

        loc_map = {
            1: self.aa, 2: self.ab, 3: self.ac,
            4: self.ba, 5: self.bb, 6: self.bc,
            7: self.ca, 8: self.cb, 9: self.cc,
        }

        if loc_map[loc] in coin:
            raise RuntimeError('Location occupied')

        cn = coin.x if player.now == player.one else coin.o
        
        if loc == 1:
            self.aa = cn
        elif loc == 2:
            self.ab = cn
        elif loc == 3:
            self.ac = cn
        elif loc == 4:
            self.ba = cn
        elif loc == 5:
            self.bb = cn
        elif loc == 6:
            self.bc = cn
        elif loc == 7:
            self.ca = cn
        elif loc == 8:
            self.cb = cn
        elif loc == 9:
            self.cc = cn

    def print_table(self) -> None:
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
                aa=self.aa.ljust(2).rjust(4), ab=self.ab.ljust(2).rjust(4), ac=self.ac.ljust(2).rjust(4),
                ba=self.ba.ljust(2).rjust(4), bb=self.bb.ljust(2).rjust(4), bc=self.bc.ljust(2).rjust(4),
                ca=self.ca.ljust(2).rjust(4), cb=self.cb.ljust(2).rjust(4), cc=self.cc.ljust(2).rjust(4),
            )
        )

    def has_won(self) -> bool:
            """Check if game won!"""    
            if (
                    # horizontal
                    self.aa == self.ab == self.ac in coin
                    or self.ba == self.bb == self.bc in coin
                    or self.ca == self.cb == self.cc in coin
        
                    # vertical
                    or self.aa == self.ba == self.ca in coin
                    or self.ab == self.bb == self.cb in coin
                    or self.ac == self.bc == self.cc in coin
        
                    # diagonal
                    or self.aa == self.bb == self.cc in coin
                    or self.ac ==self. bb == self.ca in coin            
            ):
                return True
            return False



def play():
    print(f'\n{player.now}:')
    table.print_table()
    table.place_coin(int(input('Enter location: ')))
    table.print_table()
    


if __name__ == '__main__':
    print('Player 1 - X\nPlayer 2 - O')

    if not ((ip_plr := input('Select Player [1]: ') or '1') in {'1', '2'}):
        raise RuntimeError('Please select a valid Player')

    player.now = player.one if ip_plr == '1' else player.two
    table = Table()

    while True:
        os.system('clear')
        play()
        if table.has_won():
            print(f'{player.now} has won!')
            break
        player.switch()
    else:
        print('It\'s a draw!')
