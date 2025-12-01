from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider

client = OpenAIProvider(base_url='http://localhost:4000/v1',api_key='sk-l-FfhzWRvSYlPaCV5qBjqQ')

model = OpenAIChatModel(
    model_name="deepseek-chat",
    provider=client
)

agent = Agent(model=model)

result_sync = agent.run_sync('What is the capital of Italy?')

print(f"Synchronous result: {result_sync.output}")