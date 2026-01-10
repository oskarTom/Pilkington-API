from fastapi import FastAPI

import random

app = FastAPI()

QUOTES = [
    "They keep saying that sea levels are rising an' all this. It's nowt to do with the icebergs melting, it's because there's too many fish in it. Get rid of some of the fish and the water will drop. Simple. Basic science.",
    "I always have a problem liking things that I'm told I should like. This has been the problem with most of the Wonders I have seen so far. The fact that this one is called the 'Great' Wall of China annoys me. I'll decide if it's great or not. It might end up being the 'All Right Wall of China' to me.",
    "I find that if you just talk, your mouth comes up with stuff.",
    "The problem I have with all this religion stuff is that I can't relate to it. I think most people got into 'cos it gave them something to do on a Sunday, but since all the shops are now open it isn't required as much.",
    "It's interesting to see that people had so much clutter even thousands of years ago. The only way to get rid of it all was to bury it, and then some archaeologist went and dug it all up.",
    "The problem is, these days you have to listen to too many parts of your body. Sometimes I go with my gut feeling, some say go with what your heart says - it's only a matter of time before my appendix will have an opinion. This is probably why there are so many helplines these days. No one knows who to bloody listen to!",
    "You never see an old man eating a Twix",
    "But there's only so far you can go with thinking",
    "Stephen Hawking you see – that's almost like it's not his body. It's like this brain's come from somewhere – this, you know, magnificent brain – and it's just overpowered the rest of the body to the point that there's no energy for that rest of the body to do anything. And it just sits there with the brain throbbing, thinking of stuff.",
    "There was some women in a cafe the other week that I was sat in, and she came up and she sat down with her mate and she was talkin' loudly goin' on about "oh the baby's lovely." They said it's got, er, lovely big eyes, er, really big hands and feet. Now that doesn't sound like a nice baby to me. I felt like sayin' it sounds like a frog. But I thought I don't know her, there's only so much you can say to a stranger. I don't know what kept me from sayin' it",
    "Maybe this is how Michael Jackson came up with his moonwalk. Maybe he was acting out a time when he stepped in dogshit and tried to get it off his shoes."
]

@app.get("/random")
def get_random_quote():
    return {"quote": random.choice(QUOTES)}


@app.get("/all")
def list_all_quotes():
    return {"quotes": QUOTES}
