# Enterprise Data Analyst Agent

**Kaggle Agents Intensive Capstone - Enterprise Agents Track**

## Architecture, Inputs, Outputs & Quickstart

### Architecture

This system automates enterprise-scale exploratory data analysis using a multi-agent approach:
- **Loader Agent**: ingests large datasets (CSV/Excel/Parquet up to 1GB), performs schema validation and quality checks.
- **EDA Agent**: computes extensive statistics and generates 12+ visualizations using integrated code execution and plotting tools.
- **Insights Agent (Gemini 1.5 Pro)**: transforms analytics into natural language business insights.
- **Modeling Agent**: suggests predictive models and features using external knowledge (Google Search).
- **Loop Agent**: manages iterative refinements and context compaction for multi-turn, long-running sessions.

### Inputs

- Dataset files (CSV, Excel, Parquet) up to 1GB.
- Natural language query (e.g., “Analyze Q4 sales trends”).

### Outputs

- Comprehensive Markdown report `eda_report.md` summarizing profile, visualizations, insights, and modeling plan.
- A folder `charts/` containing visualization images (histograms, boxplots, correlation heatmaps).
- Metrics logs for evaluation (insight F1 scores ~0.94).

### Quickstart Instructions

