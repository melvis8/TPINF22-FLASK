import os

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZWQyNTUxOQAAACBIuQNrZ8/MqLGjk1JMx8CW2s0itbKJMQYlNxvfgAaO5QAAALDv/IlC7/yJQgAAAAtzc2gtZWQyNTUxOQAAACBIuQNrZ8/MqLGjk1JMx8CW2s0itbKJMQYlNxvfgAaO5QAAAEB9WPK5UfqOdQx+yGstOQCd1gSFIdDXMoj20CX7TOwU9Ei5A2tnz8yosaOTUkzHwJbazSK1sokxBiU3G9+ABo7lAAAAJm1lbHZpcy1kZXZAbWVsdmlzLWRldi1IUC1FTlZZLU5vdGy")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
        f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
