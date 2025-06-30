import json
import os

PROMPT_FILE = "prompt_template.json"

def load_templates():
    if not os.path.exists(PROMPT_FILE):
        return {}
    try:
        with open(PROMPT_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("templates", {})
    except (json.JSONDecodeError, IOError):
        return {}

def save_templates(templates):
    with open(PROMPT_FILE, "w", encoding="utf-8") as f:
        json.dump({"templates": templates}, f, ensure_ascii=False, indent=2)

def set_template(name, content):
    templates = load_templates()
    templates[name] = content
    save_templates(templates)

def render_prompt(name, vars_dict):
    templates = load_templates()
    if name not in templates:
        return None, list(templates.keys())
    try:
        prompt = templates[name].format(**vars_dict)
        return prompt, None
    except KeyError as e:
        return f"Thiếu biến: {e}", None
