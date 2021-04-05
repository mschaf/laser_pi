class Device < ApplicationRecord

  validates :name, :redis_prefix, presence: true, uniqueness: true

  def set_static(animation)
    REDIS_CLIENT.set(redis_prefix + 'animation_strategy', 'static')
    REDIS_CLIENT.set(redis_prefix + 'static_animation', animation)
  end

  def all_animations
    REDIS_CLIENT.hgetall(redis_prefix + 'all_animations')
  end


end