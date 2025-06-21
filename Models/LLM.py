from crewai import LLM


llm = LLM(
    api_base= "http://192.168.56.1:1234/v1",
    api_key= "lm-studio",
    model= "openai/lmstudio-community/DeepSeek-R1-Distill-Qwen-7B-GGUF"
)


