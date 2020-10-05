# Star Question
def solve_hanoi_tower_puzzle(N, A, B, C):
    """
    Question: Assume you have N Rings pilled on Tower A like ring1, ring2, ring3, ... ringN where the largest ringN
              will be placed at the very bottom of the Tower, followed by the next largest ringN-1, ringN-2 until
              ring1 that placed at the very top of the Tower.
              Transfer all the rings to Tower C or the Destination Tower via Tower B, the Temporary Tower. In the
              process of transferring the rings you are not allowed to put smaller ring on top of the bigger ring
              at any time.

    Inputs:
        N : Number of rings
        A : Start Tower
        B: Temporary Tower
        C: End Tower, or Destination Tower

    Time Complexity: O(2 ** N)
        Why? For N = 1 >> 1 step >> 2 ** 0
             For N = 2 >> 2 steps w/c is twice the previous steps >> 2 ** 1
             For N = 3 >> 4 steps w/c is twice the previous steps >> 2 ** 2
             For N = 4 >> 8 steps w/c is twice the prevous steps >> 2 ** 3
             For N = 5 >> 16 steps w/c is twcie the prevous steps >> 2 ** 4 .... 2 ** N

             T(N) = T(N - 1) + 1 + T(N - 1)
                  = 2T(N - 1) + 1 # One to move to the Temporary Tower, B, and other to move to the End Tower, C.
    """

    if N == 1:
        a = A.pop()
        C.append(a)
    else:
        # Moving N - 1 rings from ring A to ring B, the Temporary ring
        solve_hanoi_tower_puzzle(N - 1, A, C, B)
        a = A.pop()
        C.append(a)
        solve_hanoi_tower_puzzle(N - 1, B, A, C)

def construct_tower_for_N_rings(N):
    tower = [num for num in range(10, 0, -1)]
    return tower

if __name__ == "__main__":
    print("+++++++++++++++++ for N = 1 Ring +++++++++++++")
    A = construct_tower_for_N_rings(1)
    B, C = [], []
    solve_hanoi_tower_puzzle(1, A, B, C)
    print("N = 1: Tower C: ", C)

    print("+++++++++++++++++ for N = 2 Rings +++++++++++++")
    A = construct_tower_for_N_rings(2)
    B, C = [], []
    solve_hanoi_tower_puzzle(2, A, B, C)
    print("N = 2: Tower C: ", C)

    print("+++++++++++++++++ for N = 3 Rings +++++++++++++")
    A = construct_tower_for_N_rings(3)
    B, C = [], []
    solve_hanoi_tower_puzzle(3, A, B, C)
    print("N = 3: Tower C: ", C)

    print("+++++++++++++++++ for N = 4 Rings +++++++++++++")
    A = construct_tower_for_N_rings(4)
    B, C = [], []
    solve_hanoi_tower_puzzle(4, A, B, C)
    print("N = 3: Tower C: ", C)
