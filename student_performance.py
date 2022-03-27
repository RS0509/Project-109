import statistics
import pandas as pd

df = pd.read_csv("StudentsPerformance 2.csv")
reading_score = df["reading score"].to_list()
writing_score = df["writing score"].to_list()
math_score = df["math score"].to_list()

reading_mean = statistics.mean(reading_score)
writing_mean = statistics.mean(writing_score)
math_mean = statistics.mean(math_score)

print("Mean of the reading score is -->", reading_mean)
print("Mean of the writing score is -->", writing_mean)
print("Mean of the math score is -->", math_mean)

reading_median = statistics.median(reading_score)
writing_median = statistics.median(writing_score)
math_median = statistics.median(math_score)

print("Median of the reading score is -->", reading_median)
print("Median of the writing score is -->", writing_median)
print("Median of the math score is -->", math_median)

reading_mode = statistics.mode(reading_score)
writing_mode = statistics.mode(writing_score)
math_mode = statistics.mode(math_score)

print("Mode of the reading score is -->", reading_mode)
print("Mode of the writing score is -->", writing_mode)
print("Mode of the math score is -->", math_mode)

reading_std_dev = statistics.stdev(reading_score)
writing_std_dev = statistics.stdev(writing_score)
math_std_dev = statistics.stdev(math_score)

print("Std Deviation of the reading score is -->", reading_std_dev)
print("Std Deviation of the writing score is -->", writing_std_dev)
print("Std Deviation of the math score is -->", math_std_dev)

first_reading_std_deviation_start, first_reading_std_deviation_end = reading_mean - reading_std_dev, reading_mean + reading_std_dev
second_reading_std_deviation_start, second_reading_std_deviation_end = reading_mean - (2*reading_std_dev), reading_mean + (2*reading_std_dev)
third_reading_std_deviation_start, third_reading_std_deviation_end = reading_mean - (3*reading_std_dev), reading_mean + (3*reading_std_dev)
list_of_data_within_reading_std_deviation_1 = [result for result in reading_score if result > first_reading_std_deviation_start and result < first_reading_std_deviation_end]
list_of_data_within_reading_std_deviation_2 = [result for result in reading_score if result > second_reading_std_deviation_start and result < second_reading_std_deviation_end]
list_of_data_within_reading_std_deviation_3 = [result for result in reading_score if result > third_reading_std_deviation_start and result < third_reading_std_deviation_end]

print("{}% of data lies within first reading std deviation".format(len(list_of_data_within_reading_std_deviation_1)*100.0/len(reading_score)))
print("{}% of data lies within second reading std deviation".format(len(list_of_data_within_reading_std_deviation_2)*100.0/len(reading_score)))
print("{}% of data lies within third reading std deviation".format(len(list_of_data_within_reading_std_deviation_3)*100.0/len(reading_score)))

first_writing_std_deviation_start, first_writing_std_deviation_end = writing_mean - writing_std_dev, writing_mean + writing_std_dev
second_writing_std_deviation_start, second_writing_std_deviation_end = writing_mean - (2*writing_std_dev), writing_mean + (2*writing_std_dev)
third_writing_std_deviation_start, third_writing_std_deviation_end = writing_mean - (3*writing_std_dev), writing_mean + (3*writing_std_dev)
list_of_data_within_writing_std_deviation_1 = [result for result in writing_score if result > first_writing_std_deviation_start and result < first_writing_std_deviation_end]
list_of_data_within_writing_std_deviation_2 = [result for result in writing_score if result > second_writing_std_deviation_start and result < second_writing_std_deviation_end]
list_of_data_within_writing_std_deviation_3 = [result for result in writing_score if result > third_writing_std_deviation_start and result < third_writing_std_deviation_end]

print("{}% of data lies within first writing std deviation".format(len(list_of_data_within_writing_std_deviation_1)*100.0/len(writing_score)))
print("{}% of data lies within second writing std deviation".format(len(list_of_data_within_writing_std_deviation_2)*100.0/len(writing_score)))
print("{}% of data lies within third writing std deviation".format(len(list_of_data_within_writing_std_deviation_3)*100.0/len(writing_score)))

first_math_std_deviation_start, first_math_std_deviation_end = math_mean - math_std_dev, math_mean + math_std_dev
second_math_std_deviation_start, second_math_std_deviation_end = math_mean - (2*math_std_dev), math_mean + (2*math_std_dev)
third_math_std_deviation_start, third_math_std_deviation_end = math_mean - (3*math_std_dev), math_mean + (3*math_std_dev)
list_of_data_within_math_std_deviation_1 = [result for result in math_score if result > first_math_std_deviation_start and result < first_math_std_deviation_end]
list_of_data_within_math_std_deviation_2 = [result for result in math_score if result > second_math_std_deviation_start and result < second_math_std_deviation_end]
list_of_data_within_math_std_deviation_3 = [result for result in math_score if result > third_math_std_deviation_start and result < third_math_std_deviation_end]

print("{}% of data lies within first math std deviation".format(len(list_of_data_within_math_std_deviation_1)*100.0/len(math_score)))
print("{}% of data lies within second math std deviation".format(len(list_of_data_within_math_std_deviation_2)*100.0/len(math_score)))
print("{}% of data lies within third math std deviation".format(len(list_of_data_within_math_std_deviation_3)*100.0/len(math_score)))

