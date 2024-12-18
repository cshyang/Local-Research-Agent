from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser

class SummaryStateOutputParser(BaseModel):
    query: str = Field(description="The search query")
    aspect: str = Field(description="The specific aspect or focus area of the search")
    rational: str = Field(description="Reason to select this query and aspect")


class ReflectionOutputParser(BaseModel):
    knowledge_gaps: str = Field(description="The gaps required deeper exploration")
    follow_up_query: str = Field(description="The follow-up question")
    
summary_state_parser = JsonOutputParser(pydantic_object=SummaryStateOutputParser)

reflection_parser = JsonOutputParser(pydantic_object=ReflectionOutputParser)