
from pgmpy.factors.discrete import TabularCPD

from obj_int.bn_vars import (
    CONDITIONS, RANGE, ALT
)

def get_cpd_CONDITIONS():
    cpd_CONDITIONS = TabularCPD(
        variable=CONDITIONS,
        variable_card=2,
        values=[
            [.75],
            [.25],
        ],
        state_names={
            CONDITIONS: ['clear', 'inclement'],
        }
    )
    return cpd_CONDITIONS

def get_cpd_RANGE():
    cpd_RANGE = TabularCPD(
        variable=RANGE,
        variable_card=3,
        values=[
            [.6],
            [.3],
            [.1],
        ],
        state_names={
            RANGE: ['far', 'med', 'near'],
        }
    )
    return cpd_RANGE

def get_cpd_ALT():
    cpd_ALT = TabularCPD(
        variable=ALT,
        variable_card=3,
        values=[
            [.33],
            [.34],
            [.33],
        ],
        state_names={
            ALT: ['high', 'med', 'low'],
        }
    )
    return cpd_ALT
