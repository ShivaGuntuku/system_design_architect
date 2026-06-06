export interface GraphComponent {
  id: string;
  architecture_id: string;
  name: string;
  component_type: string;
  config: Record<string, any>;
  x_position: number;
  y_position: number;
}

export interface GraphConnection {
  id: string;
  source_component_id: string;
  target_component_id: string;
}

export interface GraphResponse {
  architecture: {
    id: string;
    name: string;
    description?: string;
  };

  components: GraphComponent[];

  connections: GraphConnection[];

  stats: {
    total_components: number;
    total_connections: number;
  };
}