import asyncio
import typer
from rich.console import Console
from rich.markdown import Markdown
from .llm_chain import LLMChainManager

app = typer.Typer()
console = Console()

@app.command()
def chat():
    """Start an interactive chat session with the AI model."""
    console.print("[bold green]Welcome to the AI Chat CLI![/bold green]")
    console.print("Type 'exit' to quit the application.\n")
    
    chain_manager = LLMChainManager()
    
    async def chat_loop():
        while True:
            question = typer.prompt("You")
            
            if question.lower() == 'exit':
                console.print("\n[bold green]Goodbye![/bold green]")
                break
            
            try:
                console.print("\n[bold blue]AI Assistant:[/bold blue]")
                response = await chain_manager.get_response(question)
                console.print(Markdown(response))
                console.print("\n")
            except Exception as e:
                console.print(f"[bold red]Error: {str(e)}[/bold red]\n")
    
    asyncio.run(chat_loop())
