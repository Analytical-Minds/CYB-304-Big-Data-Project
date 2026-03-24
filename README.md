# CYB-304-Big-Data-Project

A comprehensive big data analysis and machine learning project developed by Analytical-Minds, featuring data processing, visualization, and predictive modeling for cybersecurity applications.

## 📋 Project Overview

This repository contains a complete big data analytics pipeline developed for the CYB-304 course. The project encompasses data analysis, machine learning model development, NoSQL database integration, and interactive dashboard creation using R and Python.

### Key Objectives
- Process and clean large datasets for analysis
- Build predictive machine learning models
- Implement NoSQL database solutions for scalable data storage
- Create interactive dashboards for data visualization and insights
- Document findings and model performance metrics

---

## 🏗️ Project Structure

This project is organized into several directories, each serving a unique purpose in the overall architecture of the application. Below is an overview of the directory structure:

### `/data`
Contains all datasets used for training, validation, and testing. Each dataset is version controlled to ensure reproducibility.

### `/src`
This directory holds all source code for the project. It includes subdirectories for different components:
- **/components**: Reusable UI components.
- **/models**: Machine learning models including training scripts.
- **/utils**: Utility functions that support various functionalities throughout the project.

### `/notebooks`
Contains Jupyter notebooks utilized for explorative data analysis and visualization. Each notebook is properly documented for clarity.

### `/tests`
Holding unit tests and integration tests to ensure the reliability of the codebase. Tests are organized to mirror the structure of `/src` for easy navigation.

### `/docs`
Comprehensive documentation for the project, including setup guides, usage instructions, and API documentation. This directory is essential for onboarding new contributors.

### `/scripts`
Scripts for automating various tasks such as data preprocessing, evaluation metrics, and model deployment. Each script includes a brief description of what it does.

### `/config`
Configuration files for managing environment variables and settings necessary for running the application.

### `/requirements`
Contains all dependency listings necessary for the project, typically in a `requirements.txt` file for Python projects.

This structured approach enhances collaboration, increases code maintainability, and simplifies navigation through the project. Each section is designed to provide clarity on the purpose and organization of the files and directories, fostering a better understanding of the overall architecture.

---

## 🛠️ Technologies & Languages

**Primary Languages:**
- **Python** - Primary language for data processing and NoSQL operations
- **R** - Used for interactive dashboard creation with Shiny framework

**Key Libraries & Frameworks:**
- **R Shiny** - Interactive web application framework
- **Python Data Stack** - pandas, NumPy, scikit-learn for ML
- **NoSQL Database** - Database operations and schema management
- **Machine Learning** - Predictive modeling and decision tree analysis

---

## 📁 Core Files

### Application Files

#### `app.R`
R Shiny application for interactive dashboard visualization. This file creates the user interface and server-side logic for exploring data insights and model outputs.

**Key Features:**
- Interactive visualizations
- Real-time data exploration
- Multiple dashboard variants (A and B)
- User-friendly interface design

#### `nosql_app.py`
Python application handling NoSQL database operations, data persistence, and backend processing logic.

**Key Features:**
- NoSQL database connectivity
- Data ingestion and transformation
- Query optimization
- Schema management

### Documentation

#### `CYB 304 PROJECT.docx`
Comprehensive project documentation including:
- Project requirements and objectives
- Methodology and approach
- Task descriptions and specifications
- Results and conclusions
- References and citations

#### `model_schema.txt`
Database schema definitions and model specifications including:
- Table structures
- Field definitions
- Relationships and constraints
- Data types and validation rules

---

## 📊 Project Tasks

The project is organized into distinct tasks, each with corresponding visualizations:

### **Task 1: Data Exploration**
- Initial data exploration and understanding
- Dataset characteristics and statistics
- *Output: Task-1.png*

### **Task 2: Data Analysis**
- **Part A:** Primary analysis dimensions
  - *Output: Task-2A.png*
- **Part B:** Secondary analysis dimensions
  - *Output: Task-2B.png*

### **Task 3: Advanced Analysis**
- **Part A:** Deep-dive analysis and correlations
  - *Output: Task-3A.png*
- **Part B:** Pattern recognition and insights
  - *Output: Task-3B.png*

### **Task 4: Data Preparation**
- Integration of analysis findings
- *Output: Task-4.png*

### **Task 5: Machine Learning & Visualization**
- **Data Cleaning:** Data preprocessing and quality assurance
  - *Output: Task 5 Cleaning Data.png*
- **Model Development:** Decision tree and predictive models
  - *Output: Task 5 Decision tree.png*
- **Model Evaluation:** Performance metrics and confusion matrix
  - *Output: Task 5 Confusion Matrix.png*
- **Dashboard Design:** Two design variants for presentation
  - *Outputs: Task 5 Dashboard A.png, Task 5 Dashboard B.png*
- **Dashboard UI:** Implementation of dashboard interfaces
  - *Outputs: Task 5 Dashboard UI A.png, Task 5 Dashboard UI B.png*

### **Task 6: Results & Deployment**
- **Part A-D:** Final results and implementation details
  - *Outputs: Task-6A.png through Task-6D.png*

---

## 🚀 Getting Started

### Prerequisites
- **R** (version 3.5.0 or higher)
- **Python** (version 3.7 or higher)
- **Required R packages:** shiny, ggplot2, plotly, dplyr
- **Required Python packages:** pandas, numpy, scikit-learn, pymongo (or relevant NoSQL driver)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Analytical-Minds/CYB-304-Big-Data-Project.git
cd CYB-304-Big-Data-Project

