

import numpy as np
import pandas as pd



size_df_path = './test_case_4_size_tall.csv'
size_df = pd.read_csv(size_df_path)

speed_df_path = './test_case_4_speed_tall.csv'
speed_df = pd.read_csv(speed_df_path)

df = pd.concat([
    size_df,
    speed_df
], ignore_index=True)



records = []
for object_intent, obj_df in df.groupby('object_intent'):
    values = np.absolute(obj_df['diff'])
    mean = round(np.mean(values), 3)
    std = round(np.std(values), 3)

    record = {
        'object_intent': object_intent,
        'mean': mean,
        'std': std
    }
    records.append(record)

mean_std_df = pd.DataFrame.from_records(records)

mean_std_df.to_csv('./test_case_4_combined_mean_std.csv', index=False)

