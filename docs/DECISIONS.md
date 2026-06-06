docker run --name system_design_db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=system_design_playground \
  -p 5432:5432 \
  -d postgres

uvicorn app.main:app --reload

alembic init alembic
alembic revision --autogenerate -m "create_architectures_table"
alembic upgrade head

[
  {
    "id": "5cdeda40-01ee-4dfc-82be-a3c246d816a4",
    "name": "URL Shortener retry",
    "description": "System design practice",
    "created_at": "2026-06-04T10:59:20.325250Z",
    "updated_at": "2026-06-04T10:59:20.325250Z"
  },
  {
    "id": "47a371a6-3c41-4eb7-ae40-e97723f19c77",
    "name": "URL Shortener",
    "description": "System design practice",
    "created_at": "2026-06-04T10:59:10.941684Z",
    "updated_at": "2026-06-04T10:59:10.941684Z"
  }
]


{
  "architecture": {
    "id": "123",
    "name": "URL Shortener",
    "description": "TinyURL clone"
  },

  "components": [
    {
      "id": "1",
      "name": "Load Balancer",
      "component_type": "load_balancer"
    },
    {
      "id": "2",
      "name": "API Service",
      "component_type": "api_service"
    }
  ],

  "connections": [
    {
      "id": "10",
      "source_component_id": "1",
      "target_component_id": "2"
    }
  ]
}