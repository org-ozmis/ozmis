import sentry_sdk
import os
from dotenv import load_dotenv

load_dotenv()

sentry_sdk.init(
    dsn=os.getenv("DSN"),
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
