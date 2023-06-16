import pandas as pd

## Using datatables in Google Colab (sorting columns: looking at .head and .tail values)
# %load_ext google.colab.data_table
# pd.options.display.max_rows = 85       # Allows to view more rows (default = 60)
# pd.options.display.max_columns = 85     # Allows to view more columns (default = 20)

## Read in the data from CSV file in current directory
df = pd.read_csv("survey_results_public.csv", index_col="Respondent")       # Contains the answers for the 85 question survey
schema = pd.read_csv("survey_results_schema.csv", index_col="Column")       # Contains the question for each column

#------------------------------------------------------------------------------------------------------------------------------------#

## Filter by (boolean) masking

easy = df["SurveyEase"] == "Easy"       # 'easy' is a boolean mask (true/false values)
print(easy)

print(df.loc[easy])                     # Apply mask to .loc
print(df.loc[easy, "MainBranch"])       # 2nd value is/are the columns you wish to view


## Filter by OR == | operator

condition1 = df["SurveyEase"] == "Easy" 
condition2 = df["SurveyLength"] == "Appropriate in length"
easy = condition1 | condition2
print(df.loc[easy])


## Examples

high_salary = (df["ConvertedComp"] > 70000)
print(df.loc[high_salary, ["Country", "LanguageWorkedWith", "ConvertedComp"]])

countries = ["United States", "India", "United Kingdom", "Germany", "Canada"]   # use a list combined with the .isin function
filt = df["Country"].isin(countries)
print(df.loc[filt, "Country"])

python = df["LanguageWorkedWith"].str.contains("Python", na=False)              # na=False == excl. null values
print(df.loc[python, "LanguageWorkedWith"])