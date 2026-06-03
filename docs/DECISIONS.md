docker run --name system_design_db \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=system_design_playground \
  -p 5432:5432 \
  -d postgres


alembic init alembic
alembic revision --autogenerate -m "create_architectures_table"
alembic upgrade head

{
  "id": "4b91ff72-1578-4eb7-a9e9-619e6b74d4d3",
  "name": "URL Shortener retry",
  "description": "System design practice",
  "created_at": "2026-06-03T15:18:54.662000Z",
  "updated_at": "2026-06-03T15:18:54.662000Z"
}