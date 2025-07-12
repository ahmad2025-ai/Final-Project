#!/usr/bin/env python
# coding: utf-8

# ### Importing the first dataset (math)

# In[31]:


import pandas as pd
student_math=pd.read_csv('/Users/ahmadkhalilghamai/Downloads/student+performance/student/student-mat.csv',sep=';')
student_math.head()


# ### Basic EDA for the Math dataset

# In[34]:


student_math.shape


# In[36]:


student_math.nunique()


# In[38]:


student_math.describe


# In[40]:


student_math.isnull().sum()


# In[42]:


student_math.dtypes


# In[48]:


import mysql.connector

# Connect to MySQL Server 
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ahmad123"
)
cursor = conn.cursor()


# In[ ]:





# In[51]:


# Step 1: Create the database
cursor.execute("CREATE DATABASE IF NOT EXISTS student_data")
print("✅ Database 'student_data' created or already exists.")

# Step 2: Use the database
conn.database = "student_data"

# Step 3: Create the table
create_table_query = """
CREATE TABLE IF NOT EXISTS student_performance (
    school VARCHAR(10),
    sex VARCHAR(10),
    age INT,
    address VARCHAR(10),
    famsize VARCHAR(10),
    Pstatus VARCHAR(10),
    Medu INT,
    Fedu INT,
    Mjob VARCHAR(20),
    Fjob VARCHAR(20),
    reason VARCHAR(20),
    guardian VARCHAR(20),
    traveltime INT,
    studytime INT,
    failures INT,
    schoolsup VARCHAR(10),
    famsup VARCHAR(10),
    paid VARCHAR(10),
    activities VARCHAR(10),
    nursery VARCHAR(10),
    higher VARCHAR(10),
    internet VARCHAR(10),
    romantic VARCHAR(10),
    famrel INT,
    freetime INT,
    goout INT,
    Dalc INT,
    Walc INT,
    health INT,
    absences INT,
    G1 INT,
    G2 INT,
    G3 INT
)
"""
cursor.execute(create_table_query)
print("✅ Table 'student_performance' created successfully.")


# In[53]:


cursor.execute("SELECT COUNT(*) FROM student_performance")
result = cursor.fetchone()
print(f"📊 Number of records in 'student_performance': {result[0]}")


# In[55]:


import pandas as pd
import mysql.connector



# Step 2: Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",       # Replace with your MySQL username
    password="Ahmad123",   # Replace with your MySQL password
    database="student_data"
)
cursor = conn.cursor()

# Step 3: Insert each row
for _, row in student_math.iterrows():
    sql = """
    INSERT INTO student_performance (
        school, sex, age, address, famsize, Pstatus, Medu, Fedu,
        Mjob, Fjob, reason, guardian, traveltime, studytime, failures,
        schoolsup, famsup, paid, activities, nursery, higher,
        internet, romantic, famrel, freetime, goout, Dalc,
        Walc, health, absences, G1, G2, G3
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s, %s)
    """
    values = tuple(row)
    cursor.execute(sql, values)

conn.commit()
print("✅ CSV data inserted successfully.")

# Optional: Check number of rows
cursor.execute("SELECT COUNT(*) FROM student_performance")
print(f"📊 Total records: {cursor.fetchone()[0]}")


# In[57]:


print(df.columns)


# In[59]:


cursor.execute("DELETE FROM student_performance")
conn.commit()
print("🧹 All data deleted from 'student_performance'.")


# In[61]:


conn.close()


# In[63]:


import pandas as pd
student_por=pd.read_csv('/Users/ahmadkhalilghamai/Desktop/Final-Project/student/student-por.csv',sep=';')
student_por.head()


# In[65]:


student_por.shape


# In[67]:


student_por.dtypes


# In[69]:


student_por.nunique()


# In[71]:


student_por.isnull().sum()


# In[73]:


student_por.describe()


# In[75]:


student_por.info()


# In[77]:


import mysql.connector

# Connect to MySQL Server (not to any specific DB yet)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ahmad123"
)
cursor = conn.cursor()

# Step 1: Create the database
cursor.execute("CREATE DATABASE IF NOT EXISTS student_data")
print("✅ Database 'student_data' created or already exists.")

# Step 2: Use the database
conn.database = "student_data"

