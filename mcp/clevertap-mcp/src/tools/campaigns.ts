import { CleverTapClient } from "../client.js";

export const campaignTools = [
  {
    name: "list_campaigns",
    description: "List CleverTap campaigns within a date range",
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
      const data = await client.get("/targets/list.json", {
        from: args.from,
        to: args.to,
      });
      return data;
    },
  },
  {
    name: "get_campaign_stats",
    description:
      "Get performance stats for a specific CleverTap campaign (sent, delivered, opened, clicked, converted)",
    inputSchema: {
      type: "object",
      properties: {
        campaign_id: {
          type: "string",
          description: "CleverTap campaign ID",
        },
      },
      required: ["campaign_id"],
    },
    handler: async (
      client: CleverTapClient,
      args: { campaign_id: string }
    ) => {
      const data = await client.get(`/targets/${args.campaign_id}/result.json`);
      return data;
    },
  },
  {
    name: "create_push_campaign",
    description: "Create a one-time push notification campaign in CleverTap",
    inputSchema: {
      type: "object",
      properties: {
        name: { type: "string", description: "Campaign name" },
        title: { type: "string", description: "Push notification title" },
        body: { type: "string", description: "Push notification body" },
        deep_link: {
          type: "string",
          description: "Deep link URL (e.g. app://food/promo)",
        },
        schedule_time: {
          type: "string",
          description: "Schedule datetime YYYY-MM-DD HH:MM (local time)",
        },
        segment_name: {
          type: "string",
          description: "Target segment/list name",
        },
      },
      required: ["name", "title", "body", "schedule_time"],
    },
    handler: async (
      client: CleverTapClient,
      args: {
        name: string;
        title: string;
        body: string;
        deep_link?: string;
        schedule_time: string;
        segment_name?: string;
      }
    ) => {
      const payload: Record<string, unknown> = {
        name: args.name,
        when: args.schedule_time,
        channel: "push",
        content: {
          title: args.title,
          body: args.body,
          ...(args.deep_link && {
            platform_specific: {
              android: { deep_link: args.deep_link },
              ios: { deep_link: args.deep_link },
            },
          }),
        },
        respect_frequency_caps: true,
        respect_DND: true,
      };

      if (args.segment_name) {
        payload.where = { segment: { name: args.segment_name } };
      }

      const data = await client.post("/targets/create.json", payload);
      return data;
    },
  },
  {
    name: "send_transactional_push",
    description:
      "Send a transactional push notification to a specific user (bypasses frequency caps)",
    inputSchema: {
      type: "object",
      properties: {
        identity: {
          type: "string",
          description: "User identity (user ID)",
        },
        title: { type: "string", description: "Push title" },
        body: { type: "string", description: "Push body" },
        deep_link: { type: "string", description: "Deep link URL" },
      },
      required: ["identity", "title", "body"],
    },
    handler: async (
      client: CleverTapClient,
      args: {
        identity: string;
        title: string;
        body: string;
        deep_link?: string;
      }
    ) => {
      const payload: Record<string, unknown> = {
        to: { identity: [args.identity] },
        tag_group: "default",
        respect_frequency_caps: false,
        content: {
          title: args.title,
          body: args.body,
          ...(args.deep_link && {
            platform_specific: {
              android: { deep_link: args.deep_link },
              ios: { deep_link: args.deep_link },
            },
          }),
        },
      };
      const data = await client.post("/send/push.json", payload);
      return data;
    },
  },
];
