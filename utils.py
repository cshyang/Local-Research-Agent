from enum import unique
import os
from tavily import TavilyClient

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def tavily_search(query:str, max_results:int =3, include_raw_content:bool = True):
    tavily = TavilyClient(api_key=TAVILY_API_KEY)
    return tavily.search(query=query, max_results=max_results, include_raw_content=include_raw_content)

def dedupe_sources(sources: list):
    seen = set()
    unique_sources = []
    for source in sources:
        if source['url'] not in seen:
            unique_sources.append(source)
            seen.add(source['url'])
    return unique_sources

def format_web_search(results: list):
    formatted_results = "Source: \n"
    for result in results:
        formatted_results += f"Title: {result['title']}\n\n"
        formatted_results += f"URL: {result['url']}\n\n"
        formatted_results += f"Content: {result['content']}\n\n"
    return formatted_results

def format_sources_to_text(sources: list):
    formatted_sources = ""
    for source in sources:
        for key, value in source.items():
            formatted_sources += f"{key}: {value}\n"
    return formatted_sources