# Step 3: Create the table
create_table_query = """
CREATE TABLE IF NOT EXISTS student_per_port (
    school VARCHAR(10),
    sex VARCHAR(10),
    age INT,
    address VARCHAR(10),
    famsize VARCHAR(10),
    Pstatus VARCHAR(10),
    Medu INT,
    Fedu INT,
    Mjob VARCHAR(20),
    Fjob VARCHAR(20),
    reason VARCHAR(20),
    guardian VARCHAR(20),
    traveltime INT,
    studytime INT,
    failures INT,
    schoolsup VARCHAR(10),
    famsup VARCHAR(10),
    paid VARCHAR(10),
    activities VARCHAR(10),
    nursery VARCHAR(10),
    higher VARCHAR(10),
    internet VARCHAR(10),
    romantic VARCHAR(10),
    famrel INT,
    freetime INT,
    goout INT,
    Dalc INT,
    Walc INT,
    health INT,
    absences INT,
    G1 INT,
    G2 INT,
    G3 INT
)
"""
cursor.execute(create_table_query)
print("✅ Table 'student_per_port' created successfully.")


# In[79]:


cursor.execute("SELECT COUNT(*) FROM student_per_port")
result = cursor.fetchone()
print(f"📊 Number of records in 'student_per_port': {result[0]}")


# In[81]:


import pandas as pd
import mysql.connector



# Step 2: Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",       # Replace with your MySQL username
    password="Ahmad123",   # Replace with your MySQL password
    database="student_data"
)
cursor = conn.cursor()

# Step 3: Insert each row
for _, row in student_por.iterrows():
    sql = """
    INSERT INTO student_per_port (
        school, sex, age, address, famsize, Pstatus, Medu, Fedu,
        Mjob, Fjob, reason, guardian, traveltime, studytime, failures,
        schoolsup, famsup, paid, activities, nursery, higher,
        internet, romantic, famrel, freetime, goout, Dalc,
        Walc, health, absences, G1, G2, G3
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
              %s, %s, %s, %s, %s, %s)
    """
    values = tuple(row)
    cursor.execute(sql, values)

conn.commit()
print("✅ CSV data inserted successfully.")

# Optional: Check number of rows
cursor.execute("SELECT COUNT(*) FROM student_per_port")
print(f"📊 Total records: {cursor.fetchone()[0]}")


# ### Merging two datasets

# In[ ]:





# In[85]:


merge_cols = [
    "school", "sex", "age", "address", "famsize", "Pstatus",
    "Medu", "Fedu", "Mjob", "Fjob", "reason", "guardian"
]


# In[87]:


# Merge on common demographic columns
joined_df = pd.merge(
    student_math, student_por,
    on=merge_cols,
    suffixes=('_math', '_por'),
    how='inner'  # Only students in both subjects
)


# ### Create Average or Unified Columns

# In[90]:


# Average final grade
joined_df['G3_avg'] = (joined_df['G3_math'] + joined_df['G3_por']) / 2

# Create unified dropout label
joined_df['dropout'] = joined_df['G3_avg'].apply(lambda x: 1 if x <= 9 else 0)


# In[92]:


print(joined_df.shape)
print(joined_df[['G3_math', 'G3_por', 'G3_avg', 'dropout']].head())


# ### Dropout Balance

# In[95]:


import matplotlib.pyplot as plt
import seaborn as sns

# Count & percentage
print(joined_df['dropout'].value_counts())
print(joined_df['dropout'].value_counts(normalize=True))

# Plot
sns.countplot(x='dropout', data=joined_df)
plt.title("Dropout Class Distribution (G3_avg ≤ 9 → dropout)")
plt.xticks([0, 1], ['Not Dropped', 'Dropped'])
plt.ylabel("Number of Students")
plt.show()


# ### Correlation Analysis

# In[97]:


# Select numeric features only
numeric_cols = joined_df.select_dtypes(include='number')

# Correlation with dropout
correlations = numeric_cols.corr()['dropout'].sort_values(ascending=False)
print(correlations)

# Heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(numeric_cols.corr(), annot=True, fmt=".2f", cmap='coolwarm')
plt.title("Correlation Matrix (All Numeric Features)")
plt.show()


# ### Categorical vs Dropout

# In[99]:


# A. Dropout Rate by studytime_math and studytime_por
#. 📉 Low Study Time ⟹ Higher Dropout Risk
#What to look for:

#Students with studytime = 1 (less than 2 hours/week) often show higher dropout rates.
#Could be due to poor time management, lack of motivation, or external responsibilities.
#EDA Clue:


#Takeaway: Promote study skills, after-class support, or parental involvement.
# Bar plots for studytime

sns.barplot(x='studytime_math', y='dropout', data=joined_df)
plt.title('Dropout Rate by Study Time (Math)')
plt.ylabel('Dropout Rate')
plt.show()

