from redis_conn_methods.airedis_config import get_redis_pool


async def write_data(phone: str, address: str):
    redis = await get_redis_pool()
    await redis.set(phone, address)
    await redis.close()


async def check_data(phone: str):
    redis = await get_redis_pool()
    address = await redis.get(phone)
    await redis.close()
    return address.decode() if address else None
