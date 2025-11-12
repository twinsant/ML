from ollama import chat

def get_temperature(city: str) -> str:
  """Get the current temperature for a city
  
  Args:
    city: The name of the city

  Returns:
    The current temperature for the city
  """
  temperatures = {
    "New York": "22°C",
    "London": "15°C",
    "Tokyo": "18°C",
  }
  return temperatures.get(city, "Unknown")

messages = [{"role": "user", "content": "What's the temperature in New York?"}]

# pass functions directly as tools in the tools list or as a JSON schema
response = chat(model="qwen3:32b", messages=messages, tools=[get_temperature], think=True)

messages.append(response.message)
if response.message.tool_calls:
  # only recommended for models which only return a single tool call
  call = response.message.tool_calls[0]
  result = get_temperature(**call.function.arguments)
  # add the tool result to the messages
  messages.append({"role": "tool", "tool_name": call.function.name, "content": str(result)})

  final_response = chat(model="qwen3:32b", messages=messages, tools=[get_temperature], think=True)
  print(final_response.message.content)