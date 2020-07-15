# Define a script for an beautiful insect-based love story
from base import Scene, Act, Character
class Script():
    title = "Bee Movie"

    def create_acts(self):
        self.act_one()

    def act_one(self):
        scenes = {}

        # make my characters
        barry = Character("Barry B. Benson")
        vanessa = Character("Vanessa Bloome")
        adam = Character("Adam Flayman")
        characters = [barry, vanessa, adam]

        # set my locations
        locations = ["hive - Park/Outside", "interior - Vanessa's Home"]

        self.scenes["Daily Grind"] = Scene(characters, locations[0])

        return Act(characters, scenes)