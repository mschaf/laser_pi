import redis

def redis_connection():
    return redis.Redis(host='localhost', port=6379, db=0)

def redis_prefix():
    return 'laser/0/'