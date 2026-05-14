# BUAN 446: Python for Data Analysts

**Lehigh University Graduate Course**  
6-week intensive | online asychronous 

## Course Overview

This repository contains comprehensive course materials for BUAN 446, a graduate-level Python course designed for first-year data analytics students. The course focuses on practical data analysis skills.

## Pedagogical Framework: CRAWL → WALK → RUN

This course implements a structured three-tier approach to AI integration in learning:

### 🐛 CRAWL Phase: Independent Learning
- **No AI assistance permitted**
- Students build foundational skills through direct practice
- DataCamp courses and textbook readings provide guided support
- Ensures mastery of core concepts needed for assessments

### 🚶 WALK Phase: AI as Learning Partner
- **AI permitted for understanding concepts only**
- Students use AI to clarify concepts, debug syntax, and explore alternatives
- Students must write their own code and understand their solutions
- Builds critical thinking about when and how to use AI effectively

### 🏃 RUN Phase: Full AI Collaboration
- **Full AI assistance permitted on projects**
- Students collaborate with AI to solve complex, real-world problems
- Emphasis on strategic thinking, problem decomposition, and validation
- Prepares students for professional data analyst workflows

**Assessment Balance**: Projects encourage AI collaboration while midterm and final exams are administered without AI access, ensuring students can demonstrate core competencies independently.

## Three-Dataset Progression

This course uses a structured three-dataset approach to mirror the professional data analyst journey:

1.  **Phase 1: Foundation (Weeks 1-2)**
    *   **Dataset**: `crestview_students_clean.csv` (7 variables, 600 records)
    *   **Goal**: Master Python syntax and logic without data quality distractions.
2.  **Phase 2: Reality Check (Week 3)**
    *   **Dataset**: `crestview_students_messy.csv` (8 variables, 605 records)
    *   **Goal**: Face the messy reality of corporate data. Learn systematic cleaning, standardization, and validation.
3.  **Phase 3: Analysis & Scale (Weeks 4-6)**
    *   **Dataset**: `crestview_students_extended.csv` (15 variables, 600 records)
    *   **Goal**: The "Reward Dataset." Use clean, rich data with double the variables to perform sophisticated multi-dimensional analysis with NumPy and Pandas.

## Repository Structure

```
buan446-python-for-data-analysts/
├── chapters/               # Interactive Jupyter notebooks for each chapter
├── assessments/           # Quizzes and exams (Moodle XML + Jupyter notebooks)
├── assignments/           # Weekly assignments and projects
├── data/                  # Course datasets (clean and messy versions)
└── README.md
```

## Course Content


**Chapter 1: Python Fundamentals**
- Variables, data types, and expressions
- Basic input/output operations
- Introduction to the Crestview student dataset

**Chapter 2: Control Flow**
- Conditional statements (if/elif/else)
- Iteration with for and while loops
- Loop control mechanisms

**Chapter 3: Functions**
- Function definition and calling
- Parameters, arguments, and return values
- Scope and modular programming

**Chapter 4: Data Structures**
- Lists, tuples, sets, and dictionaries
- Data structure operations and methods
- Choosing appropriate structures for tasks

**Chapter 5: File I/O and Exception Handling**
- Reading and writing text files
- CSV file processing
- Error handling with try/except blocks



**Chapter 6: NumPy**
- Array creation and vectorized operations
- Boolean indexing and statistical analysis
- Correlation analysis with extended dataset (15 variables)

**Chapter 7: Pandas**
- DataFrames, groupby, merge, pivot tables
- Multi-dimensional analysis with extended dataset
- Missing data handling and derived columns

**Chapter 8: Data Visualization**
- Matplotlib fundamentals and Seaborn statistical plots
- Multi-panel dashboards and correlation heatmaps
- Publication-quality figures and chart selection

**Chapter 9: Complete Data Analysis Workflow**
- End-to-end analysis pipeline
- Capstone project with 15-variable dataset
- Professional deliverables and executive summaries

## Case Study: Crestview University Student Data Progression

The course centers on a comprehensive synthetic dataset representing Crestview University students, evolving in complexity as your skills grow:

**1. Clean Dataset** (`crestview_students_clean.csv`)
- **Focus**: Weeks 1-2 (Python Fundamentals)
- 600 student records | 7 variables
- Purpose: Building confidence with core Python syntax.

**2. Messy Dataset** (`crestview_students_messy.csv`)
- **Focus**: Week 3 (Data Cleaning)
- 605 records | 8 variables | 28+ intentional issues
- Purpose: Mastering the "80% of the job" — handles inconsistent formatting, missing values, duplicates, and typos.

**3. Extended Dataset** (`crestview_students_extended.csv`)
- **Focus**: Weeks 4-6 (Advanced Analysis)
- 600 records | 15 variables | Clean & Rich
- Purpose: Unlocks sophisticated analysis (Study Hours, Financial Aid, Extracurriculars, etc.) using NumPy and Pandas.

