def dfs(problem):
    frontier = [problem.initial_state]
    explored = set()

    while frontier:
        state = frontier.pop()

        if problem.goal_test(state):
            return state

        explored.add(state)

        for child in problem.successors(state):
            if child not in explored:
                frontier.append(child)

    return None
