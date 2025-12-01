# Deployment Guide

## Local Development (2 minutes)

```

git clone https://github.com/YOUR_USERNAME/enterprise-data-analyst-agent.git
cd enterprise-data-analyst-agent
python3 -m venv venv \&\& source venv/bin/activate
pip install -r requirements.txt
export GEMINI_API_KEY="your_key"
python main.py --dataset data/titanic.csv --query "survival analysis"

```

## Production Deployment (Google Cloud Run - Bonus Points)

```

gcloud run deploy data-analyst-agent \
--source . --region us-central1 --allow-unauthenticated \
--set-env-vars GEMINI_API_KEY=\$GEMINI_API_KEY

```

## API Endpoints

```

POST /analyze       \# Provide dataset URL and analysis query, receive report ID
GET /report/{id}/download   \# Download final report and charts by report ID

```

## Environment Variables

- `GEMINI_API_KEY`: Your Gemini API key (required).
- `MAX_FILE_SIZE_MB`: Max dataset size in MB (default 1024).
- `LOG_LEVEL`: Log verbosity (default INFO).

## Health Check

```

GET /health   \# Returns status of agents and uptime

```

---

**No API keys included in code.**

**Docker-ready and scalable cloud deployment.**

**Commit with:**

```

git add deployment_guide.md
git commit -m "Add deployment guide"
git push origin main

```
```

<span style="display:none">[^1][^10][^2][^3][^4][^5][^6][^7][^8][^9]</span>

<div align="center">⁂</div>

[^1]: https://handbook.gitlab.com/docs/markdown-guide/

[^2]: https://about.samarth.ac.in/docs/guides/markdown-syntax-guide

[^3]: https://www.reddit.com/r/devops/comments/12epvyc/using_documentation_as_code_for_a_deployment_guide/

[^4]: https://docs.polypheny.com/en/latest/user_interfaces/notebooks/cells/markdown-cells

[^5]: https://grafana.com/docs/writers-toolkit/write/markdown-guide/

[^6]: https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Working With Markdown Cells.html

[^7]: https://docs.gruntwork.io/guides/style/markdown-style-guide/

[^8]: https://www.markdownguide.org/basic-syntax/

[^9]: https://www.markdownguide.org/extended-syntax/

[^10]: https://www.ibm.com/docs/en/planning-analytics/3.1.0?topic=313-format-text-markdown-in-single-cell-visualizations

