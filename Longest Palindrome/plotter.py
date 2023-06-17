
import matplotlib.pyplot as plt
import timeit


def plot(name, random_input_generator, func1, func2, func3):

    def get_execution_time(n, func):
        time_taken = timeit.timeit(
            lambda: func(*random_input_generator(n)), number=4)
        return time_taken

    times_1 = []
    times_2 = []
    times_3 = []
    iterations = list(range(10, 1000, 100))

    for iteration in iterations:
        time_1 = get_execution_time(iteration, func1)
        time_2 = get_execution_time(iteration, func2)
        time_3 = get_execution_time(iteration, func3)

        times_1.append(time_1)
        times_2.append(time_2)
        times_3.append(time_3)

    plt.plot(iterations, times_1, label="Approach 1")
    plt.plot(iterations, times_2, label="Approach 2")
    plt.plot(iterations, times_3, label="Approach 3")
    plt.legend()
    plt.xlabel("Input Size")
    plt.ylabel("Time Taken")
    plt.title(f"{name} - Time Taken")
    plt.savefig(f"{name}-time_taken.png")
