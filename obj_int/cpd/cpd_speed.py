
from pgmpy.factors.discrete import TabularCPD

from obj_int.bn_vars import(
    RAD_REL, IR__REL,
    SPEED_RAD, SPEED_IR_,
    SPEED
)
from .cpd_utils import load_wide_cpd


def get_cpd_SPEED_RAD():
    cpd_SPEED_RAD = TabularCPD(
        variable=SPEED_RAD,
        variable_card=3,
        values=[
            [.3],
            [.4],
            [.3],
        ],
        state_names={
            SPEED_RAD: ['fast', 'med', 'slow'],
        }
    )
    return cpd_SPEED_RAD


def get_cpd_SPEED_IR_():
    cpd_SPEED_IR_ = TabularCPD(
        variable=SPEED_IR_,
        variable_card=3,
        values=[
            [.3],
            [.4],
            [.3],
        ],
        state_names={
            SPEED_IR_: ['fast', 'med', 'slow'],
        }
    )
    return cpd_SPEED_IR_


def get_cpd_SPEED():
    cpd_speed_df = load_wide_cpd('./data/cpd_speed.xlsx')
    cpd_SPEED = TabularCPD(
        variable=SPEED,
        variable_card=3,
        values=[
            cpd_speed_df['fast'].tolist(),
            cpd_speed_df['med'].tolist(),
            cpd_speed_df['slow'].tolist(),
        ],
        evidence=[RAD_REL, IR__REL, SPEED_RAD, SPEED_IR_],
        evidence_card=[2, 2, 3, 3],
        state_names={
            RAD_REL: ['reliable', 'not'],
            IR__REL: ['reliable', 'not'],
            SPEED_RAD: ['fast', 'med', 'slow'],
            SPEED_IR_: ['fast', 'med', 'slow'],
            SPEED: ['fast', 'med', 'slow'],
        }
    )
    return cpd_SPEED
