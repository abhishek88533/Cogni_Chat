from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Loads and validates application settings from environment variables.
    """
    # Load settings from a .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # API Keys - these will raise an error if not found in the .env file
    GOOGLE_API_KEY: str
    PINECONE_API_KEY: str
    PINECONE_ENVIRONMENT: str
    COHERE_API_KEY: str

    # Pinecone Index Configuration
    PINECONE_INDEX_NAME: str = "mini-rag-index"

# Create a single, reusable instance of the settings
settings = Settings()