from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.callbacks import StreamingStdOutCallbackHandler
from .config import settings

class LLMChainManager:
    """Manages the LLM chain configuration and execution."""
    
    def __init__(self):
        self.llm = ChatOpenAI(
            api_key=settings.openai_api_key,
            model_name=settings.model_name,
            temperature=settings.temperature,
            max_tokens=settings.max_tokens,
            streaming=True,
            callbacks=[StreamingStdOutCallbackHandler()]
        )
        
        self.prompt = ChatPromptTemplate.from_template(
            "You are a helpful AI assistant. "
            "Please provide a detailed and accurate response to the following question:\n\n"
            "{question}"
        )
        
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)
    
    async def get_response(self, question: str) -> str:
        """
        Get a response from the LLM chain.
        
        Args:
            question (str): The user's question
            
        Returns:
            str: The model's response
        """
        try:
            response = await self.chain.arun(question=question)
            return response
        except Exception as e:
            return f"Error: {str(e)}"
