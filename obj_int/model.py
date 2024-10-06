
from pgmpy.models import BayesianNetwork


from obj_int.bn_vars import (
    CONDITIONS, RANGE, ALT,

    CAM_REL, RAD_REL, IR__REL,

    SIZE_CAM, SIZE_RAD,
    SPEED_RAD, SPEED_IR_,
    SIZE, SPEED,

    OBJ_TYPE,

    INTENT
)
from . import cpd


def get_model():
    model = BayesianNetwork(
        [
            # ---------------------------------------
            (CONDITIONS, CAM_REL),
            (CONDITIONS, RAD_REL),
            (CONDITIONS, IR__REL),

            (RANGE, CAM_REL),
            (RANGE, RAD_REL),
            (RANGE, IR__REL),

            (ALT, CAM_REL),
            (ALT, RAD_REL),
            (ALT, IR__REL),

            # ----------------------------------------
            (SIZE_CAM, SIZE),
            (CAM_REL, SIZE),
            (RAD_REL, SIZE),
            (SIZE_RAD, SIZE),

            (SPEED_RAD, SPEED),
            (RAD_REL, SPEED),
            (IR__REL, SPEED),
            (SPEED_IR_, SPEED),

            # -----------------------------------------
            (SIZE, OBJ_TYPE),
            (SPEED, OBJ_TYPE),
            (ALT, OBJ_TYPE),

            # -----------------------------------------
            (OBJ_TYPE, INTENT),
            (SPEED, INTENT),
            (RANGE, INTENT),
            (ALT, INTENT)
        ]
    )
    return model


def add_cpds(model):
    cpd_CONDITIONS = cpd.get_cpd_CONDITIONS()
    cpd_RANGE = cpd.get_cpd_RANGE()
    cpd_ALT = cpd.get_cpd_ALT()

    #---------------------------------------------------------------
    cpd_CAM_REL = cpd.get_cpd_CAM_REL()
    cpd_RAD_REL = cpd.get_cpd_RAD_REL()
    cpd_IR__REL = cpd.get_cpd_IR__REL()

    # -------------------------------------------------------------
    cpd_SIZE_CAM = cpd.get_cpd_SIZE_CAM()
    cpd_SIZE_RAD = cpd.get_cpd_SIZE_RAD()

    cpd_SPEED_RAD = cpd.get_cpd_SPEED_RAD()
    cpd_SPEED_IR_ = cpd.get_cpd_SPEED_IR_()

    # -------------------------------------------------------------
    cpd_SIZE = cpd.get_cpd_SIZE()
    cpd_SPEED = cpd.get_cpd_SPEED()

    # -------------------------------------------------------------
    cpd_OBJ_TYPE = cpd.get_cpd_OBJ_TYPE()
    cpd_INTENT = cpd.get_cpd_INTENT()

    model.add_cpds(
        cpd_CONDITIONS, cpd_RANGE, cpd_ALT,

        cpd_CAM_REL, cpd_RAD_REL, cpd_IR__REL,

        cpd_SIZE_CAM, cpd_SIZE_RAD,
        cpd_SPEED_RAD, cpd_SPEED_IR_,

        cpd_SIZE, cpd_SPEED,

        cpd_OBJ_TYPE,
        cpd_INTENT
    )
    return model

def build_model():
    model = get_model()
    model = add_cpds(model)
    return model
