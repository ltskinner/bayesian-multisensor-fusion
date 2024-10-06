
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


result = inference_engine.query(
    variables=[OBJ_TYPE],
    evidence={}
)
print(result)


result = inference_engine.query(
    variables=[INTENT],
    evidence={}
)
print(result)

result = inference_engine.query(
    variables=[OBJ_TYPE, INTENT],
    evidence={}
)
print(result)
