"""Idea taken from https://www.notion.so/Analogies-Generator-9b046963f52f446b9bef84aa4e416a4c"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app

# Construct GPT object and show some examples
gpt = GPT(engine="curie",
          temperature=0.5,
          max_tokens=40)

gpt.add_example(
    Example(
        "Inception",
        "Source Code, The Prestige, Cooper, Minority Report, The Matrix, Memento, The Thirteen Floor, In Time, Transcendence, Interstellar, Lucy, Coherence, Limitless, Eternal Sunshine of the Spotless Mind, Oblivion, Trance"
    )
)

gpt.add_example(
    Example(
        "Dark",
        "Maus, The Silence, Freaks, Lost Girls, White Bear, One of Us, The Ritual, The Open House, Extinction, Lights Out"
    )
)

gpt.add_example(
    Example(
        "Titanic",
        "The Great Gatsby, The Day After Tomorrow, The Perfect Storm, Romeo and Juliet, Twister, Pride & Prejudice, A Walk to Remember, Me Before You, Forrest Gump, The Longest Ride"
    )
)

gpt.add_example(
    Example(
        "Brokeback Mountain",
        "Call me by your name, Moonlight, Gone with the wind, Boy Erased, Candy, Wildlife, Gods Own Country, Into the Wild, Out of Africa, Sideways, Slumdog Millionaire"
    )
)

gpt.add_example(
    Example(
        "Interstellar",
        "The Martian, Gravity, Interstellar, Arrival, Passengers"
    )
)

gpt.add_example(
    Example(
        "Gone Girl",
        "Prisoners, Dark Places, True Story, Searching, Nightcrawler, The Hidden Face, Shutter Island, Side Effects, The Girl with the Dragon Tattoo, The Invisible Guest, The Body, Zodiac, The Prestige, Identity, Seven"
    )
)

gpt.add_example(
    Example(
        "Breaking Bad",
        "Better Call Saul, Narcos, Ozark, The Walking Dead, Succession, Peaky Blinders, Power, Sons of Anarchy, The Wire, Bad Blood, Prison Break"
    )
)

gpt.add_example(
    Example(
        "Friends",
        "How I Met Your Mother, The Big Bang Theory, Two and a Half Men, The Office, 2 Broken Girls, Seinfeld, Frasier, Modem Family"
    )
)

gpt.add_example(
    Example(
        "Toy Story",
        "Monsters Inc, Toy Story 3, Toy Story 4, How to Train Your Dragon, Up, Finding Nemo, Ice Age, Shrek the Third, The Ant Bully, Big Hero, The Lego Movie, American Tail, Bug's Life, Toy Story 2, Chicken Run, Adventure of Rocky and Bullwinkle"
    )
)

# Define UI configuration
config = UIConfig(description="Find similar series/movies",
                  button_text="Generate",
                  placeholder="Titanic")

demo_web_app(gpt, config)
