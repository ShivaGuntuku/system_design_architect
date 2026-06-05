interface Props {
  onAddComponent: (
    componentType: string
  ) => void;
}

const COMPONENT_TYPES = [
  "load_balancer",
  "api_service",
  "redis",
  "postgres",
  "mongodb",
];

export default function NodePalette({
  onAddComponent,
}: Props) {
  return (
    <div className="border p-4 w-64">
      <h2 className="font-bold mb-4">
        Components
      </h2>

      {COMPONENT_TYPES.map((type) => (
        <button
          key={type}
          onClick={() =>
            onAddComponent(type)
          }
          className="block w-full border p-2 mb-2"
        >
          {type}
        </button>
      ))}
    </div>
  );
}