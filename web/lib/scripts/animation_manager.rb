devices = Device.all.to_a

puts "Animation Manager"

while true

  devices.each do |device|

    if device.animation_strategy == 'random'
      remaining_seconds = (device.remaining_seconds.presence || 0).to_i

      if remaining_seconds == 0
        puts "Change due for #{device.name}"

        animations = device.all_animations
        weighted_animations = []

        random_weights = JSON.parse(device.random_weights).transform_values(&:to_f)
        random_durations = JSON.parse(device.random_durations).transform_values(&:to_i)

        available_animations = animations.keys

        available_animations.each do |animation|
          count = ((random_weights[animation] || 0) * 10).to_i
          count.times do
            weighted_animations << animation
          end
        end

        animation = weighted_animations.sample

        if animation
          duration = random_durations[animation] || 20
          puts "  Selected #{animations[animation]} to run for #{duration} seconds"

          device.remaining_seconds = duration
          device.current_animation = animation
          device.save
        end


      else
        device.remaining_seconds = remaining_seconds - 1
        device.save
      end
    end



  end


  sleep 1
end