sns.barplot(x='studytime_por', y='dropout', data=joined_df)
plt.title('Dropout Rate by Study Time (Portuguese)')
plt.ylabel('Dropout Rate')
plt.show()


# In[100]:


#B. Loop Through All Categorical Features
#Here’s a loop to check multiple categorical variables:
categorical_features = [
    'sex', 'school', 'address', 'famsize', 'Pstatus',
    'Mjob', 'Fjob', 'reason', 'guardian',
    'schoolsup_math', 'famsup_math', 'paid_math',
    'activities_math', 'nursery', 'internet'
]

for col in categorical_features:
    if col in joined_df.columns:
        sns.barplot(x=col, y='dropout', data=joined_df)
        plt.title(f'Dropout Rate by {col}')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


# ### 🥃 1. Alcohol Consumption vs Grades and Dropout

# In[102]:


# Compare Dalc and Walc across dropout and grades
import seaborn as sns
import matplotlib.pyplot as plt

# Alcohol vs G3_avg
sns.boxplot(x='dropout', y='Dalc_math', data=joined_df)
plt.title("Daily Alcohol Consumption by Dropout Status (Math)")
plt.show()

sns.boxplot(x='dropout', y='Walc_por', data=joined_df)
plt.title("Weekend Alcohol Consumption by Dropout Status (Portuguese)")
plt.show()

# Correlation with grades
print(joined_df[['Dalc_math', 'Walc_math', 'G3_math']].corr())
print(joined_df[['Dalc_por', 'Walc_por', 'G3_por']].corr())


# ### 📉 2. Absences vs Dropout

# In[105]:


sns.boxplot(x='dropout', y='absences_math', data=joined_df)
plt.title("Math Absences by Dropout Status")
plt.show()

sns.scatterplot(x='absences_math', y='G3_math', hue='dropout', data=joined_df)
plt.title("Math Grade vs Absences with Dropout Highlight")
plt.show()


# ### 🚻 3. Compare Dropout Trends by Gender

# In[108]:


sns.barplot(x='sex', y='dropout', data=joined_df)
plt.title("Dropout Rate by Gender")
plt.show()
#Insight: You'll likely see:

#High absences → lower grades
#Lower grades → more dropouts


# ### 4. Composite Risk Score (Simple Heuristic)

# In[111]:


#Insight: A well-tuned risk score can help flag students for early intervention.
# Normalize key risk factors
joined_df['absences_norm'] = joined_df['absences_math'] / joined_df['absences_math'].max()
joined_df['failures_norm'] = joined_df['failures_math'] / joined_df['failures_math'].max()
joined_df['low_studytime'] = joined_df['studytime_math'].apply(lambda x: 1 if x == 1 else 0)
joined_df['high_dalc'] = joined_df['Dalc_math'].apply(lambda x: 1 if x >= 3 else 0)

# Composite risk score (weights are illustrative)
joined_df['risk_score'] = (
    0.4 * joined_df['absences_norm'] +
    0.3 * joined_df['failures_norm'] +
    0.2 * joined_df['low_studytime'] +
    0.1 * joined_df['high_dalc']
)

# Inspect relationship
sns.histplot(data=joined_df, x='risk_score', hue='dropout', bins=20, kde=True)
plt.title("Risk Score Distribution by Dropout Status")
plt.show()

# Optional: flag high-risk students
joined_df['high_risk'] = joined_df['risk_score'].apply(lambda x: 1 if x > 0.5 else 0)


# ### Grade Distribution by Gender & Parental Education

# In[113]:


import seaborn as sns
import matplotlib.pyplot as plt

# Gender vs G3_avg
sns.boxplot(x='sex', y='G3_avg', data=joined_df)
plt.title("G3 Average by Gender")
plt.show()

# Mother's education vs G3_avg
sns.boxplot(x='Medu', y='G3_avg', data=joined_df)
plt.title("G3 Average by Mother's Education Level")
plt.xlabel("Mother's Education (0 = none, 4 = higher)")
plt.show()

# Father's education vs G3_avg
sns.boxplot(x='Fedu', y='G3_avg', data=joined_df)
plt.title("G3 Average by Father's Education Level")
plt.xlabel("Father's Education (0 = none, 4 = higher)")
plt.show()


# ## Dropout Rates by Alcohol Use & Absence

# In[117]:


# Daily alcohol use vs dropout
sns.barplot(x='Dalc_math', y='dropout', data=joined_df)
plt.title("Dropout Rate by Daily Alcohol Use (Math)")
plt.ylabel("Dropout Rate")
plt.show()

