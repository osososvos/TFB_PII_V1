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

< Project's name > uses the following technologies and tools:

- [Python](https://www.python.org/): ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- [SQLite](https://sqlite.org/): ![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
- ...


## Contributing

Las contribuciones son bienvenidas. Para cambios importantes, por favor abra un issue primero para discutir lo que le gustaría cambiar.

## Contributors

Here's the list of people who have contributed to < project's name >:

- John Doe – [@JohnDoeTwitter](https://twitter.com/< username >) – john@example.com
- Jane Doe – [@JaneDoeTwitter](https://twitter.com/< username >) – jane@example.com

The Anonimizer development team really appreciates and thanks the time and effort that all these fellows have put into the project's growth and improvement.

## Author

< AGR > – [@AuthorTwitter](https://twitter.com/< username >) – author@example.com

## Change log
- 0.1
    - Hecho: Falla con muchas entidades
           El modelo es ENG SM y falla con muchas PERSON in Catalan.
           Usado CAt y peor
           --Para testear otros modelos: python -m spacy download en_core_web_md y pip uninstall en-core-web-md
                   Los salva en:.venv\Lib\site-packages\en_core_web_sm---
       S: Cambiar a modelo eng_core_MD

     HECHO:Remplaza con nombre de entidad en vez de "REDACTED"
     Hecho: No detecta Fechas. 
        S: Agregado DATE y TIME as LABEL.
     Hecho: Mejorado Regex passports.Mas flexible   Hecho: Falla con nombres con acento cerrado como "Mercè ".
                S: Usar lib Unicode para normalizar y eliminar acentos
     Falla al tagear 4 digits numbers in to CARDINAL category. Possibly because is like a yer?
       S: Regex con alphan patterns preceded by keywords
- 0.0.2
    - Polish the user interface
- 0.0.1
    - First working version
- ...

## Known Issues

- Currently, all information is condensed onto one page.
- The font size is not respected.
- Failures when processing documents with many entities.
- The SpaCy `en_core_web_sm` model fails with many `PERSON` entities in Catalan.

### Alternative Solution

To test other models, you can download the SpaCy `en_core_web_md` model:
```sh
python -m spacy download en_core_web_md
```


## License

< project's name > is distributed under the < license > license. See [`LICENSE`](LICENSE.md) for more details.