import os
import argparse
import logging
from adk.agent import Agent
from adk.sessions import InMemorySessionService

# --- Import Agents (Placeholder imports for the files in the 'agents' directory) ---
# NOTE: These files (loader_agent.py, etc.) must be created as defined in the previous step.
from agents.loader_agent import LoaderAgent
from agents.eda_agent import EDAAgent
from agents.insights_agent import InsightsAgent
from agents.modeling_agent import ModelingAgent

# --- Configuration Keys for Session Memory (State Management) ---
# These keys are used to store and retrieve the shared data objects.
DATA_KEY = "dataframe_object"
REPORT_KEY = "eda_json_report"
INSIGHTS_KEY = "insights_narrative"
MODELING_KEY = "modeling_output"

# Set up basic logging for Observability (a course concept)
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def run_eda_pipeline(file_path: str) -> dict:
    """
    Orchestrates the sequential multi-agent pipeline for EDA.
    
    Args:
        file_path: The local path to the input data file (e.g., 'data/sample_data.csv').
        
    Returns:
        A dictionary containing the final aggregated analysis report.
    """
    logging.info(f"Pipeline Starting for: {file_path}")
    
    # 1. Initialize Session and Agents (Core ADK Setup)
    # The InMemorySessionService is our shared memory/state management system.
    session_service = InMemorySessionService()
    session = session_service.create_session(user_id="eda_user")
    session_id = session.session_id
    
    # Initialize agents with their roles and LLM models
    # We use gemini-2.5-pro for the Insights Agent (Bonus: Effective Use of Gemini)
    loader = LoaderAgent(session_service=session_service, llm_model="gemini-2.5-flash")
    eda = EDAAgent(session_service=session_service, llm_model="gemini-2.5-flash")
    insights = InsightsAgent(session_service=session_service, llm_model="gemini-2.5-pro") 
    modeling = ModelingAgent(session_service=session_service, llm_model="gemini-2.5-flash")

    # --- 2. Sequential Execution (A2A Protocol via Session/Memory) ---
    
    # Stage 1: Loader Agent
    initial_prompt = f"Load and validate the data from the file located at: {file_path}. Store the DataFrame using the key '{DATA_KEY}'."
    logging.info("--- Stage 1: Running Loader Agent (Data Ingestion) ---")
    loader.start(session_id, initial_prompt)
    
    # Quick check for failure before proceeding
    if session.get_data(DATA_KEY) is None:
        logging.error("Loader Agent failed: DataFrame not found in memory.")
        return {"error": "Pipeline failed at data loading stage."}

    # Stage 2: EDA Agent
    eda_prompt = f"Perform a comprehensive statistical and visual EDA on the data stored as '{DATA_KEY}'. Generate a detailed JSON report and store it as '{REPORT_KEY}'. Use the Code Execution tool for all calculations and plots."
    logging.info("--- Stage 2: Running EDA Agent (Analysis) ---")
    eda.start(session_id, eda_prompt)
    
    if session.get_data(REPORT_KEY) is None:
        logging.error("EDA Agent failed: Report not found in memory.")
        return {"error": "Pipeline failed at EDA stage."}

    # Stage 3: Insights Agent (Context Compaction & Gemini Pro Reasoning)
    insights_prompt = f"Analyze the EDA report stored as '{REPORT_KEY}'. Ignore raw statistics, and focus only on generating 5 high-level, business-actionable insights and a narrative summary. Store the final narrative as '{INSIGHTS_KEY}'."
    logging.info("--- Stage 3: Running Insights Agent (Business Narrative) ---")
    insights.start(session_id, insights_prompt)
    
    # Stage 4: Modeling Agent
    modeling_prompt = f"Based on all previous analysis, specifically the statistical data and insights, recommend the best Machine Learning task, the top 3 most predictive features, and the recommended algorithm. Store the output as '{MODELING_KEY}'."
    logging.info("--- Stage 4: Running Modeling Agent (Recommendation) ---")
    modeling.start(session_id, modeling_prompt)
    
    # 3. Final Output Compilation
    final_report = {
        "status": "Pipeline Succeeded",
        "file_analyzed": file_path,
        "insights_summary": session.get_data(INSIGHTS_KEY),
        "modeling_recommendation": session.get_data(MODELING_KEY)
    }

    logging.info("\n--- Pipeline Complete. Final Report: ---")
    # Pretty print the final output
    import json
    print(json.dumps(final_report, indent=4))
    return final_report

if __name__ == "__main__":
    # Ensure API Key is available before execution
    if not os.getenv("GEMINI_API_KEY"):
        logging.error("🚨 ERROR: GEMINI_API_KEY environment variable is not set. Please set it before running.")
    else:
        # Command Line Interface (CLI) setup for easy execution
        parser = argparse.ArgumentParser(description="Run the Enterprise Data Analyst Agent pipeline.")
        parser.add_argument("--file_path", required=True, help="Path to the input CSV/data file (e.g., data/sample_data.csv).")
        args = parser.parse_args()
        
        # Execute the main function
        run_eda_pipeline(args.file_path)