# Ziri: Voice-Activated Assistant

Ziri is a Python-based voice-activated assistant that listens to voice commands, recognizes them using Google's speech recognition, and performs various tasks such as opening websites or telling the time. This project utilizes libraries like `pyttsx3` for text-to-speech conversion and `speech_recognition` for voice recognition.

## Features

- **Voice Interaction**: Ziri can greet the user based on the time of day and ask how it can assist.
- **Voice Command Recognition**: Ziri listens to the user's command and interprets it using Google's speech recognition API.
- **Perform Actions**:
  - Opens websites such as YouTube when commanded.
  - More features like retrieving information from Wikipedia and telling the current time are present but currently commented out for future use.
  
## Prerequisites

To run this project, you need to install the following Python libraries:

- **pyttsx3**: For text-to-speech functionality.
  ```bash
  pip install pyttsx3
  ```
- **speech_recognition**: For recognizing voice input.
  ```bash
  pip install SpeechRecognition
  ```
- **pyaudio**: Needed for speech recognition to access the microphone.
  ```bash
  pip install pyaudio
  ```
- **wikipedia-api**: For fetching summaries from Wikipedia (optional feature).
  ```bash
  pip install wikipedia-api
  ```
- **win32com**: For interacting with Windows components (automatically included in `pywin32`).
  ```bash
  pip install pywin32
  ```

## Usage

1. Clone the repository or copy the provided code into a Python file, for example, `ziri.py`.
2. Install the necessary dependencies mentioned above.
3. Run the program.
   ```bash
   python ziri.py
   ```
4. Upon starting, Ziri will greet you based on the current time and wait for your voice command.
5. You can say, "Open YouTube," and Ziri will open YouTube in your default browser.

## Future Enhancements

- **Wikipedia Integration**: Uncomment and further refine the `wikipedia` code section to allow Ziri to fetch summaries for various topics.
- **Time Feature**: Ziri can tell the current time if you ask, by uncommenting the time feature.
- **More Website Commands**: Add more websites in the `sites` list for Ziri to recognize and open.

## Known Issues

- Ensure your microphone is working properly for the voice recognition to function smoothly.
- There may be a slight delay in response depending on network latency when using Google's speech recognition API.
- If voice recognition fails, the assistant will prompt, "Say that again, please," and retry.

## Contribution

Feel free to fork the project, add features, or submit bugs via pull requests!
