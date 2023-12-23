from dotenv import dotenv_values


# conf = dotenv_values(".env")
conf = dotenv_values(".env_docker")


class Settings:
    DB_HOST: str = conf.get("DB_HOST")
    DB_PORT: int = conf.get("DB_PORT")
    DB_USER: str = conf.get("DB_USER")
    DB_PASS: str = conf.get("DB_PASS")
    DB_NAME: str = conf.get("DB_NAME")

    api_v1_prefix: str = "/api/v1"

    @property
    def url_async(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def url_sync(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    echo: bool = False


settings = Settings()
