import random

list_jokes = ["Did you hear about the actor who fell through the floorboards? He was just going through a stage"]
list_jokes.append("Did you hear about the claustrophobic astronaut? He just needed a little space")
list_jokes.append("Why don’t scientists trust atoms? Because they make up everything.")
list_jokes.append("Why did the chicken go to the séance?")
list_jokes.append("What sits at the bottom of the sea and twitches? A nervous wreck.")
list_jokes.extend(["What does a nosy pepper do? Gets jalapeño business!", "How does Moses make tea? He brews.", " Why can’t you explain puns to kleptomaniacs? They always take things literally.", "How do you keep a bagel from getting away? Put lox on it."])
print(list_jokes[random.randint(0, len(list_jokes) - 1)])


