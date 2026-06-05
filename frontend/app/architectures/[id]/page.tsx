"use client";
import { useEffect, useState } from "react";
import { GraphService } from "@/src/services/graph";
import { GraphResponse } from "@/src/types/graph";
import { Node, Edge } from "reactflow";
import ArchitectureCanvas from "@/src/components/reactflow/ArchitectureCanvas";
import NodePalette from "@/src/components/reactflow/NodePalette";

import { ComponentService } from "@/src/services/component";
// import ConnectionPanel from "@/src//components/reactflow/ConnectionPanel";
import { ConnectionService } from "@/src//services/connection";
import { Connection } from "reactflow";

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

    useEffect(() => {
        loadGraph();
    }, []);

    async function loadGraph() {

        const { id } = await params;

        const data =
            await GraphService.getGraph(id);

        setGraph(data);
    }

    if (!graph) {
        return <div>Loading...</div>;
    }

    // const nodes: Node[] = graph.components.map(
    //     (component, index) => ({
    //         id: component.id,

    //         data: {
    //             label: component.name,
    //         },

    //         position: {
    //             x: 250,
    //             y: index * 150,
    //         },
    //     })
    // );

    const nodes = graph.components.map(
        (component, index) => ({
            id: component.id,

            type: "componentNode",

            position: {
                x: 250,
                y: index * 150,
            },

            data: {
                label: component.name,
                type: component.component_type,
            },
        })
    );

    const edges: Edge[] =
        graph.connections.map((connection) => ({
            id: connection.id,

            source:
                connection.source_component_id,

            target:
                connection.target_component_id,
        }));

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

    async function createConnection(
        sourceId: string,
        targetId: string
    ) {
        const { id } = await params;

        await ConnectionService.create(
            id,
            sourceId,
            targetId
        );

        await loadGraph();
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
    return (
        <div className="p-10">

            <h1 className="text-3xl font-bold mb-4">
                {graph.architecture.name}
            </h1>

            <p className="mb-2">
                {graph.architecture.description}
            </p>

            {/* <div className="flex gap-4">

                <NodePalette
                    onAddComponent={
                        addComponent
                    }
                />

                <div className="flex-1">

                    <ArchitectureCanvas
                        nodes={nodes}
                        edges={edges}
                    />

                </div>

            </div> */}
            <div className="flex gap-4">

                <NodePalette
                    onAddComponent={addComponent}
                />

                {/* <ConnectionPanel
                    components={graph.components.map(
                        (component) => ({
                            id: component.id,
                            name: component.name,
                        })
                    )}
                    onCreateConnection={
                        createConnection
                    }
                /> */}

                <div className="flex-1">
                    <ArchitectureCanvas
                        nodes={nodes}
                        edges={edges}
                        onConnect={handleConnect}
                    />
                </div>

            </div>

        </div>
    );
}