import pandas as pd

df = pd.read_csv("stretch_exercise_dataset.csv")

columns = list(df.columns)

dataset = {}

for i in range(len(df.index)):
    dataset.update({df.iloc[i, 0]: {key: str(value) for key, value in zip(columns[1:], df.iloc[i, 1:])}})

for key in dataset:
    if dataset[key]['Preparation'] == '0':
        dataset[key]['Preparation'] = 'No preparation available'
        
    if dataset[key]['Execution'] == '0':
        dataset[key]['Execution'] = 'No execution available'

    target_muscles_list = dataset[key]['Target_Muscles']
    synergist_muscles_list = dataset[key]['Synergist_Muscles']

    target_muscles_list = dataset[key]['Target_Muscles'].split(',')
    synergist_muscles_list = dataset[key]['Synergist_Muscles'].split(',')

    if target_muscles_list != [''] and target_muscles_list != ['0']:
        target_muscles_list = [elem.strip() for elem in target_muscles_list if elem != '']
        target_muscles_list = ', '.join(target_muscles_list)
    else:
        target_muscles_list = 'None__'

    if synergist_muscles_list != [''] and synergist_muscles_list != ['0']:
        synergist_muscles_list = [elem.strip() for elem in synergist_muscles_list if elem != '']
        synergist_muscles_list = ', '.join(synergist_muscles_list)
    else:
        synergist_muscles_list = 'None__'

    dataset[key]['Target_Muscles'] = target_muscles_list[:-2]

    dataset[key]['Synergist_Muscles'] = synergist_muscles_list[:-2]


print(dataset)