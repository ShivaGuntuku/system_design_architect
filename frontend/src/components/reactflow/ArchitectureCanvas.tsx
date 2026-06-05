"use client";

import ReactFlow, {
  Node,
  Edge,
} from "reactflow";

import "reactflow/dist/style.css";

import ComponentNode from "./ComponentNode";

const nodeTypes = {
  componentNode: ComponentNode,
};

interface Props {
  nodes: Node[];
  edges: Edge[];
  onConnect?: any;
}

export default function ArchitectureCanvas({
  nodes,
  edges,
  onConnect,
}: Props) {
  return (
    <div
      style={{
        width: "100%",
        height: "700px",
      }}
    >
      <ReactFlow
        nodes={nodes}
        edges={edges}
        nodeTypes={nodeTypes}
        fitView
        onConnect={onConnect}
      />
    </div>
  );
}