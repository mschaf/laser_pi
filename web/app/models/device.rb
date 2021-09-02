class Device < ApplicationRecord

  validates :name, :redis_prefix, presence: true, uniqueness: true

  include DoesRedisAttribute[:current_animation]
  include DoesRedisHashAttribute[:all_animations, readonly: true]
  include DoesRedisAttribute[:animation_strategy]
  include DoesRedisAttribute[:random_weights]
  include DoesRedisAttribute[:random_durations]
  include DoesRedisAttribute[:ready]
  include DoesRedisAttribute[:remaining_seconds]


  def human_current_animation
    all_animations.fetch(current_animation, '')
  end


end