### Data Quality Issues (Week 3 Challenge) Include:
- Inconsistent college name formatting (abbreviations, capitalization)
- Mixed case in categorical variables
- Missing values in various columns
- Duplicate student records
- Invalid GPA values (>4.0, negative numbers)
- Credits_Attempted stored as strings with formatting issues
- Invalid enrollment dates
- Extra whitespace and formatting inconsistencies

## Assessment Structure

### Quizzes (CRAWL Phase - No AI)
- Week 1: Chapters 1-2 (10 multiple choice questions)
- Week 2: Chapter 3 (10 multiple choice questions)
- Week 3: Chapters 4-5 (10 multiple choice questions)

### Midterm Exam (No AI)
**Part 1: Proctored Component**
- Multiple choice and short answer questions
- Covers Chapters 1-5 comprehensively
- Tests fundamental Python skills and concepts

**Part 2: Take-Home Project**
- Jupyter notebook-based analysis
- Uses clean Crestview student dataset
- Demonstrates ability to apply concepts independently

### Assignments (RUN Phase - Full AI Collaboration)
**Week 3: Data Cleaning Project** (100+ points)
- Six progressive parts guiding students through data quality challenges
- Inspect, clean, and validate the messy Crestview student dataset
- Requires strategic decision-making and documentation of cleaning choices

## Learning Objectives

By the end of this course, students will be able to:

1. Write clean, efficient Python code for data analysis tasks
2. Apply appropriate data structures to solve real-world problems
3. Read, process, and validate data from various file formats
4. Identify and correct data quality issues systematically
5. Use AI tools strategically while maintaining independent problem-solving skills
6. Document and communicate data analysis processes effectively

## Technical Requirements

- **Python**: 3.8 or higher
- **Required Libraries**: pandas, numpy, matplotlib, seaborn
- **Development Environment**: Jupyter Notebook or JupyterLab


## Installation

### Method 1: The "No-Code" Way (Recommended)

**1. Get the Software (One-Time Setup)**
*   **Install [Anaconda](https://www.anaconda.com/download):** This installs Python, Jupyter Notebook, and all the data libraries you need (Pandas, NumPy, etc.) in one click.
*   **Install [GitHub Desktop](https://desktop.github.com/):** This lets you download and update course files without using the command line.



**2. Get the Course Files**
*   Open **GitHub Desktop**.
*   Go to **File > Clone Repository**.
*   Select the **URL** tab and paste: `https://github.com/ejz218/python-for-data-analysts.git`
*   **Local Path:** Click "Choose..." and select your `Desktop` folder.
*   Click **Clone**.

**3. Start Coding**
*   Open **Anaconda Navigator**.
*   Click **Launch** under "Jupyter Notebook".
*   In the browser tab that opens, click **Desktop**, then **python-for-data-analysts**.
*   Click on specific chapter notebooks (e.g., `chapters/Chapter1_Python_Fundamentals.ipynb`) to open them.

### Method 2: The Command Line Way (Advanced)

If you prefer using the terminal (Mac) or Command Prompt/PowerShell (Windows):

**Mac / Linux:**
```bash
# 1. Navigate to Desktop
cd ~/Desktop

# 2. Clone the repository
git clone https://github.com/ejz218/python-for-data-analysts.git
cd python-for-data-analysts

# 3. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 4. Install packages
pip install jupyter pandas numpy matplotlib seaborn
```

**Windows:**
```powershell
# 1. Navigate to Desktop
cd $HOME\Desktop

# 2. Clone the repository
git clone https://github.com/ejz218/python-for-data-analysts.git
cd python-for-data-analysts

# 3. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 4. Install packages
pip install jupyter pandas numpy matplotlib seaborn
```

## Usage

### For Students

1. Start with Chapter 1 and progress sequentially
2. Follow the CRAWL → WALK → RUN framework for each topic
3. Complete DataCamp courses before attempting chapter exercises
4. Practice with the clean dataset before tackling messy data challenges
5. Document your learning process and AI interactions

### For Instructors

This repository can be adapted for your own Python for Data Analytics courses:

- Modify the case study dataset to fit your institution or domain
- Adjust the AI integration framework to match your pedagogical goals
- Customize assessment difficulty and point values
- Add or remove chapters based on semester length

## Data Privacy Note

All student data in this repository is **100% synthetic** and generated specifically for educational purposes. No real student information is included. The data is designed to be realistic enough for learning while maintaining complete privacy.

## Contributing

This is an educational repository. If you find errors or have suggestions for improvements:

1. Open an issue describing the problem or enhancement
2. For significant changes, please discuss in an issue before submitting a pull request
3. Follow existing code style and documentation patterns

## License

This course material is provided for educational purposes. Please contact the course instructor before using or adapting materials for other courses.

## Contact

**Course Instructor**: Eric Zematis
**Institution**: Lehigh University  
**Course**: BUAN 446 - Python for Data Analysts

## Acknowledgments

- DataCamp integration for supplementary learning resources
- Lehigh University College of Business for supporting innovative AI-integrated pedagogy

---

*Last Updated: May 2026*
