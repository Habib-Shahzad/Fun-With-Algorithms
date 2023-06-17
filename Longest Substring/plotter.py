
import matplotlib.pyplot as plt
import timeit


def plot(name, random_input_generator, func1, func2):
    def get_execution_time(n, func, input_generator):
        time_taken = timeit.timeit(
            lambda: func(*input_generator(n)), number=20)
        return time_taken

    times_bf = []
    times_dp = []
    iterations = list(range(10, 2000, 100))

    for iteration in iterations:
        time_bf = get_execution_time(iteration, func1, random_input_generator)
        time_dp = get_execution_time(iteration, func2, random_input_generator)

        times_bf.append(time_bf)
        times_dp.append(time_dp)

    plt.plot(iterations, times_bf, label="Brute Force")
    plt.plot(iterations, times_dp, label="Dynamic Programming")
    plt.legend()
    plt.xlabel("Input Size")
    plt.ylabel("Time Taken")
    plt.title(f"{name} - Time Taken")
    plt.savefig(f"{name}-time_taken.png")
