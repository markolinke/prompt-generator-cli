# Product Specification: Prompt Generator CLI (Student Edition)

## 1. Overview

**Product Name:** Prompt Generator CLI  

**Type:** Command-line interface (CLI) tool written in Python.  

**Purpose:**  
A lightweight, extensible CLI tool that helps users (primarily students) generate high-quality, structured English prompts for Large Language Models (LLMs) such as ChatGPT, Gemini, Grok, Claude, etc.  

The tool dynamically loads prompt categories and their questions from YAML configuration files, making it flexible and easy to extend with new themes without changing the code.

The initial focus is on **student life topics** (university routines, social life, food, commuting, budgeting), but the architecture supports any domain by simply adding new YAML files.

## 2. Target Users

- University students in Croatia (or similar contexts) seeking practical AI-generated advice on daily student challenges.
- Anyone who wants a reusable, configurable prompt generator for themed conversational guidance.

## 3. Key Features (Version 2 – Config-Driven)

1. **Dynamic Configuration Loading**  
   - Categories and questions are loaded from YAML files located in the `./config/categories/` folder.  
   - By default, only files in `./config/categories/student/` are loaded (student mode).  
   - Other subfolders/modes are ignored unless selected.

2. **Mode Selection**  
   - Default mode: `student` – automatically loads all YAML files from `./config/categories/student/`.  
   - Mode can be overridden via command-line argument (e.g., `--mode student`).  
   - Future extensions may add other modes by creating new subfolders.

3. **Interactive Workflow**  
   - Main menu: Display a numbered list of all loaded categories (merged from all YAML files in the active mode, sorted alphabetically).  
   - Include an option to exit (e.g., 0).  
   - After selecting a category:  
     - Sequentially ask each question defined in the YAML (show `question` and then `instruction` as helper text).  
     - Allow aborting at any question (e.g., empty input or typing "abort" → return to main menu).  
   - After completing all questions (or abort): proceed to prompt generation only if all answers collected.

4. **Prompt Generation**  
   - Use a **hard-coded prompt template engine** that combines:  
     - A fixed system role and instructions.  
     - The selected category name.  
     - All user answers clearly labeled.  
   - Generated prompt is always in **English** and follows LLM best practices (role-playing, context, step-by-step reasoning, formatted output request).  
   - Display the final prompt in a clearly marked multi-line block.  
   - Optional: copy to clipboard using `pyperclip` (with fallback message if not installed).

5. **Main Loop**  
   - After displaying a generated prompt, ask if the user wants to generate another one (y/n).  
   - If yes → return to category selection.  
   - If no → exit gracefully.

## 4. Configuration Structure

YAML files are placed in `./config/categories/student/` (default mode).

Each YAML file follows this exact structure and may contain one or more categories:

```yaml
categories:
  - name: Category Name In Croatian
    questions:
      - question: Question text shown to user
        instruction: Helper text shown below the question
      - question: Another question
        instruction: Another helper instruction
  # Multiple categories allowed per file
````

All YAML files in the active mode folder are loaded and merged.

5\. Technical Requirements
--------------------------

-   **Language:** Python 3.8+
-   **Dependencies:**
    -   pyyaml -- required for loading configuration files.
    -   Optional: pyperclip -- for clipboard functionality (detect if installed).
- Recommended Project Structure:

```text
prompt_generator_cli/
├── prompt_generator_cli.py     # Main executable script
├── config/
│   └── categories/
│       └── student/
│           ├── faculty_life.yaml
│           ├── social_life.yaml
│           └── ...                 # Additional YAML files
└── README.md
```

- Execution:

```text
python prompt_generator_cli.py          # Default student mode
python prompt_generator_cli.py --mode student
```

6\. User Experience Example

```text
$ python prompt_generator_cli.py

Welcome to Prompt Generator CLI (Student Edition)!

Available categories:
1. Život na fakultetu
2. Izlazak i društveni život
3. Hrana i menza
4. Putovanje na faks i kući
5. Ušteda novca kao student
0. Exit

Select a category (number): 1

--- Život na fakultetu ---

1. Koji fakultet pohađaš i koju godinu studija?
   Npr. "FER, 3. godina preddiplomskog" ili ...
   > FER, 3. godina

2. Koje su ti najveće poteškoće...
   > održavanje koncentracije

... (all questions)

Here is your generated prompt:

"""
You are an experienced academic coach specialized in helping university students...
[Full English prompt incorporating all answers]
"""

Prompt copied to clipboard! (or "Please copy manually")

Generate another prompt? (y/n):
```

7\. Prompt Template Guidelines (Hard-coded)
-------------------------------------------

The hard-coded prompt builder must:

-   Begin with a strong system role (e.g., "You are a friendly, practical student advisor...").
-   Include the category name for context.
-   List each answer with a clear label (e.g., "Faculty and year: FER, 3rd year undergraduate").
-   End with instructions for the LLM to respond in Croatian, using structured format (headings, bullet points, actionable steps).

The template is generic enough to work with any category/question set loaded from config.

8\. Deliverables
----------------

-   Fully functional, configuration-driven CLI tool.
-   Pre-populated ./config/categories/student/ folder with student-themed YAML files (as previously defined).
-   README.md containing:
    -   Description
    -   Installation steps (pip install pyyaml)
    -   Usage instructions and examples
    -   Guide for adding new categories or modes

9\. Non-Goals (Current Version)
-------------------------------

-   Simultaneous multi-mode support
-   In-app config editing
-   GUI or web version
-   Session history persistence
-   Per-category custom prompt templates

This design ensures the tool is **dynamically flexible** --- category listing and question flow depend entirely on the YAML files in the active mode folder, while core application logic remains simple and maintainable.