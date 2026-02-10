from openai import AsyncOpenAI


class BaseAgent:
    def __init__(self, model: str, system_prompt: str):
        self.model = model
        self.system_prompt = system_prompt
    
    async def analyze(self, idea: str, api_key: str) -> str:
        client = AsyncOpenAI(api_key=api_key)
        
        response = await client.responses.create(
            model=self.model,
            input=idea,
            instructions=self.system_prompt
        )
        
        return response.output_text
