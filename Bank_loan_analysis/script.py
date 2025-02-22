import pandas as pd

df = pd.read_csv("application_data.csv")

# pd.set_option('display.max_info_columns',len(df.columns))
# missing_percentage = df.isnull().sum()*100/len(df)
# missing_percentage = missing_percentage.sort_values(ascending = False)
# text = missing_percentage.to_string()
# print(text)

# target1 = ext_src[(ext_src["TARGET"]==1) & (~ext_src["EXT_SOURCE_1"].isna()) & (~ext_src["EXT_SOURCE_2"].isna()) & (~ext_src["EXT_SOURCE_3"].isna())]
# target0 = ext_src[(ext_src["TARGET"]==0) & (~ext_src["EXT_SOURCE_1"].isna()) & (~ext_src["EXT_SOURCE_2"].isna()) & (~ext_src["EXT_SOURCE_3"].isna())]
# target1.to_csv("target1.csv")
# target0.to_csv("target0.csv")

# median_ext1 = df.loc[df["TARGET"] == 0,"EXT_SOURCE_1"].median()
# df.loc[df["TARGET"] == 0,"EXT_SOURCE_1"] = df.loc[df["TARGET"] == 0,"EXT_SOURCE_1"].fillna(median_ext1)
# median_ext2 = df.loc[df["TARGET"] == 0,"EXT_SOURCE_2"].median()
# df.loc[df["TARGET"] == 0,"EXT_SOURCE_2"] = df.loc[df["TARGET"] == 0,"EXT_SOURCE_2"].fillna(median_ext2)
# median_ext3 = df.loc[df["TARGET"] == 0,"EXT_SOURCE_3"].median()
# df.loc[df["TARGET"] == 0,"EXT_SOURCE_3"] = df.loc[df["TARGET"] == 0,"EXT_SOURCE_3"].fillna(median_ext3)
# print("NaN values replaced for target 0")

# median_ext1 = df.loc[df["TARGET"] == 1,"EXT_SOURCE_1"].median()
# df.loc[df["TARGET"] == 1,"EXT_SOURCE_1"] = df.loc[df["TARGET"] == 1,"EXT_SOURCE_1"].fillna(median_ext1)
# median_ext2 = df.loc[df["TARGET"] == 1,"EXT_SOURCE_2"].median()
# df.loc[df["TARGET"] == 1,"EXT_SOURCE_2"] = df.loc[df["TARGET"] == 1,"EXT_SOURCE_2"].fillna(median_ext2)
# median_ext3 = df.loc[df["TARGET"] == 1,"EXT_SOURCE_3"].median()
# df.loc[df["TARGET"] == 1,"EXT_SOURCE_3"] = df.loc[df["TARGET"] == 1,"EXT_SOURCE_3"].fillna(median_ext3)
# print("NaN values replaced for target 1")

# df.loc[df["FLAG_OWN_CAR"] == "N","OWN_CAR_AGE"] = df.loc[df["FLAG_OWN_CAR"] == "N","OWN_CAR_AGE"].fillna(-1)

# print(df["CODE_GENDER"].unique) 
# df[df["CODE_GENDER"] == "XNA"].to_csv('xna_gender.csv')

# object_var = df.select_dtypes(include = ["object"])
# for col in object_var.columns:
#     print(col)
#     print(object_var[col].unique())
#     print()

