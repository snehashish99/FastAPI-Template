import databases
from configurations import POSTGRES


database = databases.Database(
    POSTGRES.POSTGRES_DATABASE_URL, min_size=POSTGRES.POSTGRES_MIN_CONNECTIONS, max_size=POSTGRES.POSTGRES_MAX_CONNECTIONS
)