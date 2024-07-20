"""
Based on problem 6.9 in book:

"Ace you next coding interview by Learning Algorithms"
by Kulikov, Pevzner

Input (deadline focused):
    d = {1, [j_11, j_12, ...], 2: [j_21, j_22, ...], 3:..}
    - keys contain priority
    - values contain lists of profits of jobs

Output:
    - Order of jobs that maximizes profit and finishes jobs
      on schedule

Approach:
    - Finish job with max profit on its deadline

"""

from collections import OrderedDict


def arg_max(a):
    L = len(a)
    assert L > 0
    m = a[0]
    m_j = 0
    for i in range(L):
        if a[i] > m:
            m = a[i]
            m_j = i
    return m, m_j


def job_schedule_deadline_focused(jobs):
    jobs = OrderedDict(dict(sorted(jobs.items())))
    append_to_end = []
    order = []
    for _, job_profits in jobs.items():
        job_profit, job_idx = arg_max(job_profits)
        order.append(job_profit)
        job_profits.pop(job_idx)
        for remaining_profit in job_profits:
            append_to_end.append(remaining_profit)
    order.extend(append_to_end)
    return order


def job_schedule_profit_focused(jobs):
    pass


if __name__ == "__main__":
    jobs = {3: [15], 1: [20, 25], 2: [50, 30]}
    order = job_schedule_deadline_focused(jobs)
    print(order)
