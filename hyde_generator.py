from openai import OpenAI

class HyDEGenerator:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def generate_hypothetical_answer(self, question: str) -> str:
        prompt = (
            "Imagine a fictional book that would perfectly match the query: '" + question + "'. "
            "Describe it in 2–3 sentences."
        )
        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=200
        )
        return response.choices[0].message.content.strip()
