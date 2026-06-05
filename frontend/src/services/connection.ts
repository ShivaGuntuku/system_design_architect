import { api } from "./api";

export const ConnectionService = {
  async create(
    architectureId: string,
    sourceComponentId: string,
    targetComponentId: string
  ) {
    const payload = {
      source_component_id: sourceComponentId,
      target_component_id: targetComponentId,
    };

    const response = await api.post(
      `/architectures/${architectureId}/connections`,
      payload
    );

    return response.data;
  },
};