"""
Based on chapter 3.3 in book:

"Ace you next coding interview by Learning Algorithms"
by Kulikov, Pevzner
"""


def hanoi_towers(n, from_peg, to_peg, total_moves):
    total_moves[0] += 1
    if n == 1:
        return
    unused_peg = 6 - from_peg - to_peg
    hanoi_towers(n - 1, from_peg=from_peg, to_peg=unused_peg, total_moves=total_moves)
    hanoi_towers(n - 1, from_peg=unused_peg, to_peg=to_peg, total_moves=total_moves)
