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

1. **Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/enterprise-data-analyst-agent.git
cd enterprise-data-analyst-agent
```

2. **Setup Virtual Environment**

Create and activate a Python virtual environment to isolate dependencies:

```bash
python3 -m venv venv
source venv/bin/activate       # Linux/Mac
# For Windows Powershell: .\venv\Scripts\Activate.ps1
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure Gemini API Key**

Export your Gemini API key as an environment variable (do NOT hardcode keys):

```bash
export GEMINI_API_KEY="your_actual_gemini_api_key"
```

5. **Run The Analysis**

Run the main script with a sample dataset and query:

```bash
python main.py --dataset data/titanic.csv --query "Analyze survival patterns"
```

6. **Output**

- Generates markdown report: `eda_report.md`
- Outputs charts in folder: `charts/` (e.g., histograms, correlation heatmaps)
- Saves execution logs in `logs/` folder for observability

7. **Modify Inputs**

You can easily swap in your own datasets (up to 1GB) and queries for custom analysis without changing code.

8. **Run Jupyter Notebook Demo**

For an interactive example, run the Kaggle-compatible notebook:

```bash
jupyter notebook AutoAnalystSuite.ipynb
```

9. **Deployment**

Instructions for local testing can be extended to cloud deployment (Google Cloud Run) for API serving.

***


