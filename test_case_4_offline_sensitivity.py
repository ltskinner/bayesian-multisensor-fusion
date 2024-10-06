
import numpy as np
import pandas as pd

from pgmpy.inference import VariableElimination


from obj_int.bn_vars import (
    CONDITIONS, RANGE, ALT,

    CAM_REL, RAD_REL, IR__REL,

    SIZE_CAM, SIZE_RAD,
    SPEED_RAD, SPEED_IR_,
    SIZE, SPEED,

    OBJ_TYPE,

    INTENT
)
from obj_int.model import build_model



def run_trial(observations):
    model = build_model()
    check_result = model.check_model()
    print(check_result)

    inference_engine = VariableElimination(model)

    result = inference_engine.query(
        variables=[OBJ_TYPE],
        evidence=observations
    )
    print(result)



    result = inference_engine.query(
        variables=[INTENT],
        evidence=observations
    )
    #print(result)

    result = inference_engine.query(
        variables=[OBJ_TYPE, INTENT],
        evidence=observations
    )
    """
    print(result)
    print(type(result))

    print(dir(result))

    print(result.variables)
    print(result.values)
    """


    object_types = [
        'missile',
        'fighter',
        'bomber',
        'uav'
    ]
    intent_types = [
        'cruise',
        'attack',
        'evade/neut'
    ]

    ordered_results = []
    for o, object_type in enumerate(object_types):
        for i, intent_type in enumerate(intent_types):
            value = result.values[o][i]
            #print(object_type, intent_type, value)
            ordered_results.append(value)
    
    return ordered_results




def size_variance():
    results_dict = {}

    for _condition in ['inclement', 'clear']:
        for _range in ['far', 'med', 'near']:
            for _alt in ['high', 'med', 'low']:
                for _size in ['lg', 'med', 'sm']:
                    observations_cam = {
                        CONDITIONS: 'inclement',  # FIXED

                        SIZE_CAM: _size,
                        #SIZE_RAD: 'sm',

                        #SPEED_RAD: 'slow',
                        #SPEED_IR_: 'slow',

                        RANGE: _range,       # FIXED
                        ALT: _alt,         # FIXED
                    }

                    ordered_results_cam = run_trial(observations_cam)


                    observations_rad = {
                        CONDITIONS: 'inclement',  # FIXED

                        #SIZE_CAM: 'sm',
                        SIZE_RAD: _size,

                        #SPEED_RAD: 'slow',
                        #SPEED_IR_: 'slow',

                        RANGE: _range,       # FIXED
                        ALT: _alt,         # FIXED
                    }
                    ordered_results_rad = run_trial(observations_rad)

                    print(ordered_results_cam)
                    print(ordered_results_rad)
                    diff = np.diff(np.array([ordered_results_cam, ordered_results_rad]), axis=0)
                    #diff = np.abs(diff)
                    diff = np.round(diff, decimals=6)

                    result_slug = f'{_size}|{_alt}|{_range}|{_condition}'
                    results_dict[result_slug] = diff[0]

    object_intents = [
        'missile, cruise',
        'missile, attack',
        'missile, evade/neut',
        'fighter, cruise',
        'fighter, attack',
        'fighter, evade/neut',
        'bomber, cruise',
        'bomber, attack',
        'bomber, evade/neut',
        'uav, cruise',
        'uav, attack',
        'uav, evade/neut',
    ]

    records = []
    for slug, value_list in results_dict.items():
        for c, diff in enumerate(value_list):
            object_intent = object_intents[c]
            record = {
                'slug': slug,
                'object_intent': object_intent,
                'diff': round(diff*100, 3)
            }
            records.append(record)

    tall_df = pd.DataFrame.from_records(records)
    tall_df.to_csv('./test_case_4_size_tall.csv', index=False)


    """
    result_df = pd.DataFrame(results_dict)
    result_df = result_df*100

    mean_col = result_df.mean(axis=1)
    std_col = result_df.std(axis=1)

    result_df['mean'] = mean_col
    result_df['std'] = std_col

    object_types = [
        'missile',
        'fighter',
        'bomber',
        'uav'
    ]
    intent_types = [
        'cruise',
        'attack',
        'evade/neut'
    ]

    objects_rows = []
    intents_rows = []
    for o, object_type in enumerate(object_types):
        for i, intent_type in enumerate(intent_types):
            objects_rows.append(object_type)
            intents_rows.append(intent_type)
    
    result_df['object'] = objects_rows
    result_df['intent'] = intents_rows

    result_df = result_df[[
        'object', 'intent',
        'mean', 'std'
    ]]



    print(result_df.head())
    result_df.to_csv('./test_case_4_size_variance.csv', index=False)
    """



