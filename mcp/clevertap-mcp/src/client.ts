import axios, { AxiosInstance } from "axios";
import * as dotenv from "dotenv";

dotenv.config();

export class CleverTapClient {
  private http: AxiosInstance;

  constructor() {
    const accountId = process.env.CLEVERTAP_ACCOUNT_ID;
    const passcode = process.env.CLEVERTAP_PASSCODE;

    if (!accountId || !passcode) {
      throw new Error(
        "Missing CLEVERTAP_ACCOUNT_ID or CLEVERTAP_PASSCODE in environment"
      );
    }

    this.http = axios.create({
      baseURL: "https://api.clevertap.com/1",
      headers: {
        "X-CleverTap-Account-Id": accountId,
        "X-CleverTap-Passcode": passcode,
        "Content-Type": "application/json",
      },
    });
  }

  async get<T>(path: string, params?: Record<string, unknown>): Promise<T> {
    const res = await this.http.get<T>(path, { params });
    return res.data;
  }

  async post<T>(path: string, body: unknown): Promise<T> {
    const res = await this.http.post<T>(path, body);
    return res.data;
  }
}
