module Device::DoesRedisAttribute

  as_trait do |field|
    attr_accessor field

    define_method field do
      instance_variable_set("@#{field}", REDIS_CLIENT.get(redis_prefix + field.to_s))
      instance_variable_get("@#{field}")
    end

    after_commit do
      
      REDIS_CLIENT.set(redis_prefix + field.to_s, instance_variable_get("@#{field}"))

    end


  end

  
end