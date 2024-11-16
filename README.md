# AI Chat CLI Application

This project provides a command-line interface (CLI) for interacting with large language models (LLMs) using LangChain.  It features a clean architecture, configuration management, and streaming responses for a better user experience.

## Features

- Interactive chat session with AI model
- Streaming responses for real-time interaction
- Markdown rendering for formatted output
- Configurable model parameters (temperature, max tokens)
- Robust error handling and input validation
- Easy environment configuration using a `.env` file

## Setup

1. **Install Dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   ```

2. **Set up `.env` file:**  Create a `.env` file in the project root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   MODEL_NAME=gpt-3.5-turbo  # Optional: Change the model name
   TEMPERATURE=0.7          # Optional: Adjust temperature
   MAX_TOKENS=1000         # Optional: Adjust max tokens
   ```

3. **Run the CLI:**
   ```bash
   python -m src.cli chat
   ```

## Architecture

The project is structured for maintainability and scalability:

- **`src/config.py`:** Handles configuration loading from the `.env` file using Pydantic.
- **`src/llm_chain.py`:** Contains the core logic for interacting with the LLM using LangChain.
- **`src/cli.py`:** Implements the CLI interface using Typer and Rich for a user-friendly experience.
- **`src/utils.py`:** Contains helper functions.
- **`requirements.txt`:** Lists project dependencies.


## Schema

The application's functioning is illustrated in the schema: `Schema_COT-REFLECT.png`.

## Contributing

Contributions are welcome!  Please open an issue or submit a pull request.
