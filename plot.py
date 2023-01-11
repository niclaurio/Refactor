import matplotlib.pyplot as plt
from datetime import datetime


def plot_time_execution(func1, func2, values, plot_title) -> None:
	"""
	plot used to check which of the 2 given version is faster
	:param func1: oldest version
	:param func2: newest version
	:param values: list of values to give to n in each function
	:param plot_title:
	:return: None
	"""
	old_version_times = []
	new_version_times = []
	for i in values:
		start1 = datetime.now()
		func1(i)
		end1 = datetime.now()
		old_version_times.append((end1 - start1).seconds)
		start2 = datetime.now()
		func2(i)
		end2 = datetime.now()
		new_version_times.append((end2 - start2).seconds)
	print(old_version_times, new_version_times, plot_title)
	plt.plot(values, old_version_times, label='old_version', color='blue')
	plt.plot(values, new_version_times, label='new_version', color='red')
	plt.legend()
	plt.title(" which version is faster?")
	plt.ylabel('execution times')
	plt.savefig(plot_title)


