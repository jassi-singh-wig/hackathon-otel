from typing import Union
from opentelemetry import trace
from opentelemetry import metrics
from random import randint


from fastapi import FastAPI

# Acquire a tracer
tracer = trace.get_tracer(__name__)

# Acquire a meter.
meter = metrics.get_meter(__name__)

# Now create a counter instrument to make measurements with
roll_counter = meter.create_counter(
    "roll_counter",
    description="The number of rolls by roll value",
)


app = FastAPI()

@app.get("/rolldice")
def roll_dice():
    return str(do_roll())

def do_roll():
    # This creates a new span that's the child of the current one
    with tracer.start_as_current_span("do_roll") as rollspan:  
        res = randint(1, 6)
        rollspan.set_attribute("roll.value", res)
        # This adds 1 to the counter for the given roll value
        roll_counter.add(1, {"roll.value": res})
        return res

@app.get("/")
def read_root():
    return {"Hello": "World FastAPI 1"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/squarefromapp1/{item_id}")
def send_square(item_id: int):
    return item_id*item_id
