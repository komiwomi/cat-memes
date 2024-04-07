#komi idk
import random
def generate_cat_meme(meme_index):

    cat_memes = [
        ("""
         /\_/\\ 
    ____/ o o \\
  /~____  =ø= /
 (______)__m_m)
        """),

        ("""
/\_/\ 
( o.o )
 > ^ <
        """),

        ("""
  /\\_/\\
( o.o )
  > ^ <
        """),

        ("""
    /\_/\ 
   / o o \\
  (   "   )
  (")_(")
        """),

        ("""
    /\_/\ 
   / o o \\
   \_   _/
    /   \
    (   )
    (   )
        """),

        ("""
  /\\___/\\ 
 ( o   o )
 (  =^=  )
 (")___(")
        """),

        ("""
  /\\_/\\ 
 ( o.o )
  > ^ <
  (\"_\")
        """),

        ("""
  /\\_/\\ 
 ( o.o )
  > ^ <
  (")_(")
        """),

        ("""
  /\\_/\\ 
 ( o.o )
  > ^ <
   \"/ \\
        """),

        ("""
  /\\_/\\ 
 ( o.o )
  > ^ <
   \_/
        """)

    ]

 

    meme = cat_memes[meme_index]
    print("Here's your cat meme:")
    print(meme)

 

def generate_cat_joke():
    cat_jokes = [
        "Why did the cat sit on the computer? To keep an eye on the mouse!",
        "What do you call a pile of cats? A meowtain!",
        "What's a cat's favorite subject in school? Hisstory!",
        "Why did the cat go to medical school? To become a purr-geon!",
        "What do you get if you cross a cat with a dark horse? Kitty Perry!",
        "What did the cat say when it was confused? 'I'm purr-plexed!'",
        "What's a cat's favorite color? Purr-ple!",
        "What's a cat's favorite dessert? Mice cream!",
        "What's a cat's favorite TV show? The Big Bang Purr!",
        "What did the cat say when it lost all its money? 'I'm paw!'",
        "Why was the cat sitting on the computer? It wanted to keep an eye on the mouse pad!",
        "Why did the cat go to school? It wanted to be a smarty-cat!",
        "What do you call a cat that can paint? An artist-meow!",
        "What's a cat's favorite game? Hide and squeak!",
        "Why did the cat join the Red Cross? She wanted to be a first-aid kit-ty!",
        "Why did the cat bring a ladder to the bar? It heard the drinks were on the house!",
        "Why did the cat go to space? To find the purr-fect atmosphere!",
        "Why was the cat afraid of a tree? Because of its bark!",
        "What's a cat's favorite type of soda? Mice tea!",
        "Why did the cat join the orchestra? It had perfect purr-cussion!"
    ]

    joke = random.choice(cat_jokes)
    print(joke)

 

def main():
    num_cat_memes = 10
    random_meme_index = random.randint(0, num_cat_memes - 1)
    generate_cat_meme(random_meme_index)
    generate_cat_joke()
  
if __name__ == "__main__":
    main()
