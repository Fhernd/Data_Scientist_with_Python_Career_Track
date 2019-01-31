# EXERCISE:

# Grouping linear regressions by row or column

# Rather than overlaying linear regressions of grouped data in the same plot, we may want to use a grid of subplots.
# The sns.lmplot() accepts the arguments row and/or col to arrangements of subplots for regressions.

# You'll use the automobile dataset again and, this time, you'll use the keyword argument row to display the subplots
# organized in rows. That is, you'll produce horsepower vs. weight regressions grouped by continent of origin in
# separate subplots stacked vertically.


# INSTRUCTIONS:

# - Plot linear regressions of 'hp' (on the y-axis) versus 'weight' (on the x-axis) grouped row-wise by 'origin' from
# DataFrame auto.
# - Use the keyword argument row to group observations with the categorical column 'origin' in subplots organized in
# rows.


# CODE:

# Plot linear regressions between 'weight' and 'hp' grouped row-wise by 'origin'
sns.lmplot(x='weight', y='hp', data=auto, row='origin', palette='Set1')

# Display the plot
plt.show()
