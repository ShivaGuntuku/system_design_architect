#### User Journey

* User Opens application -> Creates architecture based on requirement.
* e.g user -> load balance -> API Server -> Redis -> PostgresSQl
* provides requirement like below

    - User : 1M
    - Dailyt Active Users(DAU): 100 K
    - Peak RPS: 5K
    - Availability: 99.9%
* clicks for Analyze -> receives architecture score 7/10
* Provides the below info:
    
    - Bottlenecks: Single PostgreSQL Instance
    - Risk: No failover strategy
    - Improvements: Add read replicas
* Run Failure Scenarios

    - Traffic Spike: 5K RPS to 50K RPS
    - Database Failure
    - Cache Failure
    - Server Failure
    - DDoS Attack

#### Components Catalog
* Compute
    - Load Balancer
    - API Service
    - Worker
* Data
    - Redis
    - PostgreSQL
    - MongoDB
* Messaging
    - Kafka
    - Queue
* Edge
    - CDN
    - API Gateway


#### Design becomes JSON
    
    {
    "nodes": [
        {
        "id": "lb",
        "type": "load_balancer"
        },
        {
        "id": "api",
        "type": "api_service"
        },
        {
        "id": "redis",
        "type": "redis",
        "instances": 1
        }
    ],
    "edges": [
        {
        "source": "lb",
        "target": "api"
        },
        {
        "source": "api",
        "target": "redis"
        }
    ]
    }
    
    {
        "requirements": 
        {
            "users": 1000000,
            "dau": 100000,
            "peak_rps": 5000,
            "availability": 99.9
        }
    }

#### Milestone Plans
* Milestone 1: Canvas
    - Drag Nodes
    - Connect Nodes
    - Save Architecture
* Milestone 2: Graph Engine
    - Store nodes
    - Store edges
    - Validate graph
* Milestone 3: Rule Engine
    - Detect Bottlenecks
    - Detect SPOF
    - Detect Risks
* Milestone 4: Failure Simulator
    - Traffic spike
    - DB Failure
    - Cache Failure

* Milestone 5: AI Reviewer
    - Explain findings
    - Suggest improvements

* Milestone 6: Architecture Scoring
    - Scalability
    - Reliability
    - Availability
    - Securiy
    - Cost
    - Operational Complexity


    