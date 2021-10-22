from godot import exposed, export, Vector2, Node2D, ResourceLoader
from godot import *
import scramble as sc


@exposed
class minimaximus(AnimatedSprite):

    # member variables here, example:
    a = export(int)
    b = export(str, default='foo')

    def _ready(self):
        """
        Called every time the node is added to the scene.
        Initialization here.
        """
        print(sc.scramble("This is an example string."))
        self.position.x=123

        pass

    speed = export(float)
    def _process(self, delta):
        pass