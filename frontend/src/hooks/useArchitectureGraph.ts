import { useEffect, useState } from "react";

export function useArchitectureGraph(
  architectureId: string
) {
  const [graph, setGraph] = useState(null);

  async function loadGraph() {}

  return {
    graph,
    loadGraph,
  };
}