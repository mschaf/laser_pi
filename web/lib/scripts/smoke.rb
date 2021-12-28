smoke = Device.where("redis_prefix LIKE ?", "%smoke%").first

while true 
   puts "smoke"
   smoke.current_animation = "long_burst"
   smoke.save
   sleep 90
end
