import openai
from .base_model import BaseModel


class ChatGPT(BaseModel):
    def __init__(
        self,
        api_key,
        model="gpt-4o-mini",
        max_tokens=1000,
        system="このコード差分を見てプロの目線でコードレビューしてください",
    ):
        self.model = model
        self.max_tokens = max_tokens
        self.system = system
        self.messages = [{role: "system", content: system}]
        self.client = openai.ChatCompletion.create(
        )

    def send(self, message):
        self.messages.append({"role": "user", "content": message})
        result = openai.ChatCompletion.create(
            model=self.model,
            max_tokens=self.max_tokens,
            system=self.system,
            messages=self.messages
        )
        content = result['choices'][0]["message"]["content"]
        self.messages.append({"role": result.role, "content": content})
        return result
