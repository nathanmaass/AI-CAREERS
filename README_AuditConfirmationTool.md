# Audit Confirmation Drafting Assistant

This simple Python script helps you create a professional audit confirmation letter. It asks for a few details and then generates the text for you. You can save the result as a `.txt` or `.docx` file.

## Files

```
AI-CAREERS/
├── audit_confirmation_drafting_assistant.py  # main script
├── README_AuditConfirmationTool.md           # this guide
└── explorecareers-main/                      # existing project files
```

## Prerequisites

- **Python 3.8 or later** installed on your Windows machine. You can download it from [python.org](https://www.python.org/downloads/).
- **pip** (comes with recent Python versions) to install packages.
- [Optional] **Visual Studio Code** for editing and running the script.

## Setup Steps

1. **Open a Command Prompt in the project folder**
   - In File Explorer, navigate to the `AI-CAREERS` folder.
   - Click the address bar, type `cmd`, and press `Enter`. A Command Prompt should open at this location.

2. **(Optional) Install the docx package**
   - If you want to save drafts as `.docx`, run:
     ```
     pip install python-docx
     ```

3. **Run the script**
   - In the Command Prompt, execute:
     ```
     python audit_confirmation_drafting_assistant.py
     ```
   - Follow the on-screen prompts to enter the confirmation details.
   - After the draft appears, choose whether to save it as a text or Word document.

## Running in Visual Studio Code

1. Open Visual Studio Code and choose **File > Open Folder...**. Select the `AI-CAREERS` folder.
2. In the Explorer pane, open `audit_confirmation_drafting_assistant.py`.
3. Press `Ctrl+Shift+\`` to open a terminal inside VS Code.
4. From the terminal, you can run the same command:
   ```
   python audit_confirmation_drafting_assistant.py
   ```
5. The terminal will display the prompts and the generated letter. If you choose to save the file, it will appear in the same folder.

That's it! You can edit the script if you need to adjust the letter format or add more fields.
