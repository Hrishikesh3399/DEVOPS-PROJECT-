import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#CI TEST

# Title: Electric Vehicle Sales Analysis Dashboard

# Loading the dataset (IMPORTANT: relative path for DevOps)
df = pd.read_csv("Electric_Vehicle_Population_Data.csv")

# Title
st.title("Electric Vehicle Sales Analysis Dashboard")

# Dataset Overview
st.header("Dataset Overview")
st.write(df.head())
st.write("Basic Information:")
st.text(df.info())
st.write("Missing Values:")
st.write(df.isnull().sum())
st.write("Summary Statistics:")
st.write(df.describe())

# EV Adoption Trends
st.header("EV Adoption Trends")
fig, ax = plt.subplots(figsize=(10, 5))
sns.histplot(df['Model Year'], bins=20, kde=True, ax=ax)
ax.set_title('Distribution of Model Year')
ax.set_xlabel('Model Year')
ax.set_ylabel('Count')
st.pyplot(fig)

# Popular EV Types
st.header("Popular EV Models & Manufacturers")
fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(
    y=df['Electric Vehicle Type'],
    order=df['Electric Vehicle Type'].value_counts().index,
    ax=ax
)
ax.set_title('Distribution of Electric Vehicle Types')
st.pyplot(fig)

# Top EV Makes
fig, ax = plt.subplots(figsize=(10, 5))
df['Make'].value_counts().nlargest(10).plot(kind='bar', ax=ax)
ax.set_title('Top 10 EV Makes')
ax.set_xlabel('Make')
ax.set_ylabel('Count')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)

# Correlation Heatmap
st.header("Correlation Analysis")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# EV Adoption Over Years
st.header("EV Adoption Over the Years")
fig, ax = plt.subplots(figsize=(10, 5))
df['Model Year'].value_counts().sort_index().plot(kind='line', marker='o', ax=ax)
ax.set_xlabel('Model Year')
ax.set_ylabel('Number of EVs')
ax.grid()
st.pyplot(fig)

# Electric Range vs MSRP
st.header("Electric Range vs Base MSRP")
fig, ax = plt.subplots(figsize=(10, 5))
sns.scatterplot(data=df, x='Electric Range', y='Base MSRP', alpha=0.5, ax=ax)
ax.grid()
st.pyplot(fig)

# MSRP Distribution
st.header("Base MSRP Distribution by Vehicle Type")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=df, x='Electric Vehicle Type', y='Base MSRP', ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)

# Geographic Distribution
st.header("Geographic Distribution of EVs")

fig, ax = plt.subplots(figsize=(8, 8))
df['Electric Vehicle Type'].value_counts().plot.pie(
    autopct='%1.1f%%',
    startangle=90,
    ax=ax
)
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(12, 6))
df['County'].value_counts().nlargest(10).plot(kind='bar', ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(12, 6))
df['City'].value_counts().nlargest(10).plot(kind='bar', ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
st.pyplot(fig)
