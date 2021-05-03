import os
import json
import aioredis


REDIS_URL = os.getenv('REDIS_URL')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')


async def redis_connection():


    if REDIS_PASSWORD:
        redis = await aioredis.create_redis_pool(REDIS_URL, password=REDIS_PASSWORD)
    else:
        redis = await aioredis.create_redis_pool(REDIS_URL)

    return redis
    

async def redis_set(key: str, value: str):

    redis = await redis_connection()

    await redis.set(key, value)

    redis.close()
    await redis.wait_closed()

    return True

async def redis_get(key: str):

    redis = await redis_connection()

    value = await redis.get(key, encoding='utf-8')

    redis.close()
    await redis.wait_closed()

    return value

async def redis_hget(key, field: str):

    redis = await redis_connection()

    value = await redis.hget(key, field, encoding='utf-8')

    redis.close()
    await redis.wait_closed()

    if value:
        return json.loads(value)

async def redis_hset(key, field, value: str):

    redis = await redis_connection()

    await redis.hset(key, field, json.dumps(value))

    redis.close()
    await redis.wait_closed()

    return True