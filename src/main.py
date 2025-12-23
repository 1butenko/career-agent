import os
import gradio as gr
from openai import OpenAI
from agent import Agent
from tools import read_json
from dotenv import load_dotenv

load_dotenv(override=True)

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

record_unknown_question_json = read_json("tools/unknown_question.tool.json")
record_user_details_json = read_json("tools/user_details.tool.json")
tools = [{"type": "function", "function": record_user_details_json},
        {"type": "function", "function": record_unknown_question_json}]

agent = Agent(name="#", tools=tools, openai=openai) # Your name here
gr.ChatInterface(fn=agent.chat).launch()