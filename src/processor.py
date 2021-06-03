import pandas as pd


def is_vaccine_available(sessions, dose, min_age_limit):
    parameter = 'available_capacity'
    if dose == 1:
        parameter = 'available_capacity_dose1'
    elif dose == 2:
        parameter = 'available_capacity_dose2'
    num_doses = 0
    for session in sessions:
        if session[parameter] > 0 and session['min_age_limit'] <= min_age_limit:
            num_doses += session[parameter]
    return num_doses


class Processor:
    def __init__(self, json):
        df = pd.DataFrame(json['centers'])
        self._df = df

    # Returns list of dictionary
    def filter_vaccine(self, dose=1, min_age_limit=18):
        df = pd.DataFrame()
        for index, data in self._df.iterrows():

            num_doses = is_vaccine_available(data['sessions'], dose, min_age_limit)
            if num_doses > 0:
                dict = {}
                dict['availability'] = num_doses
                dict['min_age_limit'] = data['sessions'][0]['min_age_limit']
                dict['center_id'] = data['center_id']
                dict['name'] = data['name']
                dict['block_name'] = data['block_name']
                dict['vaccine_fees'] = data['vaccine_fees']
                df = df.append(dict, ignore_index=True)
        return df.to_dict('records')
