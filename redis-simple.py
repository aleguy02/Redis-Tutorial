import redis
import os
from dotenv import load_dotenv

load_dotenv()

r = redis.Redis(
    host='redis-13132.c80.us-east-1-2.ec2.redns.redis-cloud.com',
    port=13132,
    decode_responses=True,
    password=os.getenv("REDIS_PASSWORD")
    )

r.delete("Batman")