# Weekly alcohol use vs dropout
sns.barplot(x='Walc_por', y='dropout', data=joined_df)
plt.title("Dropout Rate by Weekend Alcohol Use (Portuguese)")
plt.ylabel("Dropout Rate")
plt.show()

# Absences vs dropout
sns.boxplot(x='dropout', y='absences_math', data=joined_df)
plt.title("Absences vs Dropout (Math)")
plt.xticks([0, 1], ['Not Dropped', 'Dropped'])
plt.show()


# ### Boxplot: G3 vs Study Time

# In[122]:


# Math
sns.boxplot(x='studytime_math', y='G3_math', data=joined_df)
plt.title("G3 Math vs Study Time")
plt.xlabel("Study Time (1=low, 4=high)")
plt.ylabel("Final Grade (G3)")
plt.show()

# Portuguese
sns.boxplot(x='studytime_por', y='G3_por', data=joined_df)
plt.title("G3 Portuguese vs Study Time")
plt.xlabel("Study Time (1=low, 4=high)")
plt.ylabel("Final Grade (G3)")
plt.show()


# # KPI

# #### Average Grade per Subject or Group

# In[127]:


#BY subject
# Already present as G3_math, G3_por, and G3_avg
joined_df['avg_grade'] = joined_df[['G3_math', 'G3_por']].mean(axis=1)


# In[130]:


# By Group (Optional: if you want average grade by gender, etc.)
# Example: average grade by gender (add as new column for lookup)
gender_avg = joined_df.groupby('sex')['avg_grade'].transform('mean')
joined_df['gender_avg_grade'] = gender_avg


# ### At-Risk Student (Custom Rule)
# Define your own risk threshold, for example:
# 
# G3_avg < 10
# or low studytime, high failures, etc.

# In[133]:


# Simple grade-based rule
joined_df['at_risk'] = joined_df['G3_avg'].apply(lambda x: 1 if x < 10 else 0)


# In[135]:


joined_df['risk_score'] = (
    0.4 * (joined_df['absences_math'] / joined_df['absences_math'].max()) +
    0.3 * (joined_df['failures_math'] / joined_df['failures_math'].max()) +
    0.2 * joined_df['studytime_math'].apply(lambda x: 1 if x == 1 else 0) +
    0.1 * joined_df['Dalc_math'].apply(lambda x: 1 if x >= 3 else 0)
)

joined_df['at_risk_custom'] = joined_df['risk_score'].apply(lambda x: 1 if x > 0.5 else 0)


# ### Pass/Fail Status Column

# In[138]:


joined_df['passed'] = joined_df['G3_avg'].apply(lambda x: 1 if x >= 10 else 0)


# ###  Pass Rate by Key Features (Optional as Grouped Data)

# In[141]:


support_pass = joined_df.groupby('schoolsup_math')['passed'].mean().reset_index()
print(support_pass)


#  #### Pass Rate by Mother’s Education:

# In[144]:


medu_pass = joined_df.groupby('Medu')['passed'].mean().reset_index()
print(medu_pass)


# In[146]:


joined_df.columns


# In[148]:


#If we didn't disambiguate column names during the join (e.g., suffixes=('_math', '_por')), some columns may have duplicates or overrides. To keep data clean:

# When merging:
common_columns = [
    'school', 'sex', 'age', 'address', 'famsize', 'Pstatus',
    'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian'
]

joined_df = pd.merge(
    student_math,
    student_por,
    on=common_columns,
    suffixes=('_math', '_por')
)


# In[150]:


import os

# Get path to user's desktop
desktop = os.path.join(os.path.expanduser("~"), "Desktop")

# Full path to output file
output_path = os.path.join(desktop, "joined_student_data.csv")

# Save to CSV
joined_df.to_csv(output_path, index=False)

print(f"File saved to: {output_path}")


# ### 🧪 H1: Students with Low Study Time Are More Likely to Drop Out
# ##### Null (H0): Study time has no effect on dropout.
# ##### Alternative (H1): Students with lower study time are more likely to drop out.

# In[158]:


# df is your joined student‑performance DataFrame
joined_df['G3_avg'] = (joined_df['G3_math'] + joined_df['G3_por']) / 2

# Optional check
print(joined_df[['G3_math', 'G3_por', 'G3_avg']].head())


# In[160]:


import pandas as pd

# df is your joined student-performance DataFrame
# 1) If you already have G3_avg
joined_df['dropout_flag'] = (joined_df['G3_avg'] < 10).astype(int)

