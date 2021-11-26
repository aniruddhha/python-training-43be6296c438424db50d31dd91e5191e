
'''
    - start should be greater than 5
    - stop should be less that 50
    - only 2 steps are possible 1 and 2
'''


def sample_runner(start, stop, step):
    if start < 5:
        raise Exception(f'Invalid Start : {start}')
    if stop > 50:
        raise Exception(f'Invalid Stop : {stop}')
    if step not in [1, 2]:
        raise Exception(f'Invalid Step : {step}')

    for i in range(start, stop, step):
        pass


sample_runner(1, 10, 1)
