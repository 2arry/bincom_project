from collections import Counter
from statistics import median, variance
from bincom_dev import table_dict

# Flatten the list of colors
all_colors = [color for colors in table_dict.values() for color in colors]

# Count the occurrences of each color
color_counts = Counter(all_colors)

# Find the color with the highest count (mean color)
mean_color = color_counts.most_common(1)[0][0]

# Find the color that is mostly worn throughout the week
most_worn_color = color_counts.most_common(1)[0][0]

# Find the median color
sorted_colors = sorted(all_colors)
median_color = median(sorted_colors)

# Calculate the variance of the colors
color_frequencies = list(color_counts.values())
color_variance = variance(color_frequencies)

# Calculate the probability of picking 'RED' at random
total_colors = len(all_colors)
red_count = color_counts.get('RED', 0)
red_probability = red_count / total_colors

# Print the results
print(f"The mean color is: {mean_color}")
print(f"The color mostly worn throughout the week is: {most_worn_color}")
print(f"The median color is: {median_color}")
print(f"The variance of the colors is: {color_variance}")
print(f"The probability of picking 'RED' at random is: {red_probability}")