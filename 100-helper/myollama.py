#from langchain.llms import Ollama
from langchain_community.llms import Ollama


llm = Ollama(model="codellama")

print(llm.invoke("Hello, how are you?"))

