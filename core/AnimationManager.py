from animations.CircleAnimation import CircleAnimation
from animations.PointsAnimation import PointsAnimation
from animations.ThunderStormAnimation import ThunderStormAnimation
from animations.SweepAnimation import SweepAnimation
from animations.EmptyAnimation import EmptyAnimation
from animations.CRGBCircleAnimation import CRGBCircleAnimation
from animations.DeathRayAnimation import DeathRayAnimation
from animations.PolygonAnimation import PolygonAnimation
from animations.FanPointsAnimation import FanPointsAnimation
from animations.SweepingFanPointsAnimation import SweepingFanPointsAnimation
from animations.SweepingFanAnimation import SweepingFanAnimation
from animations.StroboFanAnimation import StroboFanAnimation
import Config
import time
import random

class AnimationManager:

    @staticmethod
    def all_animations():
        return [
            {'name': 'no_animation',          'human_name': 'No Animation',          'class': EmptyAnimation},
            {'name': 'big_circle',            'human_name': 'Big Circle',            'class': CircleAnimation},
            {'name': 'rotating_points',       'human_name': 'Rotating Points',       'class': PointsAnimation},
            {'name': 'thunderstorm',          'human_name': 'Thunderstorm',          'class': ThunderStormAnimation},
            {'name': 'sweeps',                'human_name': 'Sweeps',                'class': SweepAnimation},
            {'name': 'crgb_circle',           'human_name': 'CRGB Circles',          'class': CRGBCircleAnimation},
            {'name': 'death_ray',             'human_name': 'Death Ray',             'class': DeathRayAnimation},
            {'name': 'polygon',               'human_name': 'Polygon',               'class': PolygonAnimation},
            {'name': 'fan_points',            'human_name': 'Fan Points',            'class': FanPointsAnimation},
            {'name': 'sweeping_fan_points',   'human_name': 'Sweeping Fan Points',   'class': SweepingFanPointsAnimation},
            {'name': 'sweeping_fan',          'human_name': 'Sweeping Fan',          'class': SweepingFanAnimation},
            {'name': 'strobo_fan',            'human_name': 'Strobo Fan',            'class': StroboFanAnimation},
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
                self.redis.set(Config.redis_prefix() + 'current_animation', 'no_animation')

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

            animation_name = self.redis.get(Config.redis_prefix() + 'current_animation').decode("utf-8")
            return self.set_current_animation_class(animation_name)

        # self.counter += 1
        # if self.counter > 10:
        #     self.counter = 0

        #     animation_strategy = self.redis.get(Config.redis_prefix() + 'animation_strategy')

        #     if animation_strategy == b'static':
        #         animation_name = self.redis.get(Config.redis_prefix() + 'static_animation').decode("utf-8")
        #         return self.set_current_animation_class(animation_name)

        #     if animation_strategy == b'random':
        #         animation_duration = 10000 # int(self.redis.get(Config.redis_prefix() + 'animation_duration').decode("utf-8"))
        #         if ((time.time() * 1000) - self.last_change_at) > animation_duration:
        #             self.last_change_at = time.time() * 1000

        #             animations = list(map(lambda a: a['name'], self.all_animations()))
        #             animations.remove('no_animation')

        #             if self.current_animation in animations:
        #                 animations.remove(self.current_animation)

        #             animation_name = random.choice(animations)

        #             return self.set_current_animation_class(animation_name)

        #     else:
        #         return self.set_current_animation_class('no_animation')

        # return None

