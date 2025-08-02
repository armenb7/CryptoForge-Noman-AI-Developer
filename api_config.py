import os
from dotenv import load_dotenv
from langchain.llms import HuggingFaceHub
from langchain_community.utilities import SerpAPIWrapper
from langchain_community.llms import HuggingFaceEndpoint  # For xAI if adapted; use HF for now

# Load environment variables
load_dotenv()

# Hugging Face LLM (Llama 3)
hf_token = os.getenv("HF_TOKEN")
if hf_token:
    llm_hf = HuggingFaceHub(
        repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
        huggingfacehub_api_token=hf_token,
        model_kwargs={"temperature": 0.7, "max_new_tokens": 512}
    )
else:
    print("Warning: HF_TOKEN not set.")

# xAI Grok LLM (via API; adapt if xAI has direct LangChain support)
xai_key = os.getenv("XAI_API_KEY")
if xai_key:
    # Placeholder for xAI integration (use requests for now; full in Step 4)
    print("xAI API configured. Test via manual call.")
else:
    print("Warning: XAI_API_KEY not set.")

# SerpAPI Tool
serpapi_key = os.getenv("SERPAPI_API_KEY")
if serpapi_key:
    search_tool = SerpAPIWrapper()
else:
    print("Warning: SERPAPI_API_KEY not set.")

# Test Function
def test_apis():
    if 'llm_hf' in locals():
        print("Hugging Face Test:", llm_hf("What is a secure element for Bitcoin wallets?")[:100] + "...")
    if 'search_tool' in locals():
        print("SerpAPI Test:", search_tool.run("Best secure elements for Bitcoin hardware wallets 2025")[:100] + "...")
    if xai_key:
        # Manual xAI test (replace with actual API call in agents)
        print("xAI Test: Configure in agents; key present.")

if __name__ == "__main__":
    test_apis()
