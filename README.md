# FinShield

## Digital Lending Risk Intelligence & Safety Hub

FinShield is an ML-based digital lending risk assessment platform that helps
users evaluate potentially risky instant-loan applications before installing
or using them.

It combines application metadata, regulatory indicators, lending disclosures,
review sentiment, and other risk signals into an explainable assessment.

> FinShield is an informational decision-support tool, not a financial, legal,
> or regulatory authority.

## Live Demo

[Launch FinShield](https://finshield---loan-app-detectorgit-bywwrgim8e5mbnpnzn3qme.streamlit.app/)

## Problem

Digital lending applications can expose borrowers to excessive permissions,
unclear disclosures, misleading information, high borrowing costs, and abusive
recovery practices. Users often lack a simple way to evaluate these risks
before using an application.

FinShield addresses this by combining multiple risk indicators into one
user-friendly and explainable assessment.

## Solution

FinShield evaluates lending applications using application-level and
review-based signals.

It provides:

- Risk score and risk level
- Legitimate or potentially predatory assessment
- RBI and regulatory indicators
- Terms and disclosure assessment
- Review sentiment and harassment-related signals
- Key risk drivers and explanations
- Borrower Safety Profile
- Evaluated lending-app rankings
- Loan-cost and APR calculators
- Digital lending safety guidance

The goal is to explain why an application may be considered risky rather than
simply displaying a score.

## Key Features

### 1. App Risk Scorer

Users can select a pre-analyzed application or audit an unlisted source using
an application identifier, URL, website, or package information.

The module provides:

- Overall risk assessment
- Visual Riskometer
- Individual risk indicators
- Explainable risk drivers
- Assessment status during analysis

### 2. Explainable Riskometer

Risk levels include:

`Low` · `Low–Moderate` · `Moderate` · `Moderately High` · `High` · `Very High`

Risk drivers may include regulatory status, disclosure quality, review
sentiment, harassment-related mentions, permission concerns, and other
compliance indicators.

### 3. Borrower Safety Profiler

A questionnaire evaluates lending and privacy-safety habits such as:

- Instant-loan usage
- Permission practices
- Lender verification
- Emergency-fund availability

It produces a Safety Index and borrower category.

### 4. Product Rankings

Users can search and compare evaluated lending applications using app names or
package IDs.

### 5. Financial Advisory Tools

#### Personal Loan Prepayment Calculator

- Monthly EMI
- Total interest
- Potential interest savings

#### Hidden Fees and True APR Detector

- Disbursed amount
- Repayment amount
- Loan duration
- Additional fees
- Annualized APR

### 6. RBI Safety Guidance

The application provides a simplified checklist covering areas such as:

- Key Fact Statement (KFS)
- Sensitive-data access
- Bank-account transfer requirements
- Grievance redressal
- Lender verification
- Cybercrime reporting

## How It Works

```text
User Input
    |
    v
Data Acquisition
    |
    v
Data Preprocessing
    |
    v
Feature Engineering
    |
    v
ML and Review Analysis
    |
    v
Risk Score and Level
    |
    v
Explainable Results
    |
    v
Safety Guidance
```

## ML-Based Risk Assessment

FinShield uses a machine-learning classification pipeline to distinguish
between legitimate and potentially predatory lending applications. The model
combines multiple application-level signals rather than relying on a single
rating.

### Reported Project Evaluation

| Metric | Value |
| --- | ---: |
| Manually verified loan applications | 80+ |
| Model accuracy | 88% |
| Prediction time | Approximately 2 seconds per app |

These figures represent the project evaluation during development and may
change as the dataset and model are expanded or retrained.

## Review and Sentiment Analysis

FinShield derives the following indicators from user reviews:

- Average review sentiment
- Strongly negative review percentage
- Harassment-related mentions
- Review-length characteristics

These signals are combined with application-level indicators for broader risk
assessment.

## Technology Stack

| Technology | Purpose |
| --- | --- |
| Python | Application and ML pipeline |
| Streamlit | Web application |
| Scikit-learn | Model training, evaluation, and prediction |
| VADER Sentiment | Review sentiment analysis |
| Pandas and NumPy | Data processing and numerical computation |
| Google Play metadata collection | App metadata and review collection |
| PyMuPDF | PDF text and table extraction |
| Git | Version control and collaboration |

## Project Structure

```text
FinShield/
├── .streamlit/
├── core/
│   ├── __init__.py
│   ├── config.py
│   ├── data.py
│   ├── explanations.py
│   ├── features.py
│   └── scoring.py
├── app_final.py
├── Googleplay_scraper.py
├── Pipeline_notebook.ipynb
├── dataset_dla_check.ipynb
├── app_features_final.csv
├── app_metadata_clean.csv
├── dla_dataset.csv
├── permissions_filled.csv
├── raw_reviews_clean.csv
├── predatory_loan_detector.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

### Core Modules

| Component | Purpose |
| --- | --- |
| `app_final.py` | Streamlit UI and application orchestration |
| `core/config.py` | Shared configuration, paths, and constants |
| `core/data.py` | Dataset/model loading and app lookup |
| `core/features.py` | Disclosure and install-count feature creation |
| `core/explanations.py` | Human-readable risk explanations |
| `core/scoring.py` | ML prediction and known-entity detection |
| `Googleplay_scraper.py` | Google Play metadata and review collection |
| `Pipeline_notebook.ipynb` | Feature engineering and model analysis |
| `dataset_dla_check.ipynb` | DLA dataset inspection and validation |

The CSV files contain processed application, permission, regulatory, and review
data. The `.pkl` file contains the trained model artifact.

Local virtual environments, Python caches, notebook checkpoints, temporary
archives, logs, and other development artifacts should not be committed to
Git.

## Development Pipeline

```text
Google Play Store and public sources
                |
                v
          Data collection
                |
                v
        Raw and cleaned data
                |
                v
       Data preprocessing
                |
                v
       Feature engineering
                |
                v
          ML pipeline
                |
                v
        Model evaluation
                |
                v
           Deployment
                |
                v
          FinShield UI
```

## Getting Started

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

### 2. Create and Activate a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux or macOS

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app_final.py
```

The active modular-refactor work is isolated on the
`refactor/modularize-core` branch.

## Notebook Environment

The notebook must use the same Python environment where its packages are
installed. In VS Code, select the `venv` kernel for
`Pipeline_notebook.ipynb`.

If a package works in the terminal but not in a notebook cell, install it into
the active notebook kernel:

```python
%pip install seaborn matplotlib
```

Restart the notebook kernel after installation and rerun the cells from the
beginning.

## DLA Dataset

`dla_dataset.csv` is the provenance-aware RBI Public Directory dataset. It
contains RBI serial numbers, source pages and rows, regulated entities, DLA
links, owner/LSP details, grievance contacts, platform identifiers, and source
metadata.

RBI directory membership is regulatory evidence. It is not proof that an app
is safe, non-predatory, or legally compliant in every dimension. Do not use
`rbi_dla_listed` as a direct predatory/non-predatory training label.

## Current Modules

| Module | Purpose |
| --- | --- |
| App Risk Scorer | Evaluate lending-app risk |
| Borrower Safety Profiler | Assess borrower safety habits |
| Product Rankings | Search evaluated applications |
| Advisory Calculators | Understand loan costs and APR |
| RBI Guidelines | Provide lending-safety guidance |

## Objectives

FinShield aims to:

- Identify potentially risky lending applications before installation
- Make lending-safety indicators easier to understand
- Encourage verification through official regulatory resources
- Highlight privacy and harassment-related risks
- Help borrowers understand the cost of short-term loans
- Promote transparency and safer participation in digital lending

## Future Scope

- Continuous dataset expansion
- Automated end-to-end ML pipeline
- Easier model replacement and retraining
- Integration with live verification sources
- Browser extension
- Android application
- App-store and fintech-platform integration
- Larger-scale real-time monitoring

## Data and References

FinShield's project material references:

- Google Play Store: metadata, permissions, installs, ratings, and reviews
- Reserve Bank of India (RBI): digital lending guidelines and regulatory information
- Public regulatory and domain-specific sources concerning risky or predatory lending applications
- Custom datasets created through data collection, manual verification, and feature engineering

## Disclaimer

FinShield is an informational and decision-support tool.

A risk score should not be treated as definitive proof that an application is
legitimate, fraudulent, or illegal. Users should independently verify lenders
through official regulatory sources before sharing sensitive information or
entering into a financial agreement.

## Team

- **Team:** Synapesex
- **College:** Hindustan College of Science and Technology, Farah, Mathura
- **Team Leader:** Oorvi Kulshreshtha

## Vision

Make digital lending safer, more transparent, and easier to understand before
a borrower clicks **Install**.

FinShield brings risk assessment, borrower awareness, financial calculations,
and regulatory guidance together in one digital lending safety hub.