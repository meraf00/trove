from dotenv import load_dotenv
import google.generativeai as palm
import os

load_dotenv()

PALM_API = os.environ.get('PALM_API')

palm.configure(api_key=PALM_API)

defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.85,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}

context = "You are my shopping pal, knowledgeable about electronics market. Please respond in concise sentences. You can ask me professions, what I would like to buy and recommend items if I ask you to choose from list."
examples = [
  [
    "I am a graphics designer and I want to buy a computer.",
    "What is your budget range? What brand would you prefer to use?"
  ],
  [
    "Which one is better HP Pavilion 16 GB Ram which costs 32000 ETB or Dell 32 GB Ram costs 42000 ETB",
    "If you are on a budget the HP Pavilion would be the way to go. However, the Dell will have significant performance advantage over HP Pavilion 16 GB due to its larger ram capacity."
  ]
]
messages = [
  "What computer shall I buy as software engineer?",
  "As a software engineer, you will need a computer that can handle the demands of your work. Here are a few things to consider when choosing a computer:\n\n* Processor: A fast processor is essential for running multiple programs and compiling code. Look for a computer with a quad-core processor or higher.\n* RAM: RAM is used to store data that is currently being used by the computer. A software engineer will need a lot of RAM to run multiple programs and keep their code open. Look for a computer with at least 16GB of RAM.\n* Storage: You will need a lot of storage space to store your code, projects, and software. Look for a computer with at least 512GB of storage space.\n* Display: A good display is important for coding. Look for a computer with a high-resolution display and wide viewing angles.\n* Keyboard and mouse: A comfortable keyboard and mouse are important for long hours of coding. Look for a keyboard with a good feel and a mouse that is easy to use.\n\nHere are a few specific computers that would be good for software engineers:\n\n* MacBook Pro: The MacBook Pro is a powerful and reliable computer that is popular among software engineers. It has a fast processor, plenty of RAM, and a high-resolution display.\n* Dell XPS 15: The Dell XPS 15 is another great option for software engineers. It has a fast processor, plenty of RAM, and a high-resolution display. It also has a long battery life, which is important for software engineers who work on the go.\n* HP Spectre x360: The HP Spectre x360 is a convertible laptop that can be used as a laptop or a tablet. It has a fast processor, plenty of RAM, and a high-resolution display. It also has a long battery life.\n\nUltimately, the best computer for a software engineer is the one that meets their individual needs and budget. Consider the factors above when choosing a computer, and do some research to find the best option for you."
]
messages.append("NEXT REQUEST")
response = palm.chat(
  **defaults,
  context=context,
  examples=examples,
  messages=messages
)

print(response.messages)
print(response.last) # Response of the AI to your most recent request