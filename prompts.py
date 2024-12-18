query_generation_prompt = """
<purpose>
Your goal is to generate targeted web search query based on given research topic.
Your query will gather information related to the research topic.
Topic: {research_topic}
</purpose>

<instructions>
1. Based on the research topic, generate a focused search query
2. Identify a specific aspect of the topic to investigate
3. Provide a clear rationale for your choices
</instructions>

<output_format>
Return the result in a JSON format following:
    {{"search_query": "string", "aspect": "string", "rationale": "string}}

Only return the output in JSON format.
</output_format>

"""


summarizer_prompt = """
<purpose>
Your goal is to generate a high quality summary of the given search result in a article format.
</purpose>
<instructions>

<instruction>
When extending an existing summary: 
1. Only add new information and avoid repeating existing information.
2. Seamlessly integrate new information into the existing summary.
3. Ensure smooth transitions between existing and new content
</instruction>

<instruction>
When creating a new summary:
1. Highlight the key points from the sources.
2. Provide concise overview of the key points related to the topic.
3. Emphasize the most significant findings
4. Ensure a coherent flow of information
</instruction>

<instruction>
In both cases:
1. Focus on factual information, avoiding opinion or speculation.
2. Avoid repetitive or redundant information.
3. Write in a clear and enaging format to empahsize story telling.
4. At the end of the summary, you are allowed to provide an opition or prediction based on the understanding of the topic.
5. If an opition or prediction is provided, please declare and explain your opition or prediction.
</instruction>

</instructions>

<output_format>
The output should be written in a article format with headlines and paragraphs.
</output_format>

"""

reflection_prompt = """
<purpose>
Your goal is to review the summary so far and find the gaps.
</purpose>

<instructions>
1. Analyze the summary and identify any gaps required deeper exploration.
2. Generate a follow-up search query that will help to expand your understanding of the topic.
3. The search query should be short, not more than 50 characters, and optimize for web search.
4. Focus on technical details, implementation specifies, or emerging trends that weren't fully covered.
5. Your follow-up question should be specific and have a clear objective for web search.
</instructions>

<output_format>
Here is the output schema:
{reflection_schema}

Only return the output in JSON format. Do not include any other text, markdown formatting, or additional fields.
</output_format>
"""