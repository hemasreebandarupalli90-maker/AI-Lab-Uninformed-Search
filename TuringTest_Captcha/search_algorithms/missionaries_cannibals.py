from problem import Problem

class MissionariesCannibals(Problem):

    def __init__(self):
        super().__init__((3, 3, 1))  # (M_left, C_left, Boat)

    def goal_test(self, state):
        return state == (0, 0, 0)

    def successors(self, state):
        M, C, boat = state
        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
        result = []

        for m, c in moves:
            if boat == 1:
                new_state = (M - m, C - c, 0)
            else:
                new_state = (M + m, C + c, 1)

            if self.is_valid(new_state):
                result.append(new_state)

        return result

    def is_valid(self, state):
        M, C, _ = state
        if M < 0 or C < 0 or M > 3 or C > 3:
            return False
        if M > 0 and C > M:
            return False
        if (3-M) > 0 and (3-C) > (3-M):
            return False
        return True
