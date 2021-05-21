student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas as pd

student_dataframe = pd.DataFrame(student_dict)
print(student_dataframe)

for(index, row) in student_dataframe.iterrows():
    print(row)