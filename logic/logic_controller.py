from ai.ai_client import generate_response


def build_system_prompt(mode):
    prompts = {
        "Explain": "Explain the text clearly, step-by-step, using simple language.",
        "Summarize": "Summarize the text clearly and briefly.",
        "Keywords": "Extract key concepts and explain them shortly.",
        "Quiz": "Generate 5 study questions with answers."
    }
    return prompts.get(mode, prompts["Explain"])


def process_text(mode, user_text, file_name=None):
    if not user_text.strip():
        return "Please enter some text first."

    system_prompt = build_system_prompt(mode)

    if file_name:
        user_message = f"File: {file_name}\n\nText:\n{user_text}"
    else:
        user_message = user_text

    return generate_response(system_prompt, user_message)