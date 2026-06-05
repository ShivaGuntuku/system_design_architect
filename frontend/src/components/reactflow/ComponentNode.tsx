"use client";

import { Handle, Position } from "reactflow";

interface Props {
  data: {
    label: string;
    type: string;
  };
}

export default function ComponentNode({
  data,
}: Props) {
  return (
    <div
      className="
      bg-white
      border
      rounded-lg
      shadow-md
      min-w-[180px]
      "
    >
      <Handle
        type="target"
        position={Position.Top}
      />

      <div className="p-4">

        <div className="font-bold">
          {data.label}
        </div>

        <div
          className="
          text-xs
          text-gray-500
          mt-1
          "
        >
          {data.type}
        </div>

      </div>

      <Handle
        type="source"
        position={Position.Bottom}
      />
    </div>
  );
}