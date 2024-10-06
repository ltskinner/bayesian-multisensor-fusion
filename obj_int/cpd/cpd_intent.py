
from pgmpy.factors.discrete import TabularCPD

from obj_int.bn_vars import (
    RANGE, ALT,
    SPEED,
    OBJ_TYPE,
    INTENT
)
from .cpd_utils import load_tall_cpd


def get_cpd_INTENT():
    cpd_intent_df = load_tall_cpd('./data/cpd_intent.csv')
    cpd_INTENT = TabularCPD(
        variable=INTENT,
        variable_card=3,
        values=[
            cpd_intent_df['cruise'].tolist(),
            cpd_intent_df['attack'].tolist(),
            cpd_intent_df['evade/neut'].tolist(),
        ],
        evidence=[OBJ_TYPE, RANGE, ALT, SPEED],
        evidence_card=[4, 3, 3, 3],
        state_names={
            OBJ_TYPE: ['missile', 'fighter', 'bomber', 'uav'],
            RANGE: ['far', 'med', 'near'],
            ALT: ['high', 'med', 'low'],
            SPEED: ['fast', 'med', 'slow'],
            INTENT: ['cruise', 'attack', 'evade/neut'],
        }
    )
    return cpd_INTENT
