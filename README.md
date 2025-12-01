# learn-lite-llm


## cURL
```
curl -X POST "http://localhost:4000/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-l-FfhzWRvSYlPaCV5qBjqQ" \
  -d '{
    "model": "deepseek-chat",
    "messages": [
      {"role": "user", "content": "Hello, how are you?"}
    ]
  }'
```

### Response
```
{"id":"27c91309-2fe1-4e59-ac5e-e1ecf0fb34ae","created":1764574031,"model":"deepseek-chat","object":"chat.completion","system_fingerprint":"fp_eaab8d114b_prod0820_fp8_kvcache","choices":[{"finish_reason":"stop","index":0,"message":{"content":"Hello! I'm doing great, thank you for asking! 😊 I'm here and ready to help you with whatever you need—whether it's answering questions, brainstorming ideas, or just having a friendly chat. How are you doing today?","role":"assistant"}}],"usage":{"completion_tokens":49,"prompt_tokens":10,"total_tokens":59,"prompt_tokens_details":{"cached_tokens":0},"prompt_cache_hit_tokens":0,"prompt_cache_miss_tokens":10}}
```

## Python
```
from openai import OpenAI

client = OpenAI(base_url="http://localhost:4000", api_key="sk-l-FfhzWRvSYlPaCV5qBjqQ")

resp = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "Capital of france?"}]
)

print(resp.choices[0].message)

```

### Response
```
ChatCompletionMessage(content='The capital of France is **Paris**.', refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None)
```

## Pydantic AI
```
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
```

### Response
```
Synchronous result: The capital of Italy is **Rome** (Roma in Italian). It's not only the political and administrative center but also a city with immense historical, cultural, and artistic significance, often called the "Eternal City."
```
