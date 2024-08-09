# Anonimyzer.  Universidad Carlemnay. TFB 

![coverage](https://img.shields.io/badge/coverage-80%25-yellowgreen)
![version](https://img.shields.io/badge/version-0.2-yellow)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

This application allows you to load Word documents (.docx) and remove personal identifiable information (PII) using natural language processing (NLP) with SpaCy and custom regular expressions. The graphical user interface (GUI) is built with Tkinter.


<img alt="Example Image" src="images/Anonimyzer 0.1.png"/>

**Table of Contents**

- [Installation](#installation)
- [Execution / Usage](#execution--usage)
- [Technologies](#technologies)
- [Features](#features)
- [Contributing](#contributing)
- [Contributors](#contributors)
- [Author](#author)
- [Change log](#change-log)
- [License](#license)


## Features

- Load Word documents.
- Identify PII using named entity recognition (NER) with SpaCy and custom regular expressions.
- Redact PII in the documents.
- Save redacted documents.


## Requirements

- Python 3.x
- The following Python libraries:
  - `python-docx`
  - `spacy`
  - `tkinter`
  - `re`

## Installation

1. Clone the repository or download the source code.
2. Create a virtual environment (optional but recommended):
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```
3. Install the dependencies:
    ```sh
    pip install python-docx spacy
    ```
4. Download the SpaCy model:
    ```sh
    python -m spacy download en_core_web_sm
    ```

## Execution / Usage

1. Run the main script:
    ```sh
    python main.py
    ```
2. In the GUI, select a .docx file using the "Buscar" button.
3. Click the "Anonimizar" button to process the file and save the redacted document.


## Technologies

Anonimyzer uses the following technologies and tools:

- [Python](https://www.python.org/): ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- ...


## Contributing

Las contribuciones son bienvenidas. Para cambios importantes, por favor abra un issue primero para discutir lo que le gustaría cambiar.

The Anonimizer development team really appreciates and thanks the time and effort that all these fellows have put into the project's growth and improvement.

## Author

< AGR > – [@AuthorTwitter](https://twitter.com/< username >) – author@example.com

## Change log
- 0.2.1
   - Fixed:
     - Handle File in Use
     - Handle Page Breaks
- 0.2
   - Fixed:
     - Falla con muchas entidades. Usado CAT y peor
           --Para testear otros modelos: python -m spacy download en_core_web_md y pip uninstall en-core-web-md
                   Los salva en:.venv\Lib\site-packages\en_core_web_sm---
     - Cambiar a modelo eng_core_MD
     - Remplaza con nombre de entidad en vez de "REDACTED"
     - No detecta Fechas. S: Agregado DATE y TIME as LABEL.
     - Mejorado Regex Passports.Mas flexible, pero luego se solapa con el regex de "number:" por ello, lo anulo.
     - Falla con nombres con acento cerrado como "Mercè ". S: Usar lib Unicode para normalizar y eliminar acentos
     - Fails to label 4 digits numbers in to CARDINAL category. Possibly because is like a year?S: Specific REGEX
    

- 0.0.2
    - Polish the user interface
- 0.0.1
    - First working version
- ...

### Known Issues

- PII in tables or cells not REDACTED


### Working on...
- GUI inclusiva(ampliar Font size or implement High Contrast 
- Be able to deal with texts embbebed in cells.

### License

Anonimyzer is distributed under the < license > license. See [`LICENSE`](LICENSE.md) for more details.