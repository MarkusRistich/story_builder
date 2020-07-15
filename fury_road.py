# Define a script for an impeccable apocalyptic wasteland
from base import Scene, Act, Character
class Script():
    title = "Fury Road"

    def create_acts(self):
        self.act_one()

    def act_one(self):
        scenes = {}

        # make my characters
        max = Character("Max Rockatansky")
        nux = Character("Nux")
        furiosa = Character("Furiosa")
        joe = Character("Immortan Joe")
        characters = [max, nux, furiosa, joe]

        # set my locations
        locations = ["rock castle - Australia", "desert clearing - Namibia"]

        self.scenes["Waterfall"] = Scene(characters, locations[0])

        return Act(characters, scenes)

