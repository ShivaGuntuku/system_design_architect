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
  onNodesChange?: any;
  onEdgesChange?: any;
  onNodeDragStop?: any;
}

export default function ArchitectureCanvas({
  nodes,
  edges,
  onConnect,
  onNodesChange,
  onEdgesChange,
  onNodeDragStop,
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
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onNodeDragStop={onNodeDragStop}
        
      />
    </div>
  );
}