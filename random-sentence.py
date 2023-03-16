import random

# --------------------------
# A class to generate random Star Wars sentence.
# --------------------------
class Random_Sentence:
    # Properties
    sentences = [
        "Au secours Obi-Wan Kenobi, vous êtes mon seul espoir.",
        "Je suis ton père.",
        "Fais-le ou ne le fais pas. Il n'y a pas d'essai.",
        "Je ne viendrai jamais du côté obscur. Vous avez échoué.",
        "La peur est le chemin vers le côté obscur : la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance.",
        "Vous êtes venus dans cette casserole ? Vous êtes plus braves que je ne le pensais.",
        "Que la force soit avec toi.",
        "Toujours par deux ils vont, ni plus, ni moins… Le Maître et son Apprenti…"
    ]
    sentence = ""

    # --------------------------
    # Constructor
    # --------------------------
    def __init__(self):
        print(self.generate_sentence())
    
    # --------------------------
    # Generate random sentence from self.sentences array
    #
    # :param self Object
    # :return string
    # --------------------------
    def generate_sentence(self):
        number = random.randint(0, len(self.sentences) - 1)

        self.sentence = self.sentences[number]

        return self.sentence

Random_Sentence()
