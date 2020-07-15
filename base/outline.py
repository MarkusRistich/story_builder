class Act(object):
    """
        Defines a general plot section within a story.
    """

    self._characters = []  # list of Characters
    self.scenes = []  # list of Scenes
    self._current_scene = None

    def __init__(self, characters, scenes):
        self.scenes = []
        self._characters = characters

    def define_scenes(self):

    def begin_scene(self, scene_name):
        self._current_scene = self.scenes[scene_name]
        self._current_scene.open(characters)
        self._current_scene.enter(location, characters)

    def end_scene(self):
        self._current_scene.close()

    def exeunt(self):
        self._current_scene = None
        self._characters = None


class Scene():
    """
        Defines a specific beat of action, in a certain location.
    """
    self._location = None
    self.is_active = False

    def __init__(self, characters, location):
        # in fair verona
        self._location = location

    def open(self, characters):
        # two star cross'd lovers
        self._characters = characters
        for char in self._characters:
            char.in_scene = True

        self.is_active = True

    def close(self, characters):
        # bury their parent's strife
        for char in self._characters:
            char.in_scene = False

        self.is_active = False

class Character():
    """
        Defines a character and their status within the piece.
    """
    self.name = ""
    self.in_scene = False