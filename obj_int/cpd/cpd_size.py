
from pgmpy.factors.discrete import TabularCPD

from obj_int.bn_vars import(
    CAM_REL, RAD_REL,
    SIZE_CAM, SIZE_RAD,
    SIZE
)
from .cpd_utils import load_wide_cpd


def get_cpd_SIZE_CAM():
    cpd_SIZE_CAM = TabularCPD(
        variable=SIZE_CAM,
        variable_card=3,
        values=[
            [.15],
            [.45],
            [.4],
        ],
        state_names={
            SIZE_CAM: ['lg', 'med', 'sm'],
        }
    )
    return cpd_SIZE_CAM


def get_cpd_SIZE_RAD():
    cpd_SIZE_RAD = TabularCPD(
        variable=SIZE_RAD,
        variable_card=3,
        values=[
            [.15],
            [.45],
            [.4],
        ],
        state_names={
            SIZE_RAD: ['lg', 'med', 'sm'],
        }
    )
    return cpd_SIZE_RAD


def get_cpd_SIZE():
    cpd_size_df = load_wide_cpd('./data/cpd_size.xlsx')
    cpd_SIZE = TabularCPD(
        variable=SIZE,
        variable_card=3,
        values=[
            cpd_size_df['lg'].tolist(),
            cpd_size_df['med'].tolist(),
            cpd_size_df['sm'].tolist(),
        ],
        evidence=[CAM_REL, RAD_REL, SIZE_CAM, SIZE_RAD],
        evidence_card=[2, 2, 3, 3],
        state_names={
            CAM_REL: ['reliable', 'not'],
            RAD_REL: ['reliable', 'not'],
            SIZE_CAM: ['lg', 'med', 'sm'],
            SIZE_RAD: ['lg', 'med', 'sm'],
            SIZE: ['lg', 'med', 'sm'],
        }
    )
    return cpd_SIZE

