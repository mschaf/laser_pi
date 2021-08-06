from animations.CircleAnimation import CircleAnimation
from animations.PointsAnimation import PointsAnimation
from animations.ThunderStormAnimation import ThunderStormAnimation
from animations.SweepAnimation import SweepAnimation
from animations.EmptyAnimation import EmptyAnimation
from animations.CRGBCircleAnimation import CRGBCircleAnimation
from animations.DeathRayAnimation import DeathRayAnimation
import Config
import time

class AnimationManager:

    @staticmethod
    def all_animations():
        return [
            {'name': 'no_animation',     'human_name': 'No Animation',     'class': EmptyAnimation},
            {'name': 'big_circle',       'human_name': 'Big Circle',       'class': CircleAnimation},
            {'name': 'rotating_points',  'human_name': 'Rotating Points',  'class': PointsAnimation},
            {'name': 'thunderstorm',     'human_name': 'Thunderstorm',     'class': ThunderStormAnimation},
            {'name': 'sweeps',           'human_name': 'Sweeps',           'class': SweepAnimation},
            {'name': 'crgb_circle',      'human_name': 'CRGB Circles',     'class': CRGBCircleAnimation},
            {'name': 'death_ray',        'human_name': 'Death Ray',        'class': DeathRayAnimation},
        ]

    def __init__(self):
        self.current_animation_class = None
        self.current_animation = ''
        self.last_change_at = 0
        self.counter = 0
        self.redis = Config.redis_connection()
        self.publish_all_animations()
        print("Published Animations")

    def publish_all_animations(self):
        self.redis.delete(Config.redis_prefix() + 'all_animations')
        for animation in self.all_animations():
            self.redis.hset(Config.redis_prefix() + 'all_animations', animation['name'], animation['human_name'])

    def random_animation(self):
        pass

    def set_current_animation_class(self, animation_name):

        if animation_name != self.current_animation:
            animation = None

            for a in self.all_animations():
                if a['name'] == animation_name:
                    animation = a

            if not animation:
                animation = {'name': 'no_animation', 'human_name': 'No Animation', 'class': EmptyAnimation}

            self.current_animation_class = animation['class']
            self.current_animation = animation['name']

            print(f"switching to { animation['human_name']}")
            return animation['class']
        else:
            return None

    def determine_animation_class(self):
        self.counter += 1
        if self.counter > 10:
            self.counter = 0

            animation_strategy = self.redis.get(Config.redis_prefix() + 'animation_strategy')

            if animation_strategy == b'static':
                animation_name = self.redis.get(Config.redis_prefix() + 'static_animation').decode("utf-8")
                return self.set_current_animation_class(animation_name)

            else:
                return self.set_current_animation_class('no_animation')

        return None

