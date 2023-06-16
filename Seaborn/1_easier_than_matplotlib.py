# Youtube: https://www.youtube.com/watch?v=ooqXQ37XHMM

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

sns.get_dataset_names()      # Example datasets

tips = sns.load_dataset("tips")
iris = sns.load_dataset("iris")
titanic = sns.load_dataset("titanic")
planets = sns.load_dataset("planets")


# Scatterplot
plt.figure()
sns.scatterplot(x="tip", y="total_bill", data=tips, hue="day", size="size", palette="YlGnBu")

# Histogram
plt.figure()
sns.histplot(tips["tip"], kde=True, bins=15)

# Distribution plot
plt.figure()
sns.displot(tips["tip"], kde=True, bins=15)

# Bar plot
plt.figure()
sns.barplot(x="sex", y="tip", data=tips, palette="YlGnBu")

# Box plot
plt.figure()
sns.boxplot(x="day", y="total_bill", data=tips, hue="sex", palette="YlGnBu")

# Strip plot
plt.figure()
sns.stripplot(x="day", y="tip", data=tips, hue="sex", palette="YlGnBu", dodge=True)

# Joint plot
plt.figure()
sns.jointplot(x="tip", y="total_bill", data=tips, kind="reg")   # Regression

plt.figure()
sns.jointplot(x="tip", y="total_bill", data=tips, kind="kde", fill=True, cmap="YlGnBu")    # Distribution

# Pair plot
plt.figure()
sns.pairplot(titanic.select_dtypes(["number"]), hue="pclass")   # Plot all (numerical) columns against eachother

# Heatmap 
drop_columns = ['sex', 'embarked', 'class', 'who', 'deck', 'embark_town', 'alive']   # Drop columns with string values
titanic.drop(columns=drop_columns, inplace=True)

plt.figure()
sns.heatmap(titanic.corr(), annot=True, cmap="YlGnBu")  # cmap: "coolwarm", "icefire"

# Clustermap
plt.figure()
sns.clustermap(iris.drop("species", axis=1))

plt.show()