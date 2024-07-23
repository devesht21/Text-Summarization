
<p align="center">
    <h1 align="center">Text Summarization</h1>
</p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style=flat&logo=tqdm&logoColor=black" alt="tqdm">
	<img src="https://img.shields.io/badge/Jupyter-F37626.svg?style=flat&logo=Jupyter&logoColor=white" alt="Jupyter">
	<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=flat&logo=YAML&logoColor=white" alt="YAML">
	<img src="https://img.shields.io/badge/Jinja-B41717.svg?style=flat&logo=Jinja&logoColor=white" alt="Jinja">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white" alt="pandas">
	<img src="https://img.shields.io/badge/FastAPI-009688.svg?style=flat&logo=FastAPI&logoColor=white" alt="FastAPI">
</p>
<hr>

##  Quick Links

> - [ Overview](#-overview)
> - [ Repository Structure](#-repository-structure)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Training Model for Text Summarization](#-training-Model-for-Text-Summarization)
>   - [ Running Web App](#-running-Web-App)
> - [ Contributing](#-contributing)
> - [ License](#-license)

---

##  Overview

This Project is a Web Application that summarizes long text into a summary using a transformer model.  The main technologies used in this project are Python, Flask, transformers, and Fast API. The pipeline implemented is as follows:

Data Ingestion -> Data validation -> Data transformation -> Model training -> Model Evaluation -> Predictions -> API -> Web Application


---

##  Repository Structure

```sh
└── Text-Summarization/
    ├── LICENSE
    ├── README.md
    ├── app.py
    ├── config
    │   └── config.yaml
    ├── main.py
    ├── params.yaml
    ├── requirements.txt
    ├── research
    │   ├── data_ingestion.ipynb
    │   ├── data_transformation.ipynb
    │   ├── data_validation.ipynb
    │   ├── model_evalution.ipynb
    │   ├── model_trainer.ipynb
    │   └── trials.ipynb
    ├── setup.py
    ├── src
    │   └── textSummarizer
    │       ├── __init__.py
    │       ├── components
    │       │   ├── __init__.py
    │       │   ├── data_ingestion.py
    │       │   ├── data_transformation.py
    │       │   ├── data_validation.py
    │       │   ├── model_evalution.py
    │       │   └── model_trainer.py
    │       ├── config
    │       │   ├── __init__.py
    │       │   └── configuration.py
    │       ├── constants
    │       │   └── __init__.py
    │       ├── entity
    │       │   └── __init__.py
    │       ├── logging
    │       │   └── __init__.py
    │       ├── pipeline
    │       │   ├── __init__.py
    │       │   ├── prediction.py
    │       │   ├── stage_01_data_ingestion.py
    │       │   ├── stage_02_data_validation.py
    │       │   ├── stage_03_data_transformation.py
    │       │   ├── stage_04_model_trainer.py
    │       │   └── stage_05_model_evaluation.py
    │       └── utils
    │           ├── __init__.py
    │           └── common.py
    └── template.py
```


---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version 3.10.0`

###  Installation

1. Clone the Text-Summarization repository:

```sh
git clone https://github.com/devesht21/Text-Summarization
```

2. Change to the project directory:

```sh
cd Text-Summarization
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Training Model for Text Summarization

Use the following command to run Text-Summarization:

```sh
python main.py
```


###  Running Web App

Use the following command to run Text-Summarization:

```sh
python app.py
```

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/devesht21/Text-Summarization/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/devesht21/Text-Summarization/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/devesht21/Text-Summarization/issues)**: Submit bugs found or log feature requests for Text-summarization.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/devesht21/Text-Summarization
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

[**Return**](#-quick-links)

---
