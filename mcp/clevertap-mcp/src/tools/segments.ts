import { CleverTapClient } from "../client.js";

export const segmentTools = [
  {
    name: "create_segment_list",
    description:
      "Create a static user list (segment) in CleverTap from a list of user identities",
    inputSchema: {
      type: "object",
      properties: {
        name: { type: "string", description: "Segment name" },
        description: { type: "string", description: "Segment description" },
        user_ids: {
          type: "array",
          items: { type: "string" },
          description: "Array of user identity strings",
        },
      },
      required: ["name", "user_ids"],
    },
    handler: async (
      client: CleverTapClient,
      args: { name: string; description?: string; user_ids: string[] }
    ) => {
      const payload = {
        name: args.name,
        description: args.description ?? "",
        source: "manual",
        users: args.user_ids.map((id) => ({ identity: id })),
      };
      const data = await client.post("/lists/create.json", payload);
      return data;
    },
  },
  {
    name: "get_segment_list",
    description: "Get details of a CleverTap user list/segment by ID",
    inputSchema: {
      type: "object",
      properties: {
        list_id: { type: "string", description: "CleverTap list ID" },
      },
      required: ["list_id"],
    },
    handler: async (client: CleverTapClient, args: { list_id: string }) => {
      const data = await client.get("/lists/get.json", {
        list_id: args.list_id,
      });
      return data;
    },
  },
];
