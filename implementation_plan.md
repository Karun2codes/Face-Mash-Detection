# Offline Local AI Assistant Implementation Plan

This document outlines the architecture, setup, and implementation steps for building a fully offline, locally running AI assistant using Python and Ollama.

## User Review Required

> [!IMPORTANT]
> Please review the proposed architecture and let me know if you approve.
> **Workspace Location:** Currently, the active workspace is `c:\Users\karun\Desktop\Face_Mask_Detection`. I will create the new project folder (`Offline_AI_Assistant`) inside this directory unless you would prefer me to initialize it elsewhere (e.g., `c:\Users\karun\Desktop\Offline_AI_Assistant`).

## Open Questions

> [!WARNING]
> 1. Which local LLM model do you prefer to start with using Ollama? (e.g., `llama3` 8B or `mistral`). `llama3` works great on 16GB RAM.
> 2. For the initial phase, is a CLI-based chat interface sufficient, or do you want the Tkinter/PyQt GUI implemented immediately?
> 3. Should the "Voice Support" (Speech-to-Text and Text-to-Speech) be added as functional code right now, or just stubbed out for Phase 2?

## Proposed Changes

We will create a modular Python application with the following structure. I will generate all the code for these modules:

### Project Initialization
#### [NEW] `requirements.txt`
To hold dependencies like `ollama` (for API), `pyttsx3` (for TTS), and `SpeechRecognition` (for STT).

### Core Modules

#### [NEW] `main.py`
The entry point of the application to initialize components and start the chat loop.

#### [NEW] `assistant.py`
The core logic handler that orchestrates user inputs, LLM interactions via Ollama, memory retrieval, and parses intents to trigger command execution.

#### [NEW] `commands.py`
Contains system-level commands tailored for Windows:
- Opening apps (e.g., Chrome, VS Code) using `os.startfile` or `subprocess`.
- System controls (shutdown/restart) using `os.system` with safety confirmations.

#### [NEW] `memory.py`
Manages conversation history. Will use a local JSON file (`chat_history.json`) to persist the context window for the LLM.

#### [NEW] `file_handler.py`
Handles reading text files, extracting content, and searching for files locally within specified directories to feed into the LLM for document Q&A and summarization.

#### [NEW] `ui.py`
The CLI interface loop to interact with the assistant. Can easily be swapped out with a GUI later.

#### [NEW] `README.md`
Will contain the step-by-step setup guide, architecture explanation, and performance improvement suggestions (Quantization, GPU offloading).

## Verification Plan

### Manual Verification
1. **Basic Chat:** Test basic chat capabilities to ensure offline inference works through the Ollama Python client.
2. **System Commands:** Ask the assistant to open an app (e.g., "Open Notepad") and verify the system action is executed.
3. **File Summarization:** Feed a sample text file path to the assistant and ask for a summary.
4. **Memory:** Verify memory persistence by restarting the app and asking about previous context.
