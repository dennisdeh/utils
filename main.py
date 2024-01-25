"""
Collection of small utils.

Play around with them to see what they do!
"""
import utils.dictionaries.dictionaries as dicts
import utils.filter_columns.filter_columns as filter_columns
import utils.gtdf.generate_test_data as gtdf
import utils.lists.lists as lists
import utils.paths.paths as paths

#%% dictionaries: small utils for working with dictionaries
d = {"A": 1, "B": 2, "C": 3}
# rename key
dict_out1 = dicts.rename_key(d, key_old="A", key_new="new")
# str_to_dict
strng = "{'A': 'Hello World!'}"
string_out1 = dicts.str_to_dict(strng)
# dict_to_str_formatted
string_out2 = dicts.dict_to_str_formatted(d, indent=3)
# dict_first_val
out1 = dicts.dict_first_val(d)
# dict_to_kwarg_str
string_out3 = dicts.dict_to_kwarg_str(d)
# excel to dict
dict_out2 = dicts.excel_to_dict(file="test.xlsx")

#%% gtdf: generate test data frames
df_out1 = gtdf.gdf(n_copies=2)
df_out2 = gtdf.gdf(ratio_nans=0)
df_out3 = gtdf.gdf(ratio_nans=0.01)
df_out4 = gtdf.gdf(ratio_nans=1)

#%% filter_columns: filter columns in data frames
df = gtdf.gdf(n_copies=2)
# filter_target: prepare a target column and drop other columns
df_out5 = filter_columns.filter_target(df, target_col="int")
df_out6 = filter_columns.filter_target(df, target_col="int", list_substrings=["int", "float"])

#%% lists: small utils for working with lists
a = [1, 2, 3, 4]
b = [2, 4, 6]
c = [1, 2, 3]
d = [4, 1, 2, 3]
list_out1 = lists.intersection(a, b)
list_out2 = lists.difference(a, b)
list_out3 = lists.union(a, b)
list_out4 = lists.is_sublist(c, a)
list_out5 = lists.has_same_elements(a, d)

#%% paths: util to choose the correct working directory dynamically
string_out4 = paths.get_project_path("Github")
paths.get_project_path("non_existing_project")
