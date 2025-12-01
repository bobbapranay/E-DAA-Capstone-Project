# requirements.txt - Detailed Explanation

This file lists all Python dependencies required to run the Enterprise Data Analyst Agent project reliably and reproducibly, ensuring consistent environments for Kaggle judging and deployment.

## Core AI and Data Libraries
- `google-generativeai==0.8.3`: Provides access to Gemini 1.5 Pro large language model for producing business insights.
- `pandas==2.2.2` and `numpy==1.26.4`: Essential for efficient data manipulation and numerical computations in exploratory data analysis.
- `scikit-learn==1.5.1`: Used for machine learning model recommendations and evaluations.

## Visualization
- `matplotlib==3.9.2` and `seaborn==0.13.2`: Generate informative static visualizations such as histograms and boxplots.
- `plotly==5.22.0`: Enables interactive charts for enhanced data exploration.

## Agent Framework and Querying
- `adk-python==0.1.0`: Google’s Agent Development Kit enabling multi-agent orchestration and tool integration.
- `duckdb==1.1.0`: Fast analytics querying engine to handle large enterprise datasets efficiently.

## Web API and Deployment
- `fastapi==0.115.0` and `uvicorn[standard]==0.30.6`: For serving the agent API with asynchronous, lightweight server support.
- `python-multipart==0.0.9`: Handles multipart HTTP requests, including file uploads.

## Configuration, Validation & Logging
- `pyyaml==6.0.2` and `pydantic==2.8.2`: Manage environment and session configurations with validation.
- `loguru==0.7.2`: Provides structured, easy-to-read logging for observability.
- `python-dotenv==1.0.1`: Loads environment variables from `.env` files safely.

## Utilities
- `requests==2.31.0`: HTTP library for calling external APIs and web services.
- `jinja2==3.1.4`: Template engine for generating report markdown or HTML dynamically.

---


