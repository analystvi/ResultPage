import pandas as pd

def list_of_colleges(mark, course, community, data):
    filtered_data = data[data['Branch Name'].str.contains(course, case=False, na=False) & (data[community] <= mark)]
    result = filtered_data[['College Code', 'College Name', 'Branch Name', community,'PickMyCareer Rank']]
    result = result.sort_values(by=community, ascending=False)
    return result

def filter_colleges(nirf_rank=None, lmes_rank=None, data=None):
    if nirf_rank is not None:
        data = data[data['nirf_rank'] <= nirf_rank]
    if lmes_rank is not None:
        data = data[data['lmes_rank'] <= lmes_rank]
    return data
