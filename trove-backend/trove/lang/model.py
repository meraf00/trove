import google.generativeai as palm
import string

class LangModel:
    def __init__(self, api_key):
        palm.configure(api_key=api_key)

        self.summarize_config = {
            "model": "models/text-bison-001",
            "temperature": 0.6,
            "candidate_count": 1,
            "top_k": 40,
            "top_p": 0.95,
            "max_output_tokens": 1024,
            "stop_sequences": [],
            "safety_settings": [
                {"category": "HARM_CATEGORY_DEROGATORY", "threshold": 1},
                {"category": "HARM_CATEGORY_TOXICITY", "threshold": 1},
                {"category": "HARM_CATEGORY_VIOLENCE", "threshold": 2},
                {"category": "HARM_CATEGORY_SEXUAL", "threshold": 2},
                {"category": "HARM_CATEGORY_MEDICAL", "threshold": 2},
                {"category": "HARM_CATEGORY_DANGEROUS", "threshold": 2},
            ],
        }

        self.chat_config = {
            "model": "models/chat-bison-001",
            "temperature": 0.85,
            "candidate_count": 1,
            "top_k": 40,
            "top_p": 0.95,
        }

    def sanitize(self, text):
        sanitized = []

        printable = set(string.printable)

        for char in text:
            if char in printable:
                sanitized.append(char)
        
        return ''.join(sanitized)

    def chat(self, request, messages, context=None):
        request = self.sanitize(request)
        
        examples = [
            [
                "I am a graphics designer and I want to buy a computer.",
                "What is your budget range? What brand would you prefer to use?",
            ],
            [
                "Which one is better HP Pavilion 16 GB Ram which costs 32000 ETB or Dell 32 GB Ram costs 42000 ETB",
                "If you are on a budget the HP Pavilion would be the way to go. However, the Dell will have significant performance advantage over HP Pavilion 16 GB due to its larger ram capacity.",
            ],
        ]

        if not context:
            context = "You are my shopping pal, knowledgeable about electronics market. Please respond in concise sentences. You can ask me professions, what I would like to buy and recommend items if I ask you to choose from list."

        messages.append(request)

        response = palm.chat(
            **self.chat_config, context=context, examples=examples, messages=messages
        )

        return response.last

    def summarize(self, request, context=None):
        request = self.sanitize(request)
        
        if not context:
            context = (
                "Highlight relevant points for purchase including the vendor and price."
            )

        prompt = f"Summarize this paragraph. {context}\n\n{request}".encode("utf-8", "replace").decode()                

        response = palm.generate_text(**self.summarize_config, prompt=prompt)

        return response.result
    
    def extract(self, info, text):   
        text = self.sanitize(text)                

        prompt = f"Extract {info} from this paragraph. List them separated with comma without other text.\n\n{text}. ".encode("utf-8", "replace").decode()                        
        
        response = palm.generate_text(**self.summarize_config, prompt=prompt)

        return response.result
