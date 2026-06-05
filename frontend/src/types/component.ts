export interface Component {
  id: string;
  architecture_id: string;
  name: string;
  component_type: string;
  config: Record<string, any>;
}