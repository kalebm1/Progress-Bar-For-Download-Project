# Progress-Bar-For-Download-Project
Progress Bar For Download Project

## How to build .exe file
  1. Make the changes to the .py file and run the program to make sure that it runs correctly.
  2. Open file location in command prompt.
  3. Ensure you have Pyinstaller installed on your machine
  4. While in the file location, run the following command:
  ```
    pyinstaller --one-file --windowed --icon={enter icon name}.ico {filename}.py
  ```
  5. Once ran, the .exe will be in the new 'dist' folder and you can then run it.

## FAQs
  - Icons must be in .ico format, there are converters online you can use.
  - pyinstaller help: https://datatofish.com/executable-pyinstaller/
