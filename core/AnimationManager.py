from animations.CircleAnimation import CircleAnimation
from animations.PointsAnimation import PointsAnimation
from animations.ThunderStormAnimation import ThunderStormAnimation
from animations.SweepAnimation import SweepAnimation
from animations.EmptyAnimation import EmptyAnimation
import Config
import time

class AnimationManager:

    @staticmethod
    def all_animations():
        return [
            {'name': 'nothing',          'human_name': 'Nothing',          'class': EmptyAnimation},
            {'name': 'big_circle',       'human_name': 'Big Circle',       'class': CircleAnimation},
            {'name': 'rotating_points',  'human_name': 'Rotating Points',  'class': PointsAnimation},
            {'name': 'thunderstorm',     'human_name': 'Thunderstorm',     'class': ThunderStormAnimation},
            {'name': 'sweeps',           'human_name': 'Sweeps',           'class': SweepAnimation},
        ]

    def __init__(self):
        self.current_animation_class = None
        self.last_change_at = 0
        self.counter = 0
        self.redis = Config.redis_connection()

    def random_animation(self):
        pass

    def set_current_animation_class(self, animation_class):
        self.current_animation_class = animation_class
        print(f"switching to {animation_class}")
        return animation_class

    def determine_animation_class(self):
        self.counter += 1
        if self.counter > 10:
            self.counter = 0

            animation_strategy = self.redis.get('laser/animation_strategy')

            if animation_strategy == b'static':
                animation_name = self.redis.get('laser/static_animation').decode("utf-8")

                animation = None

                for a in self.all_animations():
                    if a['name'] == animation_name:
                        animation = a

                if not animation:
                    return self.set_current_animation_class(EmptyAnimation)

                if animation['class'] != self.current_animation_class:
                    return self.set_current_animation_class(animation['class'])
                else:
                    return None

            else:
                return self.set_current_animation_class(EmptyAnimation)

        return None

