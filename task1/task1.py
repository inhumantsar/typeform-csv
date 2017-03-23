import requests
import pandas
import numpy


def get_values_or_nan(data, keys):
    return [data[k] if k in data.keys() else numpy.NaN for k in keys]


def get_all_typeforms(apikey):
    '''
    get all typeforms available with the api key provided
    
    params
        apikey    - string. required.
    
    returns
        list of dicts. eg: {'id':'SoMeID', 'name': 'Some Name'}
    '''
    url = "https://api.typeform.com/v1/forms?key={}".format(apikey)
    return requests.get(url).json()


def get_typeform_data(apikey, form_id=None):
    '''
    get a python object representing all of the info available 
    for a particular form.
    
    params
        apikey    - string. required.
        form_id   - string. default: first form returned 
                    by get_all_typeforms()
    
    '''
    if not form_id:
        forms = get_all_typeforms(apikey)
        if len(forms) < 1:
            raise ValueError('no forms found. bad apikey?')

        form_id = forms[0]['id']
    url = "https://api.typeform.com/v1/form/{}?key={}".format(form_id, apikey)
    
    return requests.get(url).json()


def get_responses_csv(apikey, form_id=None):
    '''
    returns form responses as a CSV

    params
        apikey    - string. required.
        form_id   - string. default: first form returned 
                    by get_all_typeforms()
   
    returns
        UTF-8 encoded string formatted as a CSV
    '''
    # load and checks
    data = get_typeform_data(apikey, form_id)
    if 'responses' not in data.keys() or len(data['responses']) < 1:
        raise ValueError('no responses found, aborting.')

    # fetch column names
    # assumption: all metadata objs are created with the same fields
    metadata_fields = list(data['responses'][0]['metadata'].keys())
    question_ids = [i['id'] for i in data['questions']]
    question_texts = [i['question'] for i in data['questions']]

    # init table
    cols = ['user_token'] + question_texts + metadata_fields
    table = pandas.DataFrame(columns=cols)

    for response in data['responses']:
        # add user token column data
        row = [response['token']]

        # add response answers
        row += get_values_or_nan(response['answers'], question_ids)

        # add response metadata
        row += get_values_or_nan(response['metadata'], metadata_fields)

        table = table.append(pandas.DataFrame([row], columns=cols))

    return table.set_index('user_token').to_csv(encoding='utf-8', na_rep='NaN')
