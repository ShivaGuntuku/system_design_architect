import { api } from "./api";
import { Architecture } from "../types/architecture";

export const ArchitectureService = {
  async getAll(): Promise<Architecture[]> {
    const response = await api.get("/architectures");
    return response.data;
  },

  async create(data: {
    name: string;
    description?: string;
  }): Promise<Architecture> {
    const response = await api.post(
      "/architectures",
      data
    );

    return response.data;
  },
};