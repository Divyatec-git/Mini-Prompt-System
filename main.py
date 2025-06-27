from datetime import datetime
import os
import re
import time
from jinja2 import Environment, FileSystemLoader
from openai import OpenAI
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
from collections import deque

console = Console()

# Configuration Manager (Autoconfig)
def load_config():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY not found in environment variables.")
        exit(1)
    return api_key

# Template Manager
def load_template():
    env = Environment(loader=FileSystemLoader("templete"))
    try:
        return env.get_template("prompt.txt")
    except Exception as e:
        print(f" Error in loading template: {e}")
        exit(1)

# Prompt Renderer
def render_prompt(template, question):
    if not question:
        print("Please enter a valid question.")
        return None
    return template.render(question=question)

MAX_PROMPT_TOKENS = 8000  # Or lower based on context limit and budget


# call OpenAI API 
def call_openai(client, prompt, stream=True, stream_delay=0.3):
    if not prompt:
        return None
        
  
    try:
       
        if len(prompt.split()) > MAX_PROMPT_TOKENS:
            return "InputTooLong."
            
    
        response = client.chat.completions.create(
            model="gpt-4o",  # GPT-4o model
            messages=[{"role": "user", "content": prompt}],
            stream=stream,
            temperature=0.7,
           
        )
        if stream:
           
            timestamp = datetime.now().strftime("%I:%M %p IST, %b %d, %Y")
            console.print(f"\n [bold]Response  at {timestamp}:[/bold]")
            full_response = ""
            for chunk in response:
                if chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    print(content, end="", flush=True)
                    full_response += content
                    time.sleep(stream_delay)
            print()
            return full_response
        return response.choices[0].message.content
    except Exception as e:
        return f" Error calling OpenAI API: {e}"
   

# Response Handler
def display_response(response):
    if response:
        print("\n📜 Response --------------------------------:")
        print("-" * 50)
        print(response)
        print("-" * 50)
        

# Main Controller
def main(question):
    
    # Initialize memory buffer (stores last 10 question-response pairs)
    memory = deque(maxlen=10)
    
    # Load configuration
    api_key = load_config()
    client = OpenAI(api_key=api_key)
    
    # Load template
    template = load_template()
  
    while True:
        # Exit condition
        if question.lower() == "exit":
            print("👋 Exiting the chat. Goodbye!")
            break
        
         # Prepare memory history
        memory_history = "\n".join([f"Q: {q}\nA: {r}" for q, r in memory]) if memory else "No previous conversation."
        
        # Render prompt with question and append memory history
        base_prompt = render_prompt(template, question)
        if not base_prompt:
            question = input("Ask Question: ").strip()
            continue
        prompt = f"Conversation History:\n{memory_history}\n\nCurrent Question:\n{question}\n\n{base_prompt}"
        
        
        # Call API and display response
        response = call_openai(client, prompt, stream=True, stream_delay=0.1)
        
        if response == "InputTooLong.":
            print(" ")
            print("Input too long. Please shorten your question.")
            print(" ")
            question = input("Ask Question: ").strip()
            continue
        elif response:
            # Store question-response pair in memory
            memory.append((question, response))
            # Display clarification prompt
            print(f"\n🔍 Clarification:")
            print(f"Did you mean {question} in another context or need further details?")
            display_response(response)

        # Ask the next question
        print("\nAsk another question or type 'exit' to quit.")
        question = input("Ask Question: ").strip()
        if question.lower() == "exit":
            print("👋 Exiting the chat. Goodbye!")
            break
       

if __name__ == "__main__":
    
    print("=== Mini Prompt System ===")
    print("Ask a question (e.g., 'What is Python?' or 'Explain quantum computing')")
    print("Type 'exit' to end the chat.")
    question = input("Ask Question: ").strip()
    if question.lower() == "exit":
        print("👋 Exiting before start.")
    else:
        main(question)