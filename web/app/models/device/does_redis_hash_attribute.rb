module Device::DoesRedisHashAttribute

  as_trait do |field, readonly: false|
    attr_accessor field

    define_method field do
      instance_variable_set("@#{field}", REDIS_CLIENT.hgetall(redis_prefix + field.to_s))
      instance_variable_get("@#{field}")
    end

    unless readonly
      after_commit do
        REDIS_CLIENT.del(redis_prefix + field.to_s)
        REDIS_CLIENT.hset(redis_prefix + field.to_s, instance_variable_get("@#{field}") || {})
      end
    end



  end

  
end