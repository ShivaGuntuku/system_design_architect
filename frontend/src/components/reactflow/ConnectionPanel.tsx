"use client";

import { useState } from "react";

interface ComponentOption {
  id: string;
  name: string;
}

interface Props {
  components: ComponentOption[];
  onCreateConnection: (
    sourceId: string,
    targetId: string
  ) => Promise<void>;
}

export default function ConnectionPanel({
  components,
  onCreateConnection,
}: Props) {
  const [sourceId, setSourceId] = useState("");
  const [targetId, setTargetId] = useState("");

  return (
    <div className="border p-4 w-64">
      <h2 className="font-bold mb-4">
        Create Connection
      </h2>

      <select
        value={sourceId}
        onChange={(e) =>
          setSourceId(e.target.value)
        }
        className="border w-full p-2 mb-3"
      >
        <option value="">
          Select Source
        </option>

        {components.map((component) => (
          <option
            key={component.id}
            value={component.id}
          >
            {component.name}
          </option>
        ))}
      </select>

      <select
        value={targetId}
        onChange={(e) =>
          setTargetId(e.target.value)
        }
        className="border w-full p-2 mb-3"
      >
        <option value="">
          Select Target
        </option>

        {components.map((component) => (
          <option
            key={component.id}
            value={component.id}
          >
            {component.name}
          </option>
        ))}
      </select>

      <button
        className="border p-2 w-full"
        onClick={() =>
          onCreateConnection(
            sourceId,
            targetId
          )
        }
      >
        Create Connection
      </button>
    </div>
  );
}