"use client";

import { useEffect, useState } from "react";

import {
    Edge,
    Connection,
    useNodesState,
    useEdgesState,
} from "reactflow";

import ArchitectureCanvas from "@/src/components/reactflow/ArchitectureCanvas";
import NodePalette from "@/src/components/reactflow/NodePalette";

import { GraphService } from "@/src/services/graph";
import { ComponentService } from "@/src/services/component";
import { ConnectionService } from "@/src/services/connection";

import { GraphResponse } from "@/src/types/graph";

interface Props {
    params: Promise<{
        id: string;
    }>;
}

export default function ArchitecturePage({
    params,
}: Props) {

    const [graph, setGraph] =
        useState<GraphResponse | null>(null);

    const [
        nodes,
        setNodes,
        onNodesChange,
    ] = useNodesState([]);

    const [
        edges,
        setEdges,
        onEdgesChange,
    ] = useEdgesState([]);

    useEffect(() => {
        loadGraph();
    }, []);

    useEffect(() => {

        if (!graph) return;

        const mappedNodes = graph.components.map(
            (component, index) => ({
                id: component.id,

                type: "componentNode",

                position: {
                    x:
                        component.x_position,

                    y:
                        component.y_position,
                },

                data: {
                    label: component.name,
                    type: component.component_type,
                },
            })
        );

        const mappedEdges = graph.connections.map(
            (connection) => ({
                id: connection.id,
                source:
                    connection.source_component_id,
                target:
                    connection.target_component_id,
            })
        );

        setNodes(mappedNodes);
        setEdges(mappedEdges);

    }, [graph, setNodes, setEdges]);

    async function loadGraph() {

        const { id } = await params;

        const data =
            await GraphService.getGraph(id);

        setGraph(data);
    }

    async function addComponent(
        componentType: string
    ) {
        const { id } = await params;

        await ComponentService.create(
            id,
            componentType
        );

        await loadGraph();
    }

    async function handleNodeDragStop(
        _: any,
        node: any
    ) {
        try {
            await ComponentService.updatePosition(
                node.id,
                node.position.x,
                node.position.y
            );

            console.log(
                "Position saved",
                node.position
            );
        } catch (error) {
            console.error(error);
        }
    }

    async function handleConnect(
        connection: Connection
    ) {

        if (
            !connection.source ||
            !connection.target
        ) {
            return;
        }

        const { id } = await params;

        await ConnectionService.create(
            id,
            connection.source,
            connection.target
        );

        await loadGraph();
    }

    if (!graph) {
        return <div>Loading...</div>;
    }

    return (
        <div className="p-10">

            <h1 className="text-3xl font-bold mb-4">
                {graph.architecture.name}
            </h1>

            <p className="mb-6">
                {graph.architecture.description}
            </p>

            <div className="flex gap-4">

                <NodePalette
                    onAddComponent={addComponent}
                />

                <div className="flex-1">
                    <ArchitectureCanvas
                        nodes={nodes}
                        edges={edges}
                        onConnect={handleConnect}
                        onNodesChange={onNodesChange}
                        onEdgesChange={onEdgesChange}
                        onNodeDragStop={handleNodeDragStop}
                    />
                </div>

            </div>

        </div>
    );
}