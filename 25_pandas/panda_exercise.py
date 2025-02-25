import pandas as pd
import numpy as np

# nums = [1, 2, 3, 4,5]
# s = pd.Series(nums)
# print(s)

# fruits = ['Orange','Banana','Mango']
# fruits = pd.Series(fruits, index=[1, 2, 3])
# print(fruits)

# s = pd.Series(10, index = [1, 2, 3])
# print(s)
# s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
# print(s)


# data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
#     'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
# df = pd.DataFrame(data)
# print(df)

# df = pd.read_csv('files/csv_example.csv')
# print(df)
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.columns)
# countries = df['country']
# cities = df['city']
# print(countries)
# print(cities)
# print(len(countries)==len(cities))
# print(countries.describe())
# print(cities.describe())


data = [
    ['Asabeneh', 'Finland', 'Helsink'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
# data = [    
#     ['Male', 73.847017, 241.893563],
#     ['Female', 68.781904, 162.310473],
#     ['Male',74.110105, 212.740856],
#     ['Male', 71.730978, 220.042470],
#     ['Male', 69.881796, 206.349801]
# ]
# df = pd.DataFrame(data, columns=['Gender','Height','Weight'])
df = pd.DataFrame(data)
# print(df)
weights = [74, 78, 69]
df['Weight'] = weights
heights = [173, 175, 169]
df['Height'] = heights
# df['height'] = df['Height'] * 0.01
print(df)

# Using functions makes our code clean, but you can calculate the bmi without one
def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi
    
bmi = calculate_bmi()
df["BMI"] = bmi
# print(bmi)
# df['BMI'] = round(df['BMI'], 1)
birth_year = ['1769', '1985', '1990']
current_year = pd.Series(2020, index=[0, 1,2])
df['Birth Year'] = birth_year
df['Current Year'] = current_year

print(df.Weight.dtype)
print(df['Birth Year'].dtype)

df['Birth Year'] = df['Birth Year'].astype('int')
df['Current Year'] = df['Current Year'].astype('int')
ages = df['Current Year'] - df['Birth Year']
df["Age"] = ages
# print(ages)
print(df)
print(df[df['Age'] < 120])