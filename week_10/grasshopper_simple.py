def count_traj(N):
    trajectories = [0, 1] + [0] * (N-1)
    for i in range(2, N+1):
        trajectories[i] = trajectories[i - 1] + trajectories[i - 2]
    return trajectories[N]


print(count_traj(2))
