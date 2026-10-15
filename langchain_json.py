from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from pydantic import BaseModel, Field

load_dotenv()

LLM = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

class DessertRecipe(BaseModel):
    name: str = Field(description="Tatlı adı")
    preparation_time: int = Field(description="Dakika cinsinden hazırlama süresi")
    ingredients: list[str] = Field(description="Gerekli malzemeler listesi")
    calorie: int = Field(description="Tatlının yaklaşık kalorisi")

class DessertList(BaseModel):
    recipes: list[DessertRecipe] = Field(description="Tatlı tariflerinden oluşan bir liste")

parser = JsonOutputParser(pydantic_object=DessertList)

format_intructions = parser.get_format_instructions()
prompt = ChatPromptTemplate.from_template("Bana {fruit} ile yapılan 3 tatlı tarifi ver. \n{format_intructions}")
prompt = prompt.partial(format_intructions=format_intructions) 
# Her defasında tekrar invoke da belirtmektense böyle partial içinde tanımlanır

# LCEL ("|") (LangChain Expression Language) # Bu bir kavram
chain = prompt | LLM | parser

result = chain.invoke({"fruit": "Çilek"})

print(result)


