## What is state?
States is the memory for the langgraph agent. It's essentially a list of dictionary
By default, the state will be overwritten or in every node. 
We can use typing Annotate and operator module to tell langgraph to add to the state instead of overwrite it.

### What we need:
1. query_agent: An agent that generate search query.
2. search_agent: An agent that search the web with the search query.
3. write_agent: An agent that generate write the summary of the search result.
4. review_agent: An agent review the summary so far and find the gaps. The gaps will go back to the search query agent.

For each agent we need a state to store the memory, to record what the agent has done so far.

## The workflow:
1. User give the query.
2. Convert the query into search query. (maybe 3 queries)
3. Search the web with the search query using Tavily.
4. Write the summary of the search result. If it already has a summary, combine the new summary with the old summary.
5. Review the summary so far and find the gaps.
6. Go back to step 2 for N times.

### How many states do we need?
1. query_agent: 1 state.
2. search_agent: 1 state.
3. write_agent: 1 state.
4. review_agent: 1 state.
