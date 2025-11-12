from ollama import chat
# from pathlib import Path

# Pass in the path to the image
path = input('Please enter the path to the image: ')

# You can also pass in base64 encoded image data
# img = base64.b64encode(Path(path).read_bytes()).decode()
# or the raw bytes
# img = Path(path).read_bytes()

response = chat(
  model='qwen2.5vl:32b',
  messages=[
    {
      'role': 'user',
      'content': '简单描述图片里有什么',
      'images': [path],
    }
  ],
)

print(response.message.content)