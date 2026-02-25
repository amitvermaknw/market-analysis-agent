#!/usr/bin/env python
from dotenv import load_dotenv
load_dotenv()

import os
import sys
import warnings
from datetime import datetime
import textwrap
from market_analysis_agent.utils.output_handler import save_output, print_posts
from market_analysis_agent.crew import MarketAnalysisAgent


warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    os.makedirs('output', exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = f'output/execution_log_{timestamp}.md'

    class Tee:
        def __init__(self, terminal, file):
            self.terminal = terminal
            self.file = file
        
        def write(self, message):
            self.terminal.write(message)
            self.file.write(message)
            self.file.flush()
        
        def flush(self):
            self.terminal.flush()
            self.file.flush()

    with open(log_file, 'w') as f:
        # Write header
        f.write(f"# Execution Log\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(f"**Topic:** Market analysis based on current trends in 2026\n\n")
        f.write(f"---\n\n")
        f.write(f"## Agent Execution Output\n\n")
        f.write(f"```\n")

        # Redirect stdout and stderr
        sys.stdout = Tee(sys.__stdout__, f)
        sys.stderr = Tee(sys.__stderr__, f)

        try:
            inputs = {
                'subject': 'Market analysis based on the current trandes in 2026',
                'current_year': str(datetime.now().year)
            }
            result = MarketAnalysisAgent().crew().kickoff(inputs=inputs)
            output, json_file, social_md_file = save_output(result)
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__

            f.write("```\n\n")
            f.write(f"## Summary\n\n")
            f.write(f"- JSON saved to: `{json_file}`\n")
            f.write(f"- Social media saved to: `{social_md_file}`\n")

            print_posts(output)
            print(f"\nExecution log saved to: {log_file}")

        except Exception as e:
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
            f.write("```\n\n")
            f.write(f"## Error\n\n")
            f.write(f"```\n{str(e)}\n```\n")
            raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        MarketAnalysisAgent().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MarketAnalysisAgent().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }

    try:
        MarketAnalysisAgent().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "topic": "",
        "current_year": ""
    }

    try:
        result = MarketAnalysisAgent().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")
