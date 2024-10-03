# Startup Idea Generator

## Overview
This project builds a **Startup Idea Generator** web application using **Streamlit** and **Langchain**. The tool helps users generate a startup name and description based on a specific domain (e.g., Health, Education, Finance, etc.). It leverages the power of OpenAI’s language models to dynamically suggest unique startup ideas.

## Features:
- **Domain-Based Startup Suggestions**: Users can select from various domains like Health, Education, Finance, etc., and the app provides a creative startup name and a detailed description.
- **Streamlit Integration**: The application is built with Streamlit, offering an easy-to-run web interface for interactive user experiences.
- **OpenAI's GPT Integration**: The app uses OpenAI’s GPT model via the Langchain framework to generate creative startup names and descriptions based on user-selected domains.

---

## How It Works

### File: `main.py`

#### Imports and Environment Setup:
- The required packages (`streamlit`, `langchain`, `os`, and `langchain_helper`) are imported.
- The **OpenAI API key** is set using the `os.environ` variable to securely manage the API key.

#### Langchain Setup:
- The code defines two prompts using **Langchain**:
  - One prompt asks GPT to generate a startup name based on the selected domain.
  - The second prompt requests a description for the generated startup name.
- The `generate_startup_name_and_items` function in `langchain_helper.py` uses these prompts to generate a startup name and description dynamically.

#### Streamlit UI:
- The Streamlit application has a title: "**Startup Idea Generator**."
- A sidebar allows users to pick from different domains such as Health, Education, Finance, Travel, Food, Retail, and Real Estate.
- When the user selects a domain, the `langchain_helper.generate_startup_name_and_items` function is called to generate the startup name and description.
- The response is displayed in a clean, user-friendly format on the Streamlit app.

---

### File: `langchain_helper.py`
This file contains the Langchain logic for generating startup names and descriptions based on the selected domain.

#### LLMChain Setup:
- The **OpenAI GPT model** is instantiated with a `temperature` of 0.7, which controls the creativity level of the generated content.

#### Prompt Template:
- The `PromptTemplate` ensures that the model receives consistent input to generate relevant startup names and descriptions.
- The first prompt generates a startup name based on the selected domain.
- The second prompt generates a description for the generated startup name.

#### SequentialChain Execution:
- The **SequentialChain** handles the execution of these prompts in sequence. The first chain outputs the startup name, and the second chain uses this name to generate a corresponding description.

#### Return Output:
- The generated startup name and description are passed back to the Streamlit app for display.

---

## How to Run the Project

### 1. Install Dependencies:
You’ll need to install the following dependencies:

```bash
pip install streamlit
pip install langchain
pip install langchain_community
pip install openai

2. **Set OpenAI API Key**:
   You will need to set your OpenAI API key in a `secret_key.py` file or as an environment variable:
   ```python
   openapi_key = "your-openai-api-key-here"
   ```

3. **Run the Application**:
   Use the following command to run the app:
   ```bash
   streamlit run main.py
   ```

4. **Access the App**:
   Once the app is running, a browser window will open where you can select a job role from the sidebar. The app will then generate a list of technologies relevant to that role.

---
