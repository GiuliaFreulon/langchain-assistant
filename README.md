# English Assistant with LangChain and Groq

This project is an English assistant that uses [LangChain](https://python.langchain.com/) and Groq to answer questions, correct sentences, suggest translations, and explain concepts in a didactic way.

## Requirements

- Python 3.8+
- A Groq API key (free)

## Installation

1. Clone the repository.
2. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Rename the `.env_example` file to `.env` and add your Groq API key.

## Usage

Run the assistant:
```sh
python app.py
```

Type your questions in English or Portuguese. To exit, type `sair` or `exit`.