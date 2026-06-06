import { api } from "./api";

export const ComponentService = {
  async create(
    architectureId: string,
    componentType: string
  ) {

    const payload = {
      name:
        componentType +
        "-" +
        Date.now(),

      component_type:
        componentType,

      config: {},
    };

    const response =
      await api.post(
        `/architectures/${architectureId}/components`,
        payload
      );

    return response.data;
  },
  async updatePosition(
    componentId: string,
    x: number,
    y: number
  ) {
    return api.patch(
      `/components/${componentId}/position`,
      {
        x_position: x,
        y_position: y,
      }
    );
  }
};