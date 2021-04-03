import redis

def redis_connection():
    return redis.Redis(host='localhost', port=6379, db=0)