def speed_variance():
    results_dict = {}

    for _condition in ['inclement', 'clear']:
        for _range in ['far', 'med', 'near']:
            for _alt in ['high', 'med', 'low']:
                for _speed in ['fast', 'med', 'slow']:

                    observations_rad = {
                        CONDITIONS: 'inclement',  # FIXED

                        #SIZE_CAM: _size,
                        #SIZE_RAD: 'sm',

                        SPEED_RAD: _speed,
                        #SPEED_IR_: 'slow',

                        RANGE: _range,       # FIXED
                        ALT: _alt,         # FIXED
                    }
                    ordered_results_rad = run_trial(observations_rad)


                    observations__ir = {
                        CONDITIONS: 'inclement',  # FIXED

                        #SIZE_CAM: _size,
                        #SIZE_RAD: 'sm',

                        #SPEED_RAD: 'slow',
                        SPEED_IR_: _speed,

                        RANGE: _range,       # FIXED
                        ALT: _alt,         # FIXED
                    }

                    ordered_results__ir = run_trial(observations__ir)


                    print(ordered_results__ir)
                    print(ordered_results_rad)
                    diff = np.diff(np.array([ordered_results__ir, ordered_results_rad]), axis=0)
                    #diff = np.abs(diff)
                    diff = np.round(diff, decimals=6)

                    result_slug = f'{_speed}|{_alt}|{_range}|{_condition}'
                    results_dict[result_slug] = diff[0]

    object_intents = [
        'missile, cruise',
        'missile, attack',
        'missile, evade/neut',
        'fighter, cruise',
        'fighter, attack',
        'fighter, evade/neut',
        'bomber, cruise',
        'bomber, attack',
        'bomber, evade/neut',
        'uav, cruise',
        'uav, attack',
        'uav, evade/neut',
    ]

    records = []
    for slug, value_list in results_dict.items():
        for c, diff in enumerate(value_list):
            object_intent = object_intents[c]
            record = {
                'slug': slug,
                'object_intent': object_intent,
                'diff': round(diff*100, 3)
            }
            records.append(record)

    tall_df = pd.DataFrame.from_records(records)
    tall_df.to_csv('./test_case_4_speed_tall.csv', index=False)

    """
    result_df = pd.DataFrame(results_dict)
    result_df = result_df*100

    mean_col = result_df.mean(axis=1)
    std_col = result_df.std(axis=1)

    result_df['mean'] = mean_col
    result_df['std'] = std_col

    object_types = [
        'missile',
        'fighter',
        'bomber',
        'uav'
    ]
    intent_types = [
        'cruise',
        'attack',
        'evade/neut'
    ]

    objects_rows = []
    intents_rows = []
    for o, object_type in enumerate(object_types):
        for i, intent_type in enumerate(intent_types):
            objects_rows.append(object_type)
            intents_rows.append(intent_type)
    
    result_df['object'] = objects_rows
    result_df['intent'] = intents_rows

    result_df = result_df[[
        'object', 'intent',
        'mean', 'std'
    ]]



    print(result_df.head())
    result_df.to_csv('./test_case_4_speed_variance.csv', index=False)
    """


if __name__ == '__main__':

    size_variance()
    speed_variance()



