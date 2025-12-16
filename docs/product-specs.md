Product Specification: Prompt Generator CLI
===========================================

1\. Overview
------------

**Product Name:** Prompt Generator CLI

**Type:** Command-line interface (CLI) tool written in Python.

**Purpose:** A lightweight, standalone tool that helps software developers generate high-quality, structured prompts for Large Language Models (LLMs) such as ChatGPT, Gemini, Grok, Claude, etc. The tool guides the user through a series of simple questions specific to a chosen development phase, collects the answers, and assembles a well-crafted English prompt ready to copy-paste into any LLM chat interface.

The initial version is intentionally simple and hard-coded -- no external configuration files, no database, no web framework. All prompt templates and questions are defined directly in the code.

2\. Target Users
----------------

-   Software developers, architects, product owners, and QA engineers working on software product development.
-   Anyone who wants to leverage LLMs more effectively during ideation, design, architecture, implementation, testing, or deployment phases.

3\. Key Features (MVP)
----------------------

1.  **Interactive Category Selection** The tool presents a list of predefined development phases/categories.
2.  **Guided Question Flow per Category** For the selected category, the tool asks 4--8 simple, targeted questions (via input()). Questions are hard-coded and designed to gather the most relevant context.
3.  **Prompt Assembly** Using the user's answers, the tool fills a hard-coded prompt template (in English) that follows LLM best practices:
    -   Clear role assignment
    -   Detailed context
    -   Specific instructions
    -   Desired output format
    -   Chain-of-thought encouragement where appropriate
4.  **Output**
    -   Displays the final generated prompt in a clearly marked block.
    -   Offers to copy it to the clipboard (using pyperclip if available, with graceful fallback).
    -   Asks if the user wants to generate another prompt or exit.

4\. Supported Categories (Initial Set)
--------------------------------------

The MVP must include at least the following categories with corresponding hard-coded question flows and templates:

1.  **Ideation & Product Discovery** Focus: brainstorming features, user needs, problem validation.
2.  **Product Specifications** Focus: writing user stories, functional/non-functional requirements, acceptance criteria.
3.  **Solution Architecture** Focus: high-level design, tech stack choices, component diagram suggestions.
4.  **Detailed Implementation** Focus: code structure, algorithms, specific module implementation.
5.  **Testing** Focus: unit/integration/e2e test cases, edge cases, test data generation.
6.  **CI/CD & Deployment** Focus: pipeline scripts, Dockerfiles, cloud deployment configurations.

(Developer may add 1--2 additional categories if time permits, but the above six are required.)

5\. Technical Requirements
--------------------------

-   **Language:** Python 3.8+
-   **Dependencies:**
    -   Standard library only for core functionality.
    -   Optional: pyperclip for clipboard support (detect and use if installed; otherwise inform user to copy manually).
-   **Entry Point:** Script should be executable via python prompt_generator_cli.py or installed as a console script if packaged.
-   **No external APIs or internet access required** -- fully offline.
-   **Code Structure Suggestions (recommended, not mandatory):**
    -   Main script file (prompt_generator_cli.py or main.py)
    -   Separate module/file for prompt templates and question definitions (e.g., templates.py)
    -   Clear functions for each category to keep main() readable.

6\. User Experience Flow (Example)
----------------------------------

```text$ python prompt_generator_cli.py

Welcome to Prompt Generator CLI!

Select a category:
1. Ideation & Product Discovery
2. Product Specifications
3. Solution Architecture
4. Detailed Implementation
5. Testing
6. CI/CD & Deployment

Enter number: 3

--- Solution Architecture ---

1/6: What is the main purpose of the application? 
> A fintech platform for salary advances

2/6: What are the key non-functional requirements (e.g., scalability, security, performance)?
> High security (GDPR, PCI-DSS), handle 100k+ users, low latency

... (remaining questions) ...

Here is your generated prompt:

"""[Well-structured English prompt appears here]"""

Prompt copied to clipboard! (or "Please copy the prompt above manually.")
Generate another prompt? (y/n):```

7\. Prompt Quality Guidelines
-----------------------------

All generated prompts must:

-   Be entirely in **English**.
-   Assign a clear role to the LLM (e.g., "You are an expert software architect...").
-   Provide sufficient context from user answers.
-   Specify the desired output format (e.g., Markdown sections, Mermaid diagrams, JSON).
-   Encourage step-by-step reasoning where appropriate.
-   Be optimized for the selected development phase.

8\. Deliverables
----------------

-   Fully functional Python CLI tool meeting the requirements above.
-   README.md with:
    -   Short description
    -   Installation/usage instructions
    -   Example session
    -   How to extend with new categories (for future maintenance)

9\. Non-Goals (for MVP)
-----------------------

-   Dynamic template loading from files/YAML/JSON
-   GUI or web interface
-   Integration with specific LLMs
-   Persistent history
-   Advanced validation or error correction

This specification is intentionally high-level to allow developer judgment while ensuring the core value -- fast, high-quality prompt generation -- is delivered.
