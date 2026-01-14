import re

def parse_yaml_simple(content):
    """Simple YAML parser for the specific structure used in this project.
    Only handles the categories structure with name and questions.
    """
    categories = []
    lines = content.split('\n')
    i = 0
    
    # Skip until we find "categories:"
    while i < len(lines) and not lines[i].strip().startswith('categories:'):
        i += 1
    
    if i >= len(lines):
        return []
    
    i += 1  # Skip "categories:"
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines
        if not line:
            i += 1
            continue
        
        # Check for new category (starts with "- name:")
        if line.startswith('- name:'):
            category = {'name': '', 'questions': []}
            # Extract name
            name_match = re.match(r'- name:\s*(.+)', line)
            if name_match:
                category['name'] = name_match.group(1).strip()
            
            i += 1
            
            # Look for questions section
            while i < len(lines):
                line = lines[i].strip()
                
                if not line:
                    i += 1
                    continue
                
                # If we hit a new category, break
                if line.startswith('- name:'):
                    break
                
                # Check for "questions:" line
                if line.startswith('questions:'):
                    i += 1
                    continue
                
                # Check for question entry (starts with "- question:")
                if line.startswith('- question:'):
                    question = {'question': '', 'instruction': ''}
                    # Extract question text
                    q_match = re.match(r'- question:\s*(.+)', line)
                    if q_match:
                        question['question'] = q_match.group(1).strip()
                    
                    i += 1
                    
                    # Look for instruction on next line
                    if i < len(lines):
                        inst_line = lines[i].strip()
                        if inst_line.startswith('instruction:'):
                            inst_match = re.match(r'instruction:\s*(.+)', inst_line)
                            if inst_match:
                                question['instruction'] = inst_match.group(1).strip()
                            i += 1
                    
                    category['questions'].append(question)
                else:
                    i += 1
            
            if category['name']:
                categories.append(category)
        else:
            i += 1
    
    return categories