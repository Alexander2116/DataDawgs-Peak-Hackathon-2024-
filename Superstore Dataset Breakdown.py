import datetime
import pandas as pd
import matplotlib.pyplot as plt
import ydata_profiling as ydp

data_location = 'Superstore Dataset.xlsx'
df = pd.read_excel(data_location) # creating a pandas dataframe based on given dataset

columns = df.columns.ravel() # list of columns in Superstore Dataset


def get_column_data(df, col): # returns a list with data from each column
    return df[col].tolist() # df = dataframe, col = index of column we're looking at

def get_cat(data_frame, cat_index): # returns list of different possible values given in a column
    genres = []

    for i in get_column_data(data_frame, columns[cat_index]):
        if i in genres:
            pass
        else:
            genres.append(i)

    return genres

def column_comparison(df, a_index, b_index): # returns a dictionary organised by categories and their profits
    prof_by_cat = {} # a dictionary organising profits by categories
    for cat in get_cat(df, a_index):
        prof_by_cat.update({cat: 0})

    a_column = get_column_data(df, columns[a_index])
    b_column = get_column_data(df, columns[b_index])

    for prof in b_column:
        current_cat = a_column[b_column.index(prof)]
        prof_by_cat[current_cat] += prof

    return prof_by_cat


# categories and profits
plt.bar(column_comparison(df, 14, 20).keys(), column_comparison(df, 14, 20).values())
plt.show()

# sub categories and profits
plt.bar(column_comparison(df, 15, 20).keys(), column_comparison(df, 15, 20).values())
plt.show()


# top 3 sales
dictionary = column_comparison(df, 15, 17)
kvs = {}
for i in range(3):
    max_key = max(dictionary, key=dictionary.get)
    kvs[max_key] = dictionary[max_key]
    del dictionary[max_key]

plt.bar(kvs.keys(), kvs.values())
plt.show()


# top 3 profits
dictionary = column_comparison(df, 15, 20)
kvp = {}
for i in range(3):
    max_key = max(dictionary, key=dictionary.get)
    kvp[max_key] = dictionary[max_key]
    del dictionary[max_key]

plt.bar(kvp.keys(), kvp.values())
plt.show()

#kvf = 
#plt.bar(column_comparison(df, 16, 20).keys(), column_comparison(df, 16, 20).values())
#plt.show()