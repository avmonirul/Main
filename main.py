import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
  model="code-davinci-002",
  prompt="#JavaScript to Python:\nJavaScript: \ndogs = [\"bill\", \"joe\", \"carl\"]\ncar = []\ndogs.forEach((dog) {\n    car.push(dog);\n});\n\nPython:\nBuild me a login page with python\n\n#Python to JavaScript:\nPython:\ndef add(a, b):\n    return a + b\n\nJavaScript:\nfunction add(a, b) {\n    return a + b;\n}\n\n#JavaScript to Python:\nJavaScript:\nfunction add(a, b) {\n    return a + b;\n}\n\nPython:\ndef add(a, b):\n    return a + b\n\n#Python to JavaScript:\nPython:\ndef add(a, b):\n    return a + b\n\nJavaScript:\nfunction add(a, b) {\n    return a + b;\n}\n\n#JavaScript to Python:\nJavaScript:\nfunction add(a, b) {\n    return a + b;\n}\n\nPython:\ndef add(a, b):\n    return a + b\n\n#Python to JavaScript:\nPython:\ndef add(a, b):\n    return a + b\n\nJavaScript:\nfunction add(a, b) {\n    return a + b;\n}\n\n#JavaScript to Python:\nJavaScript:\nfunction add(a, b",
  temperature=0,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)