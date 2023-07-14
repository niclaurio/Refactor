from datetime import datetime

from matplotlib import pyplot as plt
import version1
import version2
import version3
import version4
import version5
import version6


def get_execution_time(version, i: int,  use_milliseconds: bool) -> float:
    start = datetime.now()
    version.get_primes_lower_n(i)
    end = datetime.now()
    if use_milliseconds:
        return (end - start).total_seconds() * 1000
    return (end - start).total_seconds()


def plot_versions(v1, v2, use_milliseconds: bool = False):
    start = 5*10 ** 2
    jump = 10 ** 3
    end = start + 10 * jump
    v1_values = []
    v2_values = []
    y = list(range(start, end, jump))
    for i in range(start, end, jump):
        v1_values.append(get_execution_time(v1, i, use_milliseconds=use_milliseconds))
        v2_values.append(get_execution_time(v2, i, use_milliseconds=use_milliseconds))
    plt.plot(y, v1_values,color="blue", label="v1")
    plt.plot(y, v2_values, color="red", label="v2")
    plt.legend()
    plt.savefig('version5 vs version6 .png')
    plt.show()



plot_versions(version5, version6)