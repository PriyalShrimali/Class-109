import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

#Javascript :  Array , Python : List
dice_result = []

for i in range(0,1000):
    dice1= random.randint(1,6)
    dice2= random.randint(1,6)
    dice_result.append(dice1+dice2)

#Calculate mean, mode, median
mean= sum(dice_result)/ len(dice_result)
std_deviation = statistics.stdev(dice_result)
median = statistics.median(dice_result)
mode= statistics.mode(dice_result)

print(mean)
print(median)
print(mode)
print(std_deviation)



