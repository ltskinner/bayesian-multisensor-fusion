
from pgmpy.factors.discrete import TabularCPD

from .cpd_utils import load_wide_cpd


from obj_int.bn_vars import (
    CONDITIONS, RANGE, ALT,

    CAM_REL, RAD_REL, IR__REL
)


def get_cpd_CAM_REL():
    cam_rel_df = load_wide_cpd('./data/cpd_cam_rel.xlsx')
    cpd_CAM_REL = TabularCPD(
        variable=CAM_REL,
        variable_card=2,
        values=[
            cam_rel_df['reliable'].tolist(),
            cam_rel_df['not'].tolist(),
        ],
        evidence=[CONDITIONS, RANGE, ALT],
        evidence_card=[2, 3, 3],
        state_names={
            CONDITIONS: ['clear', 'inclement'],
            RANGE: ['far', 'med', 'near'],
            ALT: ['high', 'med', 'low'],
            CAM_REL: ['reliable', 'not'],
        }
    )
    return cpd_CAM_REL


def get_cpd_RAD_REL():
    rad_rel_df = load_wide_cpd('./data/cpd_rad_rel.xlsx')
    cpd_RAD_REL = TabularCPD(
        variable=RAD_REL,
        variable_card=2,
        values=[
            rad_rel_df['reliable'].tolist(),
            rad_rel_df['not'].tolist(),
        ],
        evidence=[CONDITIONS, RANGE, ALT],
        evidence_card=[2, 3, 3],
        state_names={
            CONDITIONS: ['clear', 'inclement'],
            RANGE: ['far', 'med', 'near'],
            ALT: ['high', 'med', 'low'],
            RAD_REL: ['reliable', 'not'],
        }
    )
    return cpd_RAD_REL


def get_cpd_IR__REL():
    ir_rel_df = load_wide_cpd('./data/cpd_ir_rel.xlsx')
    cpd_IR__REL = TabularCPD(
        variable=IR__REL,
        variable_card=2,
        values=[
            ir_rel_df['reliable'].tolist(),
            ir_rel_df['not'].tolist(),
        ],
        evidence=[CONDITIONS, RANGE, ALT],
        evidence_card=[2, 3, 3],
        state_names={
            CONDITIONS: ['clear', 'inclement'],
            RANGE: ['far', 'med', 'near'],
            ALT: ['high', 'med', 'low'],
            IR__REL: ['reliable', 'not'],
        }
    )
    return cpd_IR__REL
