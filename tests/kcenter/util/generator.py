def next_main(generator):
    step = next(generator)
    solver_state = step[2]
    while not solver_state.is_main():
        step = next(generator)
        solver_state = step[2]
    return step
