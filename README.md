# Prompt Generator CLI

A lightweight, extensible CLI tool that helps users generate high-quality, structured English prompts for Large Language Models (LLMs) such as ChatGPT, Gemini, Grok, Claude, etc.

The tool dynamically loads prompt categories and their questions from YAML configuration files, making it flexible and easy to extend with new themes without changing the code.

## Installation

1. Ensure you have Python 3.8 or higher installed.

2. That's it! No dependencies required. The script uses only Python's standard library.

3. (Optional) Install pyperclip for clipboard functionality:
```bash
pip install pyperclip
```

## Usage

Run the CLI tool:
```bash
python prompt_generator_cli.py
```

The tool will:
1. Display a numbered list of available categories
2. Allow you to select a category (or exit)
3. Ask you questions sequentially for the selected category
4. Generate an English prompt incorporating your answers
5. Optionally copy the prompt to your clipboard
6. Allow you to generate another prompt or exit

### Example Session

```
$ python prompt_generator_cli.py

Welcome to Prompt Generator CLI (Student Edition)!

Available categories:
1. Hrana i menza
2. Izlazak i društveni život
3. Putovanje na faks i kući
4. Ušteda novca kao student
5. Život na fakultetu
0. Exit

Select a category (number): 1

--- Hrana i menza ---

1. Koristiš li studentsku menzu ili X-icu?
   Napiši "da/redovito", "povremeno" ili "ne".
   > povremeno

2. Koliko približno trošiš mjesečno na hranu?
   Ukupno – menza, samoposluge, dostava, restorani.
   > 150 eura

...

Here is your generated prompt:

"""
You are a friendly, practical student advisor...
"""

Prompt copied to clipboard!

Generate another prompt? (y/n): n
Goodbye!
```

## Configuration

Categories and questions are defined in `config/categories/student-life-hr.yaml`. The YAML file follows this structure:

```yaml
categories:
  - name: Category Name
    questions:
      - question: Question text shown to user
        instruction: Helper text shown below the question
      - question: Another question
        instruction: Another helper instruction
```

## Features

- **Dynamic Configuration**: Categories and questions are loaded from YAML files
- **Interactive Workflow**: Simple menu-driven interface
- **Abort Support**: Type "abort" or press Enter with empty input to return to the main menu
- **Clipboard Integration**: Automatically copies generated prompts to clipboard (if pyperclip is installed)
- **Plain Text Output**: No colors or visual enhancements - simple, clean interface

## Adding New Categories

To add new categories or questions:

1. Edit `config/categories/student-life-hr.yaml`
2. Add new category entries following the existing structure
3. Categories are automatically sorted alphabetically in the menu
4. No code changes required

## Requirements

- Python 3.8+ (standard library only)
- pyperclip (optional, for clipboard functionality)

## License

This project is provided as-is for educational and personal use.

