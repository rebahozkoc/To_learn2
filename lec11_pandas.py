import pandas as pd

data = {"name": ["Fuat", "Aykut", "Erkut"],
        "midterm":[60, 85, 100],
        "final": [69, 90, 100],
        "attandance": [6,10,10]}

df_bbm101 = pd.DataFrame(data)

print(df_bbm101.head())

print(type(df_bbm101))


names = ['Fuat', 'Aykut', 'Erkut']
midterms = [60, 85, 100]
finals = [69, 90, 100]
attendances = [6, 10, 10]
list_labels = ['name', 'midterm', 'final', 'attendance']
list_cols = [names, midterms, finals, attendances]

zipped = list(zip(list_labels, list_cols))
print(zipped)
data = dict(zipped)
print(data)
print(type(zipped))

df_bbm101 = pd.DataFrame(data)
df_bbm101["total"] = df_bbm101['midterm']*0.3 + \
                     df_bbm101['final']*0.6 +\
                     df_bbm101['attendance']*0.1
print(df_bbm101["total"])


df_bbm101.loc[(df_bbm101["total"] < 70), "grade"] = "D"
df_bbm101.loc[(df_bbm101["total"] >= 70) & (df_bbm101["total"] < 80), "grade"] = "C"
df_bbm101.loc[(df_bbm101["total"] >= 80) & (df_bbm101["total"] < 90), "grade"] = "B"
df_bbm101.loc[(df_bbm101["total"] > 90), "grade"] = "A"

print(df_bbm101.head())
print(df_bbm101[["name", "grade"]])
print(df_bbm101.iloc[:, [0,5]])
print(df_bbm101.iloc[:, [True, False, False, False, False, True]])

print("\n\n\n")
#########################CSV Files###################################
df_bbm101 = pd.read_csv("bbm101.csv", index_col ="name")
print(df_bbm101.loc["Fuat"])
print(df_bbm101.loc[['Aykut', 'Erkut']])
