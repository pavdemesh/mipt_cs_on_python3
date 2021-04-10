def count_traj_allowed(n: int, allowed: list):

    traj = [0, 1, int(allowed[2])] + [0] * (n - 2)
    for i in range(3, n + 1):
        if allowed[i]:
            traj[i] = traj[i - 1] + traj[i - 2] + traj[i - 3]
    return traj[n]


allowed = [False, True, True, True, False, True, True, False, True, True]
print(count_traj_allowed(5, allowed))
