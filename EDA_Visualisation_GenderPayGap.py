# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 21:06:49 2024

@author: Maja
"""
#####    Data Visualization 
 
###          QUESTIONS

# 0. Import libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick


### 1.	Import Premium and Claim data and merge both data sets into one data.
GGPG_data = pd.read_csv("C:/Users/Maja/Documents/Learning/MS_Projects/Portfolio 2024/GitHub Portfolio/4_Data Visualisation/Glassdoor Gender Pay Gap.csv")

GGPG_data.head(n=20)
print("GGPG_data shape: ", GGPG_data.shape)
GGPG_data.info()
print(list(GGPG_data))


# 2.	BasePay & Bonus by Department, Job Role, Seniority:
# 2.1 By Department: We'll visualize BasePay and Bonus across departments,

# Department by Base Pay
# Set the color palette
sns.set_palette("Paired")

# Create the bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Dept', y='BasePay', data=GGPG_data)

# Add titles and labels
plt.title('Base Pay by Department')
plt.xlabel('Dept')
plt.ylabel('Base Pay')

# Format y-axis with commas
plt.gca().yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{int(x):,}'))

# Rotate x-axis labels
plt.xticks(rotation=45, ha='right')

# Minimal theme
sns.despine()

# Show plot
plt.show()

# Department by Bonus
# Set the color palette
sns.set_palette("Paired")

# Create the bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Dept', y='Bonus', data=GGPG_data)

# Add titles and labels
plt.title('Bonus by Department')
plt.xlabel('Dept')
plt.ylabel('Bonus')

# Format y-axis with commas
plt.gca().yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{int(x):,}'))

# Rotate x-axis labels
plt.xticks(rotation=45, ha='right')

# Minimal theme
sns.despine()

# Show plot
plt.show()

# Box Plot: To compare BasePay across different levels of Seniority

# Set the color palette
sns.set_palette("Paired")

# Create the box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Seniority', y='BasePay', data=GGPG_data, hue='Seniority')

# Add titles and labels
plt.title('BasePay by Seniority Level')
plt.xlabel('Seniority Level')
plt.ylabel('BasePay')

# Show plot
plt.show()

# Box Plot: To compare Bonus across different levels of Seniority
# Set the color palette
sns.set_palette("Paired")

# Create the box plot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Seniority', y='Bonus', data=GGPG_data, hue='Seniority')

# Add titles and labels
plt.title('Bonus by Seniority Level')
plt.xlabel('Seniority Level')
plt.ylabel('Bonus')

# Move the legend to the top right outside the plot
plt.legend(title='Seniority', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show plot
plt.tight_layout()  # Adjust layout to ensure everything fits without overlap
plt.show()

# 2.2	By Job Role: We'll then explore the BasePay and Bonus distribution across different job roles.
# Set the color palette
sns.set_palette("Paired")

# Plot 1: BasePay by JobTitle
plt.figure(figsize=(12, 6))
sns.barplot(x='JobTitle', y='BasePay', data=GGPG_data, palette='Paired')
plt.title('Base Pay by Job Title')
plt.xlabel('Job Title')
plt.ylabel('Base Pay')
plt.xticks(rotation=45)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
plt.show()

# Plot 2: Bonus by JobTitle
plt.figure(figsize=(12, 6))
sns.barplot(x='JobTitle', y='Bonus', data=GGPG_data, palette='Paired')
plt.title('Bonus by Job Title')
plt.xlabel('Job Title')
plt.ylabel('Bonus')
plt.xticks(rotation=45)
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
plt.show()

# 3.	Mean BasePay Visualization:
# 3.1	Bar Chart by Department: Calculate the mean BasePay for each department and visualize it with a bar chart, using a palette from R's Color Brewer.
# Calculate mean Base Pay per Department

# Calculate mean Base Pay per Department
mean_BasePay_per_Dept = GGPG_data.groupby('Dept')['BasePay'].mean().reset_index()

# Rename columns for clarity 
mean_BasePay_per_Dept.columns = ['Dept', 'BasePay_avg']

# Set the color palette
sns.set_palette("Paired")

# Plot the bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='Dept', y='BasePay_avg', data=mean_BasePay_per_Dept, palette="Paired")

# Add titles and labels
plt.title('Average Base Pay by Department')
plt.xlabel('Department')
plt.ylabel('Mean of Base Pay')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Apply minimal theme
sns.despine()

# Show plot
plt.tight_layout()  # Adjust the layout to fit everything
plt.show()


# Bonus by Department: Visualize the average Bonus across departments.
# Calculate mean Bonus per Department

mean_Bonus_per_Dept = GGPG_data.groupby('Dept')['Bonus'].mean().reset_index()

# Rename columns for clarity 
mean_Bonus_per_Dept.columns = ['Dept', 'Bonus_avg']

# Set the color palette
sns.set_palette("Paired")

# Plot the bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='Dept', y='Bonus_avg', data=mean_Bonus_per_Dept, palette="Paired")

# Add titles and labels
plt.title('Average Bonus by Department')
plt.xlabel('Department')
plt.ylabel('Mean of Bonus')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Apply minimal theme
sns.despine()

# Show plot
plt.tight_layout()  # Adjust the layout to fit everything
plt.show()

# 3.2 BasePay & Bonus by Department: Visualize the average BasePay and Bonus across departments.

# Step 1: Merge the two datasets
combined_data = pd.merge(mean_BasePay_per_Dept, mean_Bonus_per_Dept, on='Dept')

# Step 2: Pivot the merged dataset from wide to long format
combined_data = combined_data.melt(id_vars='Dept', 
                                   value_vars=['BasePay_avg', 'Bonus_avg'], 
                                   var_name='Pay_Type', 
                                   value_name='Average')

# Step 3: Plot the bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='Dept', y='Average', hue='Pay_Type', data=combined_data, palette="Paired")

# Add titles and labels
plt.title('Average Base Pay and Bonus by Department')
plt.xlabel('Department')
plt.ylabel('Average Pay')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Apply minimal theme
sns.despine()
# Show plot
plt.tight_layout() 
plt.show()

# 3.3	BasePay & Bonus by Job Role: Similarly, visualize the average BasePay and Bonus by job roles.
# Mean of Base Pay & Bonus by Job Role
#  Calculate mean BasePay and Bonus per Job Title
mean_JobRole = GGPG_data.groupby('JobTitle').agg(
    avg_BasePay=('BasePay', 'mean'),
    avg_Bonus=('Bonus', 'mean')
).reset_index()

#  Pivot the DataFrame from wide to long format
mean_JobRole_long = mean_JobRole.melt(
    id_vars='JobTitle', 
    value_vars=['avg_BasePay', 'avg_Bonus'], 
    var_name='Pay_Type2', 
    value_name='Average2'
)

#  Plotting the bar chart
plt.figure(figsize=(12, 6))
sns.barplot(x='JobTitle', y='Average2', hue='Pay_Type2', data=mean_JobRole_long, palette='Paired')

#  Customize the plot
plt.title('Average Base Pay and Bonus by Job Title')
plt.xlabel('Job Title')
plt.ylabel('Average Pay')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
sns.despine()  # Apply minimal theme

# Adjust layout to ensure everything fits
plt.tight_layout()

# Show the plot
plt.show()

# 4.	Gender-Based Pay Visualizations:
# 4.1	BasePay by Gender: Use boxplots to compare the distributions of BasePay across genders.

# Set the color palette
sns.set_palette("Paired")

# Create the boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Gender', y='BasePay', data=GGPG_data, palette='Paired')

# Add titles and labels
plt.title('BasePay Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Base Pay')

# Apply minimal theme
sns.despine()  # Removes the top and right spines for a cleaner look

# Show the plot
plt.show()

# 4.2	Bonus by Gender: Visualize the distribution of Bonus amounts across genders using boxplots.
# Set the color palette
sns.set_palette("Paired")

# Create the boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Gender', y='Bonus', data=GGPG_data, palette='Paired')

# Add titles and labels
plt.title('Bonus Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Bonus')

# Apply minimal theme
sns.despine()  # Removes the top and right spines for a cleaner look

# Show the plot
plt.show()
# 4.3	Scatter Plot: Explore the relationship between BasePay and Bonus, with points coloured by gender.

# Create the plot
plt.figure(figsize=(10, 6))

# Create the scatter plot
plot = sns.scatterplot(data=GGPG_data, x='BasePay', y='Bonus', hue='Gender', alpha=0.7, palette='Paired')

# Add titles and labels
plot.set_title('Scatter Plot of BasePay vs. Bonus by Gender')
plot.set_xlabel('Base Pay')
plot.set_ylabel('Bonus')

# Show the legend
plt.legend(title='Gender')

# Apply a minimal theme
plt.style.use('seaborn-darkgrid')

# Display the plot
plt.show()

# 4.4	Facet Grid: View separate scatter plots for each gender, offering a clear comparison.
# Set the overall aesthetics
sns.set(style="whitegrid")

# Create the scatter plot with facet grid
g = sns.FacetGrid(GGPG_data, col="Gender", height=5, aspect=1)
g.map(sns.scatterplot, "BasePay", "Bonus", alpha=0.7)

# Add titles and labels
g.set_axis_labels("Base Pay", "Bonus")
g.set_titles("Gender: {col_name}")
g.fig.suptitle("BasePay vs. Bonus Faceted by Gender", y=1.05, fontsize=16)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show plot
plt.show()

# 4.5 Violin Plot: Combine the distributions of BasePay and Bonus into a single plot, visualizing differences by gender.
# Melting the data
melted_data = GGPG_data.melt(id_vars='Gender', value_vars=['BasePay', 'Bonus'], var_name='variable', value_name='value')

# Create the figure and subplots
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6), sharey=False)

# Plot for BasePay
sns.violinplot(data=melted_data[melted_data['variable'] == 'BasePay'], x='Gender', y='value', hue='Gender', palette='Paired', ax=axes[0], trim=False)
axes[0].set_title('Distribution of BasePay by Gender')
axes[0].set_xlabel('Gender')
axes[0].set_ylabel('Value')

# Plot for Bonus
sns.violinplot(data=melted_data[melted_data['variable'] == 'Bonus'], x='Gender', y='value', hue='Gender', palette='Paired', ax=axes[1], trim=False)
axes[1].set_title('Distribution of Bonus by Gender')
axes[1].set_xlabel('Gender')
axes[1].set_ylabel('Value')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

# 4.6	Bar Plot: Compare the average BasePay and Bonus between genders using a bar plot.

# Compute average BasePay and Bonus by Gender
mean_pay_bonus = GGPG_data.groupby('Gender').agg(
    BasePay_avg=('BasePay', 'mean'),
    Bonus_avg=('Bonus', 'mean')
).reset_index()

# Melt the data for plotting
mean_pay_bonus_melted = pd.melt(mean_pay_bonus, id_vars='Gender', value_vars=['BasePay_avg', 'Bonus_avg'], var_name='Variable', value_name='Average Value')

# Create the grouped bar plot
plt.figure(figsize=(10, 6))
plot = sns.barplot(data=mean_pay_bonus_melted, x='Gender', y='Average Value', hue='Variable', palette='Paired')

# Add titles and labels
plot.set_title('Average BasePay and Bonus by Gender')
plot.set_xlabel('Gender')
plot.set_ylabel('Average Value')
plot.legend(title='Variable')

# Apply a minimal theme
sns.set_style('whitegrid')

# Show the plot
plt.show()

# 5.	Heat Map Visualizations:
# 5.1	By Job Title and Department: Create a heat map showing the average BasePay by Job Title and Department.
# Compute average BasePay by Dept and JobTitle

# Compute average BasePay by Dept and JobTitle
avgBasePay_Dept_JobTitle = GGPG_data.groupby(['Dept', 'JobTitle']).agg(
    avg_BasePay=('BasePay', 'mean')
).reset_index()

# Pivot the data for heatmap
heatmap_data = avgBasePay_Dept_JobTitle.pivot(index='JobTitle', columns='Dept', values='avg_BasePay')

# Create the heatmap
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(
    heatmap_data,
    cmap='coolwarm',  # Use a gradient from cool to warm colors
    annot=True,       # Show values in the heatmap
    fmt=".1f",        # Format the values
    linewidths=0.5,   # Line width between cells
    cbar_kws={'label': 'Average Base Pay'}  # Color bar label
)

# Set titles and labels
plt.title('Heatmap of Job Title and Department with Average Base Pay')
plt.xlabel('Dept')
plt.ylabel('Job Title')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.tight_layout()
plt.show()

# 5.2	Count of Job Titles by Department: Visualize the count of job titles across departments using a heat map.
# Compute count of JobTitle by Dept
JobTitle_count = GGPG_data.groupby(['Dept', 'JobTitle']).size().reset_index(name='JT_count')

# Pivot the data for heatmap
heatmap_data = JobTitle_count.pivot(index='JobTitle', columns='Dept', values='JT_count')

# Create the heatmap
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(
    heatmap_data,
    cmap='YlGnBu',  # Use a gradient from light to dark green
    annot=True,     # Show counts in the heatmap
    fmt='d',        # Format for integer values
    linewidths=0.5, # Line width between cells
    cbar_kws={'label': 'Count'}  # Color bar label
)

# Set titles and labels
plt.title('Heat Map of Job Title Counts by Department')
plt.xlabel('Department')
plt.ylabel('Job Title')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the plot
plt.tight_layout()
plt.show()

# 5.3	BasePay by Job Title and Gender: Explore the relationship between BasePay, job titles, and gender with a heat map.
# Compute average BasePay by JobTitle and Gender
heatmap_data = GGPG_data.groupby(['JobTitle', 'Gender']).agg(
    BasePay_avg=('BasePay', 'mean')
).reset_index()

# Pivot the data for heatmap
heatmap_pivot = heatmap_data.pivot(index='Gender', columns='JobTitle', values='BasePay_avg')

# Create the heatmap
plt.figure(figsize=(12, 8))
heatmap = sns.heatmap(
    heatmap_pivot,
    cmap='coolwarm',       # Use a gradient color map from yellow to turquoise
    annot=True,            # Show values in the heatmap
    fmt=".1f",            # Format the values
    linewidths=0.5,       # Line width between cells
    cbar_kws={'label': 'Average Base Pay'}  # Color bar label
)

# Set titles and labels
plt.title('Heatmap of Job Title and Gender with Average Base Pay')
plt.xlabel('Job Title')
plt.ylabel('Gender')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Apply a minimal theme
sns.set_style('whitegrid')

# Show the plot
plt.tight_layout()
plt.show()

# 6.	Age Distribution:
# 6.1	Histogram: Obtain a histogram to visualize the distribution of employees' ages.
# Code Example Using matplotlib:
# Create the histogram
plt.figure(figsize=(10, 6))
plt.hist(GGPG_data['Age'], bins=range(20, 100, 5), color='skyblue', edgecolor='black')

# Add titles and labels
plt.title('Distribution of Employee Ages')
plt.xlabel('Age')
plt.ylabel('Count')

# Show the plot
plt.tight_layout()
plt.show()


# Code Example Using seaborn:
# Create the histogram
plt.figure(figsize=(10, 6))
sns.histplot(GGPG_data['Age'], bins=range(20, 100, 5), color='skyblue', edgecolor='black')

# Add titles and labels
plt.title('Distribution of Employee Ages')
plt.xlabel('Age')
plt.ylabel('Count')

# Show the plot
plt.tight_layout()
plt.show()

# 7.	Gender Distribution:
# 7.1	Bar Chart: Display the count of each gender within the dataset.

# Code Example Using matplotlib:
# Count occurrences of each gender
gender_counts = GGPG_data['Gender'].value_counts()

# Create the bar plot
plt.figure(figsize=(8, 6))
plt.bar(gender_counts.index, gender_counts.values, color='lightgreen', edgecolor='black')

# Add titles and labels
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')

# Show the plot
plt.tight_layout()
plt.show()


# Code Example Using seaborn:
# Create a count plot (bar plot of counts)
plt.figure(figsize=(8, 6))
sns.countplot(data=GGPG_data, x='Gender', color='lightgreen', edgecolor='black')

# Add titles and labels
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')

# Show the plot
plt.tight_layout()
plt.show()

# 8.	Education Level Distribution:
# 8.1	Bar Chart: Visualize the count of employees at different education levels using a bar chart.
# Code Example Using matplotlib:
# Count occurrences of each education level
education_counts = GGPG_data['Education'].value_counts()

# Create the bar plot
plt.figure(figsize=(8, 6))
plt.bar(education_counts.index, education_counts.values, color='purple', edgecolor='black')

# Add titles and labels
plt.title('Distribution of Education Levels')
plt.xlabel('Education Level')
plt.ylabel('Count')

# Show the plot
plt.tight_layout()
plt.show()
    
# Code Example Using seaborn:
# Create a count plot (similar to a bar plot of counts)
plt.figure(figsize=(8, 6))
sns.countplot(data=GGPG_data, x='Education', palette='Purples', edgecolor='black')

# Add titles and labels
plt.title('Distribution of Education Levels')
plt.xlabel('Education Level')
plt.ylabel('Count')

# Show the plot
plt.tight_layout()
plt.show()



















































































































