import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import { CleverTapClient } from "./client.js";
import { campaignTools } from "./tools/campaigns.js";
import { segmentTools } from "./tools/segments.js";
import { eventTools } from "./tools/events.js";
import { analyticsTools } from "./tools/analytics.js";

const allTools = [
  ...campaignTools,
  ...segmentTools,
  ...eventTools,
  ...analyticsTools,
];

const server = new Server(
  { name: "clevertap-mcp", version: "1.0.0" },
  { capabilities: { tools: {} } }
);

server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: allTools.map(({ name, description, inputSchema }) => ({
    name,
    description,
    inputSchema,
  })),
}));

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const tool = allTools.find((t) => t.name === request.params.name);
  if (!tool) {
    return {
      content: [{ type: "text", text: `Unknown tool: ${request.params.name}` }],
      isError: true,
    };
  }

  try {
    const client = new CleverTapClient();
    const result = await tool.handler(
      client,
      request.params.arguments as Record<string, unknown>
    );
    return {
      content: [{ type: "text", text: JSON.stringify(result, null, 2) }],
    };
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    return {
      content: [{ type: "text", text: `Error: ${message}` }],
      isError: true,
    };
  }
});

const transport = new StdioServerTransport();
server.connect(transport).then(() => {
  process.stderr.write("CleverTap MCP server running\n");
});
