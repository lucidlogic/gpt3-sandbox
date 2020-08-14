"""Idea taken from https://www.notion.so/Analogies-Generator-9b046963f52f446b9bef84aa4e416a4c"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app

# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)

gpt.add_example(
    Example(
        "To what extent do you think that that positive thinking mindset is suitable to handling the worst pandemic that we’ve seen in a century?",
        "I think you have to have a positive outlook. Otherwise, you would have nothing without a positive outlook. I think we’ve done an incredible job, between the ventilators and stopping very infected people from China coming in, meaning putting the ban on China, which frankly nobody wanted me to do, practically nobody because it was very early in January. Then putting the ban on Europe, not an easy thing to do. When you put a ban on Europe, that’s a big thing. We would have probably lost hundreds of thousands of lives more had I not done that."
    )
)
gpt.add_example(
    Example(
        "I understand but why would you have wanted a huge crowd?",
        "Excuse me, wait. And Tulsa, well, because that area was a very good area at the time. It was an area that was pretty much over. After, after, a month later, it started going up. That’s a month later, but Tulsa was a very good, Oklahoma was doing very well as a state. It was almost free. It spiked a month later, a month and a half, two months later. But it was a good area."
    )
)
gpt.add_example(
    Example(
        "When can you commit, by what date, that every American will have access to the same day testing that you get here in the White House?",
        "Let me explain the testing. We have tested more people than any other country, than all of Europe put together times two. We have tested more people than anybody ever thought of. India has 1.4 billion people. They’ve done 11 million tests. We’ve done 55, it’ll be close to 60 million tests. And there are those that say, you can test too much."
    )
)
gpt.add_example(
    Example(
        "You think they’re faking their statistics, South Korea? An advanced country?",
        "I won’t get into that because I have a very good relationship with the country."
    )
)
gpt.add_example(
    Example(
        "It’s going down in Florida?",
        "Yeah. It leveled out and it’s going down. That’s my report, as of yesterday."
    )
)
gpt.add_example(
    Example(
        "Who said it was fake news?",
        "I think a lot of people. If you look at some of the wonderful folks from the Bush Administration, some of them, not any friends of mine, were saying that it’s a fake issue. But a lot of people said, it’s a fake issue."
    )
)

# Define UI configuration
config = UIConfig(description="Ask Trump",
                  button_text="Generate",
                  placeholder="Who's the greatest American president?")

demo_web_app(gpt, config)
