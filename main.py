from fastapi import FastAPI

import random

app = FastAPI()

QUOTES = [
    "They keep saying that sea levels are rising an' all this. It's nowt to do with the icebergs melting, it's because there's too many fish in it. Get rid of some of the fish and the water will drop. Simple. Basic science.",
"I always have a problem liking things that I'm told I should like. This has been the problem with most of the Wonders I have seen so far. The fact that this one is called the 'Great' Wall of China annoys me. I'll decide if it's great or not. It might end up being the 'All Right Wall of China' to me."
]

@app.get("/quote")
def get_random_quote():
    return {"quote": random.choice(QUOTES)}


@app.get("/all")
def list_all_quotes():
    return {"quotes": QUOTES}
