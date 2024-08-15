
####  Data Visualization 

#### Background:
#### The data for analysis is a Glassdoor Gender Pay Gap in which base pay information
#### is provided for each employee for all the roles and departments.

####  QUESTIONS

## 0. Importing packages and libraries:
library(dplyr)
library(ggplot2)
library(RColorBrewer)
library(tidyr)

# 1.	Import the Data: Begin by importing the Glassdoor Gender Pay Gap data.
GGPG_data<-read.csv(file.choose(), header=T)

head(GGPG_data)
dim(GGPG_data)
summary(GGPG_data)

# 2.	BasePay & Bonus by Department, Job Role, Seniority:
# 2.1 By Department: We'll visualize BasePay and Bonus across departments,
#     utilizing a color palette from R’s Color Brewer.

ggplot(GGPG_data, aes(Dept, BasePay, fill = Dept))+
  geom_col()+
  scale_fill_brewer(palette = "Paired") +  
  labs(x = "Dept", y = " Base Pay", title = " Base Pay by Department")+
  theme_minimal()+
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

ggplot(GGPG_data, aes(Dept, Bonus, fill = Dept))+
  geom_col()+
  scale_fill_brewer(palette = "Paired") +  
  labs(x = "Dept", y = " Bonus", title = " Bonus by Department")+
  theme_minimal()+
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Box Plot: To compare BasePay across different levels of Seniority
ggplot(GGPG_data, aes(x = factor(Seniority), y = BasePay, fill = factor(Seniority))) +
  geom_boxplot() +
  labs(title = "BasePay by Seniority Level", x = "Seniority Level", y = "BasePay")

# Box Plot: To compare Bonus across different levels of Seniority
ggplot(GGPG_data, aes(x = factor(Seniority), y = Bonus, fill = factor(Seniority))) +
  geom_boxplot() +
  labs(title = "BasePay by Seniority Level", x = "Seniority Level", y = "BasePay")


# 2.2	By Job Role: We'll then explore the BasePay and Bonus distribution across different job roles.
ggplot(GGPG_data, aes(JobTitle, BasePay, fill = JobTitle))+
  geom_col()+
  scale_fill_brewer(palette = "Paired") +  
  labs(x = "JobTitle", y = " Base Pay", title = " Base Pay by JobTitlet")+
  theme_minimal()+
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

ggplot(GGPG_data, aes(JobTitle, Bonus, fill = JobTitle))+
  geom_col()+
  scale_fill_brewer(palette = "Paired") +  
  labs(x = "JobTitle", y = " Bonus", title = " Bonus by JobTitle")+
  theme_minimal()+
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# 3.	Mean BasePay Visualization:
# 3.1	Bar Chart by Department: Calculate the mean BasePay for each department and visualize it with a bar chart, using a palette from R's Color Brewer.
# Calculate mean Base Pay per Department
mean_BasePay_per_Dept<-GGPG_data%>%
  group_by(Dept)%>%
  summarise(BasePay_avg=mean(BasePay))
mean_BasePay_per_Dept
# checking all colour pallets in the package
dev.off() 
display.brewer.all(colorblindFriendly = TRUE) 
# Plot bar chart of mean Base Pay per Department
ggplot(mean_BasePay_per_Dept, aes(x = Dept, y = BasePay_avg, fill = Dept)) +
  geom_bar(stat = "identity") +
  scale_fill_brewer(palette = "Paired") +  
  labs(x = "Dept", y = "Mean of Base Pay", title = "Average Base Pay by Department")+
  theme_minimal()+
  theme(axis.text.x = element_text(angle = 45, hjust = 1))


# 3.2 BasePay & Bonus by Department: Visualize the average BasePay and Bonus across departments.
# Calculate mean Bonus per Department
mean_Bonus_per_Dept<-GGPG_data%>%
  group_by(Dept)%>%
  summarise(Bonus_avg=mean(Bonus))
