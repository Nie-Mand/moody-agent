from dotenv import load_dotenv
import asyncio
import os

from phoenix.agent import Agent
from phoenix.user_session import UserSession
from phoenix.models.azure_ai_inference import AzureAIInferece
import phoenix.models.openai_history as openai_history
from phoenix.connectors.mcp import MCPClient, MCPServer
import utils

load_dotenv()

async def main():
    # Initialize chat history
    chat_history = openai_history.ChatHistory()

    # Setup LLM with Azure AI
    llm = AzureAIInferece(
        token=os.getenv("GITHUB_TOKEN"),
        history=chat_history
    )

    # Setup MCP connector with servers
    get = utils.mcp_servers_path_getter()
    mcp = MCPClient([
        MCPServer(path=get("mood.py"))
    ])

    try:
        await mcp.connect()

        # Create agent
        agent = Agent(
            brain=llm,
            history=chat_history,
            connector=mcp,
            system="You are a moody AI, you need to know your current mood to know how to respond.",
        )

        # Create user session and interact
        session = UserSession()
        response = await agent.call("Hello, how are you?", session)
        print(response)

    finally:
        await mcp.cleanup()

if __name__ == "__main__":
    asyncio.run(main())
