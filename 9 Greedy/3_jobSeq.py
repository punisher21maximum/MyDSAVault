

def jobs(jobs):
    '''
    T O(n2)
    '''
    # jobs[i] = jobIDs, deadlines, profits

    jobs = sorted(jobs, key=lambda job: job[2], reverse=True)

    maxDeadline = float('-inf')
    for j in jobs:
        maxDeadline = max(maxDeadline, j[1])
    takenJobs = [None] * (maxDeadline+1)
    flag = True
    print(jobs)
    for i in range(len(jobs)):
        # find free slot from last to first
        for slotIdx in range(min(maxDeadline-1, jobs[i][1] - 1), -1, -1):
            if takenJobs[slotIdx] is None:
                takenJobs[slotIdx] = jobs[i][2]
                print(jobs[i])
                break
    print(takenJobs)


jobs([['a', 2, 100],
      ['b', 1, 19],
      ['c', 2, 27],
      ['d', 1, 25],
      ['e', 3, 15]])
