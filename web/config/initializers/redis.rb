redis_host = ENV['REDIS_HOST'].presence || 'localhost'

REDIS_CLIENT = Redis.new(host: redis_host, port: 6379, db: 0)