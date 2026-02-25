# Market Analysis Agent 🚀

A CrewAI-powered multi-agent system that analyzes financial markets, generates insights, and creates content including blog articles and social media posts.

## Sample Output

> **2026: A Promising Year for Growth and Innovation in Financial Markets**
>
> Global economy expected to grow by **2.8%**, with the US leading the way, driven by AI adoption, private credit expansion, and autonomous AI systems in banking.

---

## Features

- 📰 **Market News Monitoring** — Scrapes and monitors latest financial news
- 📊 **Data Analysis** — Analyzes market trends and generates insights
- ✍️ **Content Creation** — Generates blog articles and social media posts
- ✅ **Quality Assurance** — Reviews and validates all generated content
- 💾 **Structured Output** — Saves results as JSON and Markdown files

---

## Project Structure

```
market_analysis_agent/
├── src/
│   └── market_analysis_agent/
│       ├── config/
│       │   ├── agents.yaml          # Agent definitions
│       │   └── tasks.yaml           # Task definitions
│       ├── tools/                   # Custom tools
│       ├── utils/
│       │   └── output_handler.py    # Output saving utilities
│       ├── models.py                # Pydantic output models
│       ├── crew.py                  # Crew definition
│       └── main.py                  # Entry point
├── output/                          # Generated outputs (gitignored)
├── .env                             # API keys (gitignored)
├── .gitignore
└── pyproject.toml
```

---

## Agents

| Agent | Role | LLM | Tools |
|---|---|---|---|
| `market_news_monitor_agent` | Monitors financial news | Groq LLaMA 3.3 70B | SerperDev, ScrapeWebsite |
| `data_analyst_agent` | Analyzes market data | Groq LLaMA 3.3 70B | SerperDev, WebsiteSearch |
| `content_creator_agent` | Creates blog & social posts | OpenAI GPT-4o | SerperDev, WebsiteSearch |
| `quality_assurance_agent` | Reviews final content | OpenAI GPT-4o | — |

---

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager
- API keys for Groq, OpenAI, and Serper

---

## Installation

```bash
# Clone the repository
git clone https://github.com/your-username/market-analysis-agent.git
cd market_analysis_agent

# Install dependencies
crewai install
```

---

## Configuration

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key
```

### Getting API Keys

- **OpenAI** → [platform.openai.com](https://platform.openai.com)
- **Groq** (free tier available) → [console.groq.com](https://console.groq.com)
- **Serper** (2,500 free searches) → [serper.dev](https://serper.dev)

---

## Usage

```bash
# Run the crew
crewai run

# Train the crew
crewai train <n_iterations> <output_file>

# Replay from a specific task
crewai replay <task_id>

# Test the crew
crewai test <n_iterations> <model_name>
```

---

## Inputs

Modify the `inputs` dictionary in `main.py` to customize the analysis:

```python
inputs = {
    'subject': 'Market analysis based on the current trends in 2026',
    'current_year': '2026'
}
```

---

## Output

The crew generates structured output saved to the `output/` directory:

- `output/output_20260224_215547.json` — Full structured JSON output
- `output/social_media_posts.md` — Social media posts in Markdown
- `output/article_20260224_215547.md` — Blog article in Markdown

### Sample Social Media Output

**Twitter:**
> 🚀 2026 is looking bright for the financial market! A global growth of 2.8% is anticipated, with the US leading the way. Companies adopting AI will outperform. #FinancialTrends #AI

**LinkedIn:**
> Key Insights for 2026 Financial Markets: AI-driven companies are expected to lead growth. Private credit is on the rise as businesses seek flexible financing.

**Instagram:**
> 📊 The Future of Finance: 2026 — Projected global growth: 2.8% | Focus on AI-led growth and rising private credit.

---

## Key Market Trends Covered

- **AI-led Rally** — AI-driven companies outperforming traditional firms
- **Rise of Private Credit** — Alternative funding sources gaining traction
- **Autonomous AI in Banking** — Financial institutions integrating AI systems
- **Job Growth Expectations** — Stable unemployment with modest growth projected

---

## Dependencies

- [crewai](https://docs.crewai.com) — Multi-agent framework
- [crewai-tools](https://docs.crewai.com/concepts/tools) — Built-in tools
- [litellm](https://docs.litellm.ai) — LLM routing
- [pydantic](https://docs.pydantic.dev) — Structured output validation
- [python-dotenv](https://pypi.org/project/python-dotenv/) — Environment management
