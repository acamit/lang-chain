from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from langchain.chat_models import init_chat_model
from pydantic import BaseModel

from prompts import SYSTEM_PROMPT
from responseformat import ResponseFormat
from tools.Context import Context

from tools.WeatherTool import get_user_location, get_weather_for_location

# Switch to OpenAI model using init_chat_model. The API key is expected to be set in environment variables.
model = init_chat_model(
    "gpt-4o",  # OpenAI's latest model, or use "gpt-4" if not available
    temperature=0.5,
    timeout=10,
    max_tokens=1000)
checkpointer = InMemorySaver()

agent = create_agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    tools=[get_user_location, get_weather_for_location],
    context_schema=Context,
    response_format=ToolStrategy(ResponseFormat),
    checkpointer=checkpointer
)

class MessageInput(BaseModel):
    messages: list[dict[str, str]]

config = {"configurable": {"thread_id": "1"}}

response = agent.invoke(
    MessageInput(messages=[{"role": "user", "content": "what is the weather outside?"}]),
    config=config,
    context=Context(user_id="1")
)


print(response['structured_response'])
# ResponseFormat(
#     punny_response="Florida is still having a 'sun-derful' day! The sunshine is playing 'ray-dio' hits all day long! I'd say it's the perfect weather for some 'solar-bration'! If you were hoping for rain, I'm afraid that idea is all 'washed up' - the forecast remains 'clear-ly' brilliant!",
#     weather_conditions="It's always sunny in Florida!"
# )


# Note that we can continue the conversation using the same `thread_id`.
response = agent.invoke(
    MessageInput(messages=[{"role": "user", "content": "thank you!"}]),
    config=config,
    context=Context(user_id="1")
)

print(response['structured_response'])