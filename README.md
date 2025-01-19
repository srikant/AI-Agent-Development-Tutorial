# Simple AI Agent Programs

This repository contains 10 simple AI agent programs, each designed to demonstrate a unique use case for AI or automation. These programs are beginner-friendly and serve as excellent examples of how AI can solve various problems or enhance productivity.

---

## AI Agents Overview

### 1. Basic Chatbot with GPT-3.5 API

- **File**: `basic_chatbot.py`
- **Description**: A text-based chatbot that uses the OpenAI API (GPT-3.5) to generate conversational responses based on user input.
- **Features**:
  - Interactive chat
  - Natural language understanding
- **Dependencies**: `openai`

---

### 2. Simple Chatbot with Hugging Face GPT-2

- **File**: `chatbot_huggingface.py`
- **Description**: A locally-run chatbot that uses Hugging Face's GPT-2 model to respond to user input.
- **Features**:
  - Offline support (no API required)
  - Lightweight and flexible
- **Dependencies**: `transformers`

---

### 3. Voice-to-Text AI Agent with OpenAI Whisper

- **File**: `voice_to_text_agent.py`
- **Description**: Accepts voice input via a microphone, transcribes it to text, and interacts with the user using GPT-3.5 for responses.
- **Features**:
  - Speech-to-text with `SpeechRecognition`
  - Text-based interaction
- **Dependencies**: `speechrecognition`, `openai`, `pyaudio`

---

### 4. Keyword-Based AI Chatbot

- **File**: `keyword_chatbot.py`
- **Description**: Responds to user input based on predefined keywords and phrases, simulating intelligence without requiring external APIs.
- **Features**:
  - Simple and fast
  - Fully customizable keyword-response pairs

---

### 5. Random Advice Generator

- **File**: `advice_generator.py`
- **Description**: Provides random motivational or practical advice from a predefined list.
- **Features**:
  - Randomized responses
  - No external dependencies

---

### 6. Weather Simulation AI Agent

- **File**: `weather_simulator.py`
- **Description**: Simulates weather conditions for a given location, including temperature and weather type.
- **Features**:
  - Random weather generation
  - Simple text-based interaction

---

### 7. Quiz Bot with Multiple-Choice Questions

- **File**: `quiz_bot.py`
- **Description**: A fun and interactive quiz bot that asks multiple-choice questions, checks user answers, and tracks the score.
- **Features**:
  - Randomized questions
  - Score tracking
- **Dependencies**: None

---

### 8. Math Assistant AI Agent

- **File**: `math_assistant.py`
- **Description**: Solves user-provided mathematical expressions and returns the result.
- **Features**:
  - Handles arithmetic and advanced math functions
  - Secure evaluation using Python’s `math` library

---

### 9. Knowledge Base AI Agent

- **File**: `knowledge_base_agent.py`
- **Description**: A question-answering chatbot that uses a predefined knowledge base to simulate intelligence.
- **Features**:
  - Offline capability
  - Expandable knowledge base

---

### 10. Task Manager AI Agent

- **File**: `task_manager.py`
- **Description**: A personal task manager that allows users to add, view, and mark tasks as complete.
- **Features**:
  - Simple menu interface
  - Task tracking and completion management
- **Dependencies**: None

---

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/srikant/AI-Agent-Development-Tutorial.git
   cd AI-Agent-Development-Tutorial
   ```
2. Install any required dependencies listed in each script using
   ```bash
   pip install <dependency>
   ```
3. Run the desired program

````bash
  python <file_name>.py
  ```
````

## Contribution

Feel free to fork this repository and contribute by adding more AI agents or enhancing the existing ones. Pull requests are welcome!

## License

This project is licensed under the MIT License.

## Author

This repository was created by Srikanth Dhondi, a passionate software professional with expertise in artificial intelligence, machine learning, and innovative software solutions. Srikanth thrives on building tools that simplify complex tasks and help others learn the power of AI. Connect with him on **[LinkedIn](https://www.linkedin.com/in/srikanthdhondi/)** to explore his latest projects and insights into the tech world.
