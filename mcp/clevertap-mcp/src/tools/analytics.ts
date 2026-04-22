import { CleverTapClient } from "../client.js";

export const analyticsTools = [
  {
    name: "get_campaign_performance_summary",
    description:
      "Get a formatted performance summary for multiple campaigns in a date range",
    inputSchema: {
      type: "object",
      properties: {
        from: { type: "string", description: "Start date YYYYMMDD" },
        to: { type: "string", description: "End date YYYYMMDD" },
      },
      required: ["from", "to"],
    },
    handler: async (
      client: CleverTapClient,
      args: { from: string; to: string }
    ) => {
      const listResponse = await client.get<{ targets?: { id: string; name: string }[] }>(
        "/targets/list.json",
        { from: args.from, to: args.to }
      );

      const targets = listResponse.targets ?? [];
      const results = await Promise.all(
        targets.map(async (t) => {
          try {
            const stats = await client.get<Record<string, unknown>>(
              `/targets/${t.id}/result.json`
            );
            return { id: t.id, name: t.name, ...stats };
          } catch {
            return { id: t.id, name: t.name, error: "Failed to fetch stats" };
          }
        })
      );

      return results;
    },
  },
  {
    name: "get_user_profile",
    description: "Look up a user profile in CleverTap by identity",
    inputSchema: {
      type: "object",
      properties: {
        identity: { type: "string", description: "User identity (user ID)" },
      },
      required: ["identity"],
    },
    handler: async (client: CleverTapClient, args: { identity: string }) => {
      const data = await client.get("/profile.json", {
        identity: args.identity,
      });
      return data;
    },
  },
];
