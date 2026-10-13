import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model_name = os.getenv("APP_MODEL_NAME", "gpt-4o")
llm = ChatOpenAI(model=model_name, temperature=0)
