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

gpt.add_example(Example('life goals',
                        'Your goal in life is to find out the people who need you the most, to find out the business that needs you the most, to find the project and the art that needs you the most. There is something out there just for you.'))
gpt.add_example(Example('wealth',
                        'Seek wealth, not money or status. Wealth is having assets that earn while you sleep. Money is how we transfer time and wealth. Status is your place in the social hierarchy.'))
gpt.add_example(Example(
    'founders', 'Founders run every sprint as if they’re about to lose, but grind out the long race knowing that victory is inevitable.'))
gpt.add_example(Example('health',
                        'Doctors won’t make you healthy. Nutritionists won’t make you slim.Teachers won’t make you smart.Gurus won’t make you calm.Mentors won’t make you rich.Trainers won’t make you fit.Ultimately, you have to take responsibility. Save yourself.'))
gpt.add_example(Example('fakes',
                        'It is the mark of a charlatan to explain a simple concept in a complex way'))
gpt.add_example(Example('ethics',
                        'Don\’t do things that you know are morally wrong. Not because someone is watching, but because you are. Self-esteem is just the reputation that you have with yourself. You’ll always know.'))

gpt.add_example(Example('originality',
                        'The larger the herd, the lower the returns'))

gpt.add_example(Example('politics',
                        'The two party system is an emergent bug in representative democracy.'))

# Define UI configuration
config = UIConfig(description="Wisdom generator",
                  button_text="Generate",
                  placeholder="boredom")

demo_web_app(gpt, config)
