import numpy as np
import pandas as pd

df = pd.read_csv("bp_loan_task_log (1) (1).csv", sep=";")
df = df.sort_values(by=['task', 'time'])

unique_kind = df.drop_duplicates('kind')
kind_dict = dict(zip(unique_kind['kind'], unique_kind['kindName']))

previous_kind = None
previous_time = None

data = dict()

for index, row in df.iterrows():
    kind = row['kind']
    time = row['time']

    if(previous_kind is not None):
        if previous_kind == 5 or kind == 0:
            previous_kind = kind
            previous_time = time
            continue

        case = (kind_dict[previous_kind], kind_dict[kind])
        dt = time - previous_time
        if data.get(case) is not None:
            data[case]['count_all'] += 1
            data[case]['count_unique'].add(row['task'])
            data[case]['dt'] = np.append(data[case]['dt'], dt)
        else:
            data[case] = {'kindName': kind_dict[previous_kind], 'otherKindName': kind_dict[kind], 'count_all': 1, 
                          'count_unique': set([row['task']]), 'dt': np.array([dt], dtype="int64"), 
                          'dt_min': 0, 'dt_max': 0, 'dt_avg': 0}

        previous_kind = kind
    else:
        previous_kind = kind
        previous_time = time

data_for_csv = {}

for key, i in zip(data.keys(), range(len(data.keys()))):
    data[key]['count_unique'] = len(data[key]['count_unique'])
    data[key]['dt_min'] = np.min(data[key]['dt'])
    data[key]['dt_max'] = np.max(data[key]['dt'])
    data[key]['dt_avg'] = np.mean(data[key]['dt'], dtype='int64')
    data[key].pop('dt')
    data_for_csv[i] = data[key]

newDf = pd.DataFrame.from_dict(data=data_for_csv, orient='index')
newDf.to_csv('table.csv')
print(newDf)