mean_Bonus_per_Dept
# Combine the mean base pay and mean bonus datasets into one, pivoting longer
combined_data <- mean_BasePay_per_Dept %>%
  inner_join(mean_Bonus_per_Dept, by = "Dept") %>%
  pivot_longer(cols = c("BasePay_avg", "Bonus_avg"),
               names_to = "Pay_Type",
               values_to = "Average")
head(combined_data)
# 2b ) Base Pay and Bonus by Department
ggplot(combined_data, aes(x = Dept, y = Average, fill = Pay_Type)) +
  geom_bar(stat = "identity", position = "dodge") +
  scale_fill_brewer(palette = "Paired") +
  labs(x = "Department", y = "Average Pay", 
       title = "Average Base Pay and Bonus by Department") +
  theme_minimal()

# 3.3	BasePay & Bonus by Job Role: Similarly, visualize the average BasePay and Bonus by job roles.
# Mean of Base Pay & Bonus by Job Role
mean_JobRole <- GGPG_data %>%
  group_by(JobTitle) %>%
  summarise(avg_BasePay = mean(BasePay),
            avg_Bonus = mean(Bonus))

mean_JobRole_long <- mean_JobRole %>%
  pivot_longer(cols = c("avg_BasePay", "avg_Bonus"),
               names_to = "Pay_Type2",
               values_to = "Average2")
mean_JobRole
mean_JobRole_long

ggplot(mean_JobRole_long, aes(x = JobTitle, y = Average2, fill = Pay_Type2 ))+
  geom_bar(stat = "identity", position = "dodge")+
  scale_fill_brewer(palette = "Paired") +
  labs(x = "Job Title", y = "Average Pay", 
       title = "Average Base Pay and Bonus by Job Title") +
  theme_minimal()+
  theme(axis.text.x = element_text(angle = 45, hjust = 1))
# 4.	Gender-Based Pay Visualizations:
# 4.1	BasePay by Gender: Use boxplots to compare the distributions of BasePay across genders.
ggplot(GGPG_data, aes(x = Gender, y = BasePay, fill = Gender)) +
  geom_boxplot() +
  scale_fill_brewer(palette = "Paired") +
  labs(title = "BasePay Distribution by Gender",
       x = "Gender",
       y = "Base Pay") +
  theme_minimal()
# 4.2	Bonus by Gender: Visualize the distribution of Bonus amounts across genders using boxplots.
ggplot(GGPG_data, aes(x = Gender, y = Bonus, fill = Gender)) +
  geom_boxplot() +
  scale_fill_brewer(palette = "Paired") +
  labs(title = "Bonus Distribution by Gender",
       x = "Gender",
       y = "Bonus") +
  theme_minimal()

# 4.3	Scatter Plot: Explore the relationship between BasePay and Bonus, with points colored by gender.
ggplot(GGPG_data, aes(x = BasePay, y = Bonus, color = Gender)) +
  geom_point(alpha = 0.7) +
  scale_color_brewer(palette = "Paired") +
  labs(title = "Scatter Plot of BasePay vs. Bonus by Gender",
       x = "Base Pay",
       y = "Bonus") +
  theme_minimal()

# 4.4	Facet Grid: View separate scatter plots for each gender, offering a clear comparison.
ggplot(GGPG_data, aes(x = BasePay, y = Bonus)) +
  geom_point(alpha = 0.7) +
  facet_wrap(~Gender) +
  labs(title = "BasePay vs. Bonus Faceted by Gender",
       x = "Base Pay",
       y = "Bonus") +
  theme_minimal()

# 4.5 Violin Plot: Combine the distributions of BasePay and Bonus into a single plot, visualizing differences by gender.
library(reshape2)
# Melting the data to combine BasePay and Bonus into one variable
melted_data <- melt(GGPG_data, id.vars = "Gender", measure.vars = c("BasePay", "Bonus"))

# Violin plot for BasePay and Bonus by Gender
ggplot(melted_data, aes(x = Gender, y = value, fill = Gender)) +
  geom_violin(trim = FALSE) +
  facet_wrap(~variable, scales = "free_y") +
  scale_fill_brewer(palette = "Paired") +
  labs(title = "Distribution of BasePay and Bonus by Gender",
       x = "Gender",
       y = "Value") +
  theme_minimal()