# 2) If you *don’t* yet have G3_avg, calculate it first:
# df['G3_avg'] = (df['G3_math'] + df['G3_por']) / 2
# df['dropout_flag'] = (df['G3_avg'] < 10).astype(int)

# Quick check
print(joined_df[['G3_avg', 'dropout_flag']].head())
print(joined_df['dropout_flag'].value_counts())


# In[164]:


import pandas as pd
from scipy.stats import chi2_contingency

# df already contains `studytime_math` (1‑4), `G3_avg`, and `dropout_flag`

# 1 = "<2 hours/week", 2‑4 = higher study times
joined_df['study_low'] = (joined_df['studytime_math'] == 1).astype(int)


# In[166]:


# 2×2 table: rows = low / high study, columns = dropout vs stay
table = pd.crosstab(joined_df['study_low'], joined_df['dropout_flag'])
print("Contingency table\n", table)


# In[168]:


chi2, p, dof, expected = chi2_contingency(table)
print(f"Chi² = {chi2:.2f},  p‑value = {p:.4f},  dof = {dof}")


# ### Interpretation
# ### Because the p‑value (≈ 0.41) is far above the typical α‑level of 0.05, we fail to reject the null hypothesis.
# 
# ### Conclusion: In this sample, there is no statistically significant evidence that students with low study time (< 2 hours / week) drop out more often than students who study longer. Any difference you see in raw percentages is likely due to random variation.

# In[ ]:





# 
# ### 🧪 H2: Weekend Alcohol Use Affects Academic Performance
# ##### Null (H0): Weekend alcohol use has no effect on final grades.
# ##### Alternative (H1): Higher Walc is associated with lower G3_avg.
# Variables:
# Walc (1 to 5)
# G3_avg

# In[179]:


import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

# ── 1. Quick box/violin plot ──────────────────────────────────────────
sns.boxplot(x='Walc_math', y='G3_avg', data=joined_df)
plt.title('G3_avg by Weekend Alcohol Use (Walc_math)')
plt.xlabel('Weekend Alcohol Level (Math)')
plt.ylabel('Average Final Grade')
plt.show()

# ── 2. One‑way ANOVA ──────────────────────────────────────────────────
groups = [grp['G3_avg'].values for name, grp in joined_df.groupby('Walc_math')]
f_stat, p_val = stats.f_oneway(*groups)
print(f"ANOVA  F = {f_stat:.2f}   p‑value = {p_val:.4f}")

# ── 3. Spearman correlation (optional check) ──────────────────────────
rho, spearman_p = stats.spearmanr(joined_df['Walc_math'], joined_df['G3_avg'])
print(f"Spearman ρ = {rho:.3f}   p = {spearman_p:.4f}")


# ### 🧠 Interpretation
# #### ANOVA Result:
# #### The p-value > 0.05 → We fail to reject the null hypothesis. This means there's no strong evidence that group means (i.e., grades across Walc levels) are significantly different.
# 
# #### Spearman Correlation:
# #### The correlation is weak but negative and statistically significant (ρ = –0.117, p < 0.05).
# #### This suggests a slight tendency: as weekend alcohol use increases, average grades tend to decrease.

# ### 🧩 Conclusion
# #### While the group difference (via ANOVA) isn't significant, the correlation shows some weak evidence that students with higher alcohol consumption may perform slightly worse.
# 
# 
# #### There is a weak but statistically significant negative correlation between weekend alcohol use and academic performance, although group-level differences are not strong.”

# In[193]:


import pandas as pd

# Calculate math performance
math_avg = round(joined_df['G3_math'].mean(), 2)
math_pass_rate = round((joined_df['G3_math'] >= 10).sum() / joined_df['G3_math'].count() * 100, 2)
math_fail_rate = round((joined_df['G3_math'] < 10).sum() / joined_df['G3_math'].count() * 100, 2)

# Calculate Portuguese performance
por_avg = round(joined_df['G3_por'].mean(), 2)
por_pass_rate = round((joined_df['G3_por'] >= 10).sum() / joined_df['G3_por'].count() * 100, 2)
por_fail_rate = round((joined_df['G3_por'] < 10).sum() / joined_df['G3_por'].count() * 100, 2)

# Combine results
performance_df = pd.DataFrame({
    'Subject': ['Math', 'Portuguese'],
    'Average Grade': [math_avg, por_avg],
    'Pass Rate (%)': [math_pass_rate, por_pass_rate],
    'Fail Rate (%)': [math_fail_rate, por_fail_rate]
})

performance_df


# In[ ]:




