"use client";

import { useEffect, useState } from "react";
import Link from "next/link";

import { Architecture } from "@/src/types/architecture";
import { ArchitectureService } from "@/src/services/architecture";

export default function Home() {
  const [architectures, setArchitectures] = useState<
    Architecture[]
  >([]);

  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  useEffect(() => {
    loadArchitectures();
  }, []);

  async function loadArchitectures() {
    try {
      const data =
        await ArchitectureService.getAll();

      setArchitectures(data);
    } catch (error) {
      console.error(error);
    }
  }

  async function createArchitecture() {
    try {
      await ArchitectureService.create({
        name,
        description,
      });

      setName("");
      setDescription("");

      await loadArchitectures();
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div className="p-10">
      <h1 className="text-3xl font-bold mb-6">
        Architectures
      </h1>

      <div className="mb-8 flex gap-2">
        <input
          value={name}
          onChange={(e) =>
            setName(e.target.value)
          }
          placeholder="Architecture Name"
          className="border p-2"
        />

        <input
          value={description}
          onChange={(e) =>
            setDescription(e.target.value)
          }
          placeholder="Description"
          className="border p-2"
        />

        <button
          onClick={createArchitecture}
          className="border px-4"
        >
          Create
        </button>
      </div>

      {architectures.map((architecture) => (
        <Link
          key={architecture.id}
          href={`/architectures/${architecture.id}`}
        >
          <div className="border rounded p-4 mb-3 cursor-pointer">
            <h2 className="font-semibold">
              {architecture.name}
            </h2>

            <p>
              {architecture.description}
            </p>
          </div>
        </Link>
      ))}
    </div>
  );
}