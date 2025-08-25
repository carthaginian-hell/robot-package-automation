# **Data Ingestion**

# read packages.csv
import csv 
from collections import defaultdict
from src.robot_package_automation.package_sorter import sort

filename = "./packages.csv"

def preprocess(datarow):
    '''clean data - return {} for missing values and non-numeric values'''
    processed_row = {}
    try:
        processed_row['Width'] = float(datarow['Width'])
        processed_row['Height'] = float(datarow['Height'])
        processed_row['Length'] = float(datarow['Length'])
        processed_row['Mass'] = float(datarow['Mass'])

        # Validate inputs
        for value in [processed_row['Width'], processed_row['Height'], processed_row['Length'], processed_row['Mass']]:
            if value <= 0:
                #raise ValueError("All measurements must be positive numbers")
                return {}

        return processed_row
    except:
        return {}

with open(filename, 'r') as f:
    raw_data = csv.DictReader(f)

    cleaned_data = []

    for row in raw_data:
        cleaned_row = preprocess(row)
        print(f"{cleaned_row}")
        if cleaned_row:
            cleaned_row['Category'] = sort(cleaned_row['Width'],
                            cleaned_row['Height'],
                            cleaned_row['Length'],
                            cleaned_row['Mass'])
            
            cleaned_data.append(cleaned_row)

# **Data Analysis and Reporting**
total_sorted_packages = len(cleaned_data)

rejected = 0
special = 0
standard = 0

mass_dict = defaultdict(list)
volume_dict = defaultdict(list)
count_dict = defaultdict(int)

categories = ['REJECTED', 'SPECIAL', 'STANDARD']

for row in cleaned_data:
    v = row['Width'] * row['Height'] * row['Length']
    m = row['Mass']

    for category in categories:
        if row['Category'] == category:
            mass_dict[category].append(m)
            volume_dict[category].append(v)
            count_dict[category] += 1

print(f"{total_sorted_packages=}")

for category in categories:

    print(f"Count of {category}: {count_dict[category]}")

    if len(mass_dict[category]) > 0:
        print(f"Avg {category} Mass: {sum(mass_dict[category])/len(mass_dict[category])}")
        print(f"Min {category} Mass: {min(mass_dict[category])}")
        print(f"Max {category} Mass: {max(mass_dict[category])}")
    else:
        print(f"{category} division by zero error: {len(mass_dict[category])=}")

    if len(volume_dict[category]) > 0:
        print(f"Avg {category} Volume: {sum(volume_dict[category])/len(volume_dict[category])}")
        print(f"Min {category} Volume: {min(volume_dict[category])}")
        print(f"Max {category} Volume: {max(volume_dict[category])}")
    else:
        print(f"{category} division by zero error: {len(mass_dict[category])=}")


#**Q&A**

# - Spend a few minutes discussing potential improvements to the solution
#     - How to handle extremely large datasets
#     - Ways to enhance performance further
#     - Additional features that could be added