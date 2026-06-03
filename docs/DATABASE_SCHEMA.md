### PostgreSQL Database
#####  Tables
    * architectures
        - id UUID
        - name varchar
        - description TEXT
        - created_at
        - updated_At
    * components
        - id UUID
        - architecture_id
        - component_type varchar
        - config JSONB
    * connections
        - id UUID
        - source_component_id UUID
        - target_component_id UUID
    *requirements
        - id UUID
        - architecture_id UUID
        - users BIGINT
        - dau BIGINT
        - peak_rps INT
        - availabilty Float