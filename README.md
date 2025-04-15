Example MCP Server using Discit API
=========================

Clone
--------------
```bash
git clone https://github.com/jeremyary/disc-catalog.git
cd disc-catalog
```

Prerequisite(s)
---------------------------

Prior to running the app, create a local `.env` file & add your Anthropic API token - credit will be required as Claude is currently the LLM in use. (approx 1 cent per query)

```bash
touch .env
echo "ANTHROPIC_API_KEY=<your key here>" >> .env
echo ".env" >> .gitignore
```

Run the App
---------------------------

To run the application, execute the following command:

```bash
uv run client.py catalog.py
```

This will launch the application & result in a Query prompt.

Example Use
----------------------------
```
(disc-catalog) jary@jary-ubuntu:~/redhat/git/disc-catalog$ uv run client.py catalog.py
[04/15/25 13:56:06] INFO     Processing request of type ListToolsRequest                                                                                                                                                                                                                                                                      server.py:534

Connected to server with tools: ['get_disc_total_count', 'get_full_disc_list', 'get_discs_by_manufacturer_brand']

MCP Client Started!
Type your queries or 'quit' to exit.

Query: Recommend an understable putter for a low-power thrower
[04/15/25 13:56:22] INFO     Processing request of type ListToolsRequest                                                                                                                                                                                                                                                                      server.py:534
[04/15/25 13:56:25] INFO     Processing request of type CallToolRequest                                                                                                                                                                                                                                                                       server.py:534
                    INFO     HTTP Request: GET https://discit-api.fly.dev/disc "HTTP/1.1 200 OK"                                                                                                                                                                                                                                            _client.py:1740
                    INFO     disc list found (len: 1097)                                                                                                                                                                                                                                                                                      catalog.py:67

I'll help you by checking the available discs. Let me use the tools to get disc information.
[Calling tool get_full_disc_list with args {}]
Based on the data, here are some good understable putter options for a low-power thrower:

1. APX (Speed: 2, Turn: -1, Fade: 1) - A stable-understable putter with mild turn
2. Deputy (Speed: 3, Turn: -1.5, Fade: 0) - Very understable with minimal fade
3. Mirage (Speed: 3, Turn: -3, Fade: 0) - Very understable with no fade
4. Ruby (Speed: 3, Turn: -3, Fade: 1) - Very understable with minimal fade
5. Pure (Speed: 3, Turn: -1, Fade: 1) - Mild understability with controlled flight

Among these, I would specifically recommend the Deputy or Pure as they offer:
- Manageable speed (2-3)
- Consistent understable flight
- Low fade numbers that won't fight against the turn
- Good glide (4-5) to help maintain flight with lower power

The Deputy would be particularly good for a beginner as it has very low fade (0) and will hold an anhyzer line well while still being controllable.

```
