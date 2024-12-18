import operator
from typing import Annotated, TypedDict
from dataclasses import dataclass, field


class SummaryState(TypedDict, total=False):
    research_topic: str 
    search_query: str
    web_search_result: Annotated[list, operator.add]
    sources_gathered: Annotated[list, operator.add] 
    research_loop_count: int
    running_summary: str 

class SummaryStateInput(TypedDict):
    research_topic: str

class SummaryStateOutput(TypedDict):
    running_summary: str