from Version1 import get_primes_lower_n as v1
from Version2 import get_primes_lower_n as v2
from Version3 import get_primes_lower_n as v3
from Version4 import get_primes_lower_n as v4
from plot import plot_time_execution


plot_time_execution(v1, v2, [i for i in range(5000, 100000, 5000)], plot_title='Version1VsVersion2.png')
plot_time_execution(v2, v3, [i for i in range(250000, 5000000, 250000)], plot_title='Version2VsVersion3.png')
plot_time_execution(v3, v4, [i for i in range(5000000, 100000000, 5000000)], plot_title='Version3VsVersion4.png')
