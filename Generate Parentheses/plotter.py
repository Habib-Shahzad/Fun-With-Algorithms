
import matplotlib.pyplot as plt
import timeit


def plot(name, random_input_generator, func1, func2):

    def get_execution_time(n, func):
        time_taken = timeit.timeit(
            lambda: func(*random_input_generator(n)), number=5)
        return time_taken

    times_1 = []
    times_2 = []
    iterations = list(range(10))

    for iteration in iterations:
        time_1 = get_execution_time(iteration, func1)
        time_2 = get_execution_time(iteration, func2)

        times_1.append(time_1)
        times_2.append(time_2)

    plt.plot(iterations, times_1, label="Iterative")
    plt.plot(iterations, times_2, label="Recursive")
    plt.legend()
    plt.xlabel("Input Size")
    plt.ylabel("Time Taken")
    plt.title(f"{name} - Time Taken")
    plt.savefig(f"{name}-time_taken.png")
