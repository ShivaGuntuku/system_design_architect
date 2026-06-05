import { api } from "./api";
import { GraphResponse } from "@/src/types/graph";

export const GraphService = {
  async getGraph(
    architectureId: string
  ): Promise<GraphResponse> {

    const response = await api.get(
      `/architectures/${architectureId}/graph`
    );

    return response.data;
  },
};