# Study Companion (AI Desktop App)

A Python desktop application that helps users study more effectively by combining focus tools with AI-powered text explanation.

---

## Features

- Load `.txt` study materials
- Select specific parts of the text
- AI-powered actions:
  - Explain
  - Summarize
  - Extract Keywords
- Save assistant responses to file
- Guard against empty selection (prevents unnecessary API calls)
- Clean modular structure (UI / Logic / AI)

---

## How it works

1. Upload a `.txt` file or paste text manually  
2. Select a fragment of the text  
3. Click one of the actions (Explain / Summarize / Keywords)  
4. View the AI-generated response  
5. Optionally save the result  

---

## Tech Stack

- Python
- PySide6 (GUI)
- OpenAI API
- python-dotenv
