
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


model = build_model()
check_result = model.check_model()
print(check_result)


inference_engine = VariableElimination(model)


observations = {
    CONDITIONS: 'inclement',

    SIZE_CAM: 'lg',
    SIZE_RAD: 'sm',

    SPEED_RAD: 'med',
    SPEED_IR_: 'med',

    RANGE: 'near',
    ALT: 'med',
}

result = inference_engine.query(
    variables=[OBJ_TYPE],
    evidence=observations
)
print(result)



result = inference_engine.query(
    variables=[INTENT],
    evidence=observations
)
print(result)


result = inference_engine.query(
    variables=[OBJ_TYPE, INTENT],
    evidence=observations
)
print(result)
