import { CleverTapClient } from "../client.js";

export const eventTools = [
  {
    name: "upload_event",
    description: "Upload a single user event to CleverTap",
    inputSchema: {
      type: "object",
      properties: {
        identity: { type: "string", description: "User identity (user ID)" },
        event_name: {
          type: "string",
          description: "Event name (e.g. 'Order Placed')",
        },
        event_properties: {
          type: "object",
          description: "Key-value event properties",
        },
        timestamp: {
          type: "number",
          description: "Unix epoch timestamp (optional, defaults to now)",
        },
      },
      required: ["identity", "event_name"],
    },
    handler: async (
      client: CleverTapClient,
      args: {
        identity: string;
        event_name: string;
        event_properties?: Record<string, unknown>;
        timestamp?: number;
      }
    ) => {
      const payload = {
        d: [
          {
            identity: args.identity,
            ts: args.timestamp ?? Math.floor(Date.now() / 1000),
            type: "event",
            evtName: args.event_name,
            evtData: args.event_properties ?? {},
          },
        ],
      };
      const data = await client.post("/upload", payload);
      return data;
    },
  },
  {
    name: "get_event_stats",
    description: "Get aggregate stats for a specific event over a date range",
    inputSchema: {
      type: "object",
      properties: {
        event_name: { type: "string", description: "Event name" },
        from: {
          type: "string",
          description: "Start date YYYYMMDD",
        },
        to: {
          type: "string",
          description: "End date YYYYMMDD",
        },
      },
      required: ["event_name", "from", "to"],
    },
    handler: async (
      client: CleverTapClient,
      args: { event_name: string; from: string; to: string }
    ) => {
      const data = await client.post("/counts/events.json", {
        event_name: args.event_name,
        from: parseInt(args.from),
        to: parseInt(args.to),
      });
      return data;
    },
  },
  {
    name: "update_user_profile",
    description: "Update a user's profile properties in CleverTap",
    inputSchema: {
      type: "object",
      properties: {
        identity: { type: "string", description: "User identity (user ID)" },
        profile_data: {
          type: "object",
          description:
            "Profile properties to set (e.g. Name, Phone, custom_user_type)",
        },
      },
      required: ["identity", "profile_data"],
    },
    handler: async (
      client: CleverTapClient,
      args: { identity: string; profile_data: Record<string, unknown> }
    ) => {
      const payload = {
        d: [
          {
            identity: args.identity,
            ts: Math.floor(Date.now() / 1000),
            type: "profile",
            profileData: args.profile_data,
          },
        ],
      };
      const data = await client.post("/upload", payload);
      return data;
    },
  },
];
