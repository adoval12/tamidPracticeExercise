import pandas as pd

# Question 1
def read_file(file_path):
    df = pd.read_csv(file_path)
    return df

df = read_file('myBoys.csv')
print(df)
print()

#Question 2
print(df["Age"])
print()

#Question 3
def increase_age_by_five(age):
    return age + 5

df["Age"] = df["Age"].apply(increase_age_by_five)
print(df)

#Question 4
Years = ["Senior", "Senior", "Junior", "Junior", "Sophmore"]
df["Current Year"] = Years
print(df)

#Question 5
df["Dog Age"] = df["Age"].apply(lambda x : x * 7)
print(df)

# Question 6
def get_school(major):
    if major in ["Film and TV", "Advertising"]:
        return "COM"
    elif major in ["Computer Science", "English"]:
        return "CAS"
    elif major == "Business Administration":
        return "Questrom"

df["school"] = df["Major"].apply(get_school)
print(df)

# Question 7
df.to_csv("answers.csv")