# 4.6	Bar Plot: Compare the average BasePay and Bonus between genders using a bar plot.
mean_pay_bonus <- GGPG_data %>%
  group_by(Gender) %>%
  summarise(BasePay_avg = mean(BasePay),
            Bonus_avg = mean(Bonus))

# Melt the data for ggplot
mean_pay_bonus_melted <- melt(mean_pay_bonus, id.vars = "Gender")

# Grouped bar plot
ggplot(mean_pay_bonus_melted, aes(x = Gender, y = value, fill = variable)) +
  geom_bar(stat = "identity", position = "dodge") +
  scale_fill_brewer(palette = "Paired") +
  labs(title = "Average BasePay and Bonus by Gender",
       x = "Gender",
       y = "Average Value",
       fill = "Variable") +
  theme_minimal()

# 5.	Heat Map Visualizations:
# 5.1	By Job Title and Department: Create a heat map showing the average BasePay by Job Title and Department.
avgBasePay_Dept_JobTitle<-GGPG_data %>%
  group_by(Dept, JobTitle)%>%
  summarise(avg_BasePay = mean(BasePay))
avgBasePay_Dept_JobTitle
# Creating the heat map of Average BasePay by JobTitle and Dept:           
ggplot(avgBasePay_Dept_JobTitle, aes(x = Dept, y = JobTitle, fill = avg_BasePay)) +
  geom_tile(color = "white") +
  labs(x = "Dept", y = "Job Title", title = "Heatmap of Job Title and Department with Average Base Pay") +
  scale_fill_gradientn(colors = c("orange", "lightyellow", "steelblue")) +  # Three-color gradient
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

### --> This heat map would show the distribution of average BasePay or Bonus across different 
## job titles within each department. It could help you identify which departments have higher
## or lower pay for specific job titles.

# 5.2	Count of Job Titles by Department: Visualize the count of job titles across departments using a heat map.
JobTitle_count <- GGPG_data %>%
  group_by(Dept, JobTitle) %>%
  summarise(JT_count = length(JobTitle))
JobTitle_count
ggplot(JobTitle_count, aes(x = JobTitle, y = Dept, fill = JT_count)) +
  geom_tile(color = "white") +  
  geom_text(aes(label = JT_count), size = 4, color = "black") + 
  scale_fill_gradient(low = "lightgreen", high = "darkgreen") +  
  labs(x = "Job Title", y = "Department", fill = "Count",
       title = "Heat Map of Job Title Counts by Department") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))  

# 5.3	BasePay by Job Title and Gender: Explore the relationship between BasePay, job titles, and gender with a heat map.
ggplot(GGPG_data, aes(x = JobTitle, y = Gender, fill = BasePay)) +
  geom_tile(color = "white") +
  labs(x = "Job Title", y = "Dept", title = "Heatmap of Job Title and Department with Job Titles Count") +
  scale_fill_gradient(low = "yellow2", high = "turquoise4")+
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))  

# 6.	Age Distribution:
# 6.1	Histogram: Obtain a histogram to visualize the distribution of employees' ages.
ggplot(GGPG_data, aes(x = Age)) +
  geom_histogram(binwidth = 5, fill = "skyblue", color = "black") +
  labs(title = "Distribution of Employee Ages", x = "Age", y = "Count")

# 7.	Gender Distribution:
# 7.1	Bar Chart: Display the count of each gender within the dataset.
ggplot(GGPG_data, aes(x = Gender)) +
  geom_bar(fill = "lightgreen", color = "black") +
  labs(title = "Gender Distribution", x = "Gender", y = "Count")
# 8.	Education Level Distribution:
# 8.1	Bar Chart: Visualize the count of employees at different education levels using a bar chart.
ggplot(GGPG_data, aes(x = Education)) +
  geom_bar(fill = "purple4", color = "black") +
  labs(title = "Distribution of Education Levels", x = "Education Level", y = "Count")



                                                                                                                                                                                        