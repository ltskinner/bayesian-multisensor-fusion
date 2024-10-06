
from pgmpy.factors.discrete import TabularCPD

from obj_int.bn_vars import (
    ALT,
    SIZE,
    SPEED,
    OBJ_TYPE
)
from .cpd_utils import load_wide_cpd


def get_cpd_OBJ_TYPE():
    cpd_obj_type_df = load_wide_cpd('./data/cpd_obj_type.xlsx')
    cpd_OBJ_TYPE = TabularCPD(
        variable=OBJ_TYPE,
        variable_card=4,
        values=[
            cpd_obj_type_df['missile'].tolist(),
            cpd_obj_type_df['fighter'].tolist(),
            cpd_obj_type_df['bomber'].tolist(),
            cpd_obj_type_df['uav'].tolist(),
        ],
        evidence=[ALT, SIZE, SPEED],
        evidence_card=[3, 3, 3],
        state_names={
            ALT: ['high', 'med', 'low'],
            SIZE: ['lg', 'med', 'sm'],
            SPEED: ['fast', 'med', 'slow'],
            OBJ_TYPE: ['missile', 'fighter', 'bomber', 'uav'],
        }
    )
    return cpd_OBJ_TYPE
