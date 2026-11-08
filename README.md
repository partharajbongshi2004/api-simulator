
API Simulator

A lightweight, configurable API simulator designed to mock endpoints, simulate network latency, and test edge-case responses without touching production or external services. Perfect for local frontend development, CI/CD testing, and staging integration.

🚀 Key Features

• Dynamic Mocking: Define routes, status codes, and JSON payloads via simple configuration files.
• Latency Simulation: Simulate realistic API lags (e.g., 500ms delay, fluctuating network) to test UI loading states.
• Chaos Engineering: Randomly inject 5xx server errors, rate limiting (429), or drop connections entirely.
• State Maintenance: Keep ephemeral local states across sequential requests (e.g., POSTing an entity makes it available in the subsequent GET request).
• OpenAPI Support: Automatically bootstrap simulated endpoints from an existing Swagger or OpenAPI specification document.

🛠️ Tech Stack & Dependencies

• Core: Node.js (Express / TypeScript)
• Data Immutability: Immer
• Documentation Parsing: OpenAPI-Backend

🗂️ Getting Started


Prerequisites
python 3.x
Streamlit
• Node.js (version 18.0 or higher)
• npm or yarn

Installation
pip install Streamlit
Streamlit run main.py
