
# Moody AI

A simple AI agent that responds to messages based on its current mood. The agent randomly switches between different moods (happy, sad, angry, excited, bored, relaxed) and adjusts its responses accordingly.

## Overview

This project implements a moody AI agent using:
- Phoenix framework for AI agent implementation
- MCP (Model Context Protocol) for mood server communication
- Github Models (Azure AI) for language model inference

## Requirements

- Python 3.13+
- uv (Python package manager)
- Access to Github Models
- Required Python packages:
  - phoenix-agents

## Setup

1. Clone the repository
2. Install dependencies:
```bash
uv add phoenix-agents
```
3. Create a `.env` file in the root directory with:
```
GITHUB_TOKEN=your_github_token_here
```

## Project Structure

```
moody/
├── main.py           # Main application entry point
├── servers/
│   └── mood.py      # Mood server implementation
└── utils.py         # Utility functions
```

## Usage

Run the application:

```bash
uv run main.py
```
