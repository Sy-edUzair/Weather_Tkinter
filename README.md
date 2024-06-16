# MeganMorse

#### Video Demo:  <URL HERE>

#### Description:

MeganMorse is a Morse code translator that encodes and decodes Morse code by loading a dictionary through a CSV file where all characters and corresponding codes are saved. The project's name is inspired by the DC character Miss Martian, whose adopted last name is "Morse." The program functions as if she performs the encoding and decoding telepathically. 

## Features

- **Encode Text to Morse Code**: Convert any alphanumeric text into Morse code.
- **Decode Morse Code to Text**: Translate Morse code back into readable text.
- **Play Morse Code Sound**: Listen to the Morse code through sound playback.
- **Text-to-Speech**: Use Google Text-to-Speech to read out the decoded message.

## Libraries Used

- `csv`: For manipulating the CSV file containing the Morse code dictionary.
- `os`: For interacting with the operating system, such as file handling.
- `playsound`: To play sound files representing Morse code.
- `time`: For managing delays and timing in sound playback.
- `sys`: For system-specific parameters and functions.
- `gtts`: Google Text-to-Speech library for converting text to speech.

## How to Use

1. **CSV File Structure**: Ensure your CSV file is structured with characters and their corresponding Morse codes. Example:
    ```
    character,code
    A,.- 
    B,-...
    C,-.-.
    ```
   
2. **Loading the Dictionary**: The program reads the CSV file to load the Morse code dictionary.

3. **Encoding**: Input your text, and the program will convert it to Morse code.

4. **Decoding**: Input your Morse code, and the program will translate it to text.

5. **Play Sound**: The program can play the Morse code as sound.

6. **Text-to-Speech**: The decoded text can be read aloud using the Google Text-to-Speech library.

## Installation

1. Install the required libraries using pip:
    
    pip install playsound gtts
    
2. Download or clone the project repository.

3. Ensure you have the Morse code CSV file in the correct format.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

Inspired by Miss Martian from DC Comics. The name MeganMorse pays homage to her character.
