from redis import asyncio as aioredis


async def get_redis_pool():
    return await aioredis.from_url("redis://localhost")
