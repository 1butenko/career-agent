# AI Career Agent

An AI-powered website chat assistant that represents a person professionally, answering questions about their career, background, skills, and experience using a resume and personal description.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Required Files](#required-files)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Configuration](#configuration)
- [How It Works](#how-it-works)
- [Tool Functions](#tool-functions)
- [Security Notes](#security-notes)
- [Limitations](#limitations)
---

## Overview

This project implements an AI agent that acts as a **digital representative** on a personal or professional website.

The agent:
- Answers career-related questions using real resume data
- Uses a personal description as contextual background
- Records unanswered questions for follow-up
- Collects user contact details when appropriate
- Sends push notifications for important interactions

The chat interface is exposed via **Gradio**, making it easy to deploy and test locally or on the web.

---

## Features

- ✅ AI agent that maintains professional character
- 📄 Reads and understands resume (PDF) and personal description (TXT)
- 🔧 OpenAI function (tool) calling for structured interactions
- 📝 Records unknown questions and user contact details
- 🔔 Push notifications via **Pushover**
- 💬 Web-based chat UI with **Gradio**
- 🎯 Context-aware responses based on actual career information

---

## Tech Stack

- **Python 3.9+**
- **OpenAI API** – GPT models with function calling
- **Gradio** – Interactive web UI
- **PyPDF** – PDF text extraction
- **python-dotenv** – Environment variable management
- **Requests** – HTTP client for notifications

---

## Project Structure
```
.
├── agent.py                      # Core AI agent logic
├── main.py                       # App entry point (Gradio UI)
├── api.py                        # Tool implementations
├── tools/
│   ├── read_json.py
│   ├── unknown_question.tool.json
│   └── user_details.tool.json
├── resume.pdf                    # REQUIRED – user-provided
├── description.txt               # REQUIRED – user-provided
├── .env                          # REQUIRED – user-provided
└── README.md
```

---

## Requirements

- Python 3.9 or higher
- OpenAI API key
- Internet connection
- (Optional) Pushover account for notifications

---

## Installation

### 1. Clone or download the repository
```bash
git clone <repository-url>
cd ai-career-agent
```

### 2. Install dependencies
```bash
pip install openai gradio python-dotenv pypdf requests
```

Or use a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install openai gradio python-dotenv pypdf requests
```

---

## Required Files

### `resume.pdf`

A PDF resume of the person the agent represents.  
The agent extracts text from this file and uses it as factual context for answering questions.

**What to include:**
- Work experience
- Education
- Skills
- Projects
- Contact information (optional)

---

### `description.txt`

A short professional summary or bio that provides additional context about the person.

**Example:**
```
Senior software engineer with 5+ years of experience in AI, startups, and full-stack development. 
Passionate about building intelligent systems and solving complex problems.
```

---

## Environment Variables

Create a `.env` file in the project root:
```env
OPENAI_API_KEY=your_openai_api_key
PUSHOVER_TOKEN=your_pushover_app_token
PUSHOVER_USER=your_pushover_user_key
```

### Getting API Keys:

- **OpenAI API Key:** Sign up at [platform.openai.com](https://platform.openai.com)
- **Pushover (optional):** Create an account at [pushover.net](https://pushover.net)

⚠️ **Never commit this file to version control.** Add `.env` to your `.gitignore`.

---

## Usage

### Run the application:
```bash
python main.py
```

### After startup:

1. A Gradio URL will appear in the terminal (e.g., `http://127.0.0.1:7860`)
2. Open it in your browser to start chatting with the agent
3. Ask questions about the person's career, skills, or experience
4. The agent will respond based on the resume and description

### Example interactions:

- "What programming languages do you know?"
- "Tell me about your work experience"
- "What projects have you worked on?"
- "How can I contact you?"

---

## Configuration

### Change Agent Name

In `main.py`:
```python
agent = Agent(name="Your Name Here", tools=tools, openai=openai)
```

### Modify Agent Behavior

Edit the `system_prompt()` method in `agent.py` to:

- Change tone (formal, casual, technical)
- Add constraints or guidelines
- Adjust conversation strategy
- Define response boundaries

### Add or Remove Tools

Tool schemas are defined as JSON files in the `tools/` directory.

**To add a new tool:**

1. Create a function in `api.py`
2. Define its JSON schema in `tools/`
3. Register it in the agent's tool list

---

## How It Works

1. **Initialization:**
   - Resume and description are loaded at startup
   - System prompt is dynamically generated with context

2. **User Interaction:**
   - User messages are sent to OpenAI API
   - Agent processes the query with resume context

3. **Tool Calling:**
   - If a tool call is triggered (e.g., user provides email)
   - The corresponding function executes
   - Result is returned to the model

4. **Response:**
   - Final response is generated and shown to user
   - Notifications sent if configured

---

## Tool Functions

### `record_user_details`

**Purpose:** Stores user email and optional metadata (name, company, etc.)

**When triggered:** User provides contact information during conversation

**Actions:**
- Saves contact details
- Sends Pushover notification (if configured)

---

### `record_unknown_question`

**Purpose:** Records questions the agent could not answer adequately

**When triggered:** Agent encounters a question outside its knowledge base

**Actions:**
- Logs the question for review
- Sends notification to owner
- Helps improve future responses

---

## Security Notes

### Do NOT commit:

- `.env` file (contains API keys)
- `resume.pdf` (personal information)
- `description.txt` (if it contains sensitive data)

### Best Practices:

- Add these files to `.gitignore`
- Use environment variables for all secrets
- Treat user emails as sensitive data
- Use HTTPS when deploying publicly
- Consider rate limiting for public deployments
- Regularly rotate API keys

---

## Limitations

- No persistent storage by default (data not saved between sessions)
- Resume context is static at startup (requires restart to update)
- Designed for single-persona use (one agent per instance)
- Depends on OpenAI API availability
- Limited to information in resume and description

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## Support

For questions or issues, please open an issue on the repository or contact the maintainer.

---

**Built with ❤️ using OpenAI and Gradio**