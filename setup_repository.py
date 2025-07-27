#!/usr/bin/env python3
"""
Setup script to create all missing files for the data integration repository
"""

import os
from pathlib import Path

def create_file(filepath, content):
    """Create a file with the given content"""
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Created: {filepath}")

def main():
    """Create all missing files"""
    
    # Create .gitignore
    gitignore_content = """# Data Files - NEVER COMMIT SENSITIVE DATA
*.csv
*.sql
*.txt
*.xlsx
*.xls
*.accdb
*.zip
*.rar
*.7z

# Analysis Results - Contains sensitive data
data_analysis_results.json
data_analysis_summary.md

# Database Files
*.db
*.sqlite
*.sqlite3

# Configuration Files with Sensitive Data
DBconfig.txt
*.env
*.config

# Log Files
*.log
logs/

# Temporary Files
*.tmp
*.temp
temp/
tmp/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual Environment
venv/
env/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Backup Files
*.bak
*.backup
*.old

# Data Client Directory - ENTIRE DIRECTORY
../data_client/
../*.csv
../*.sql
../*.txt
../*.xlsx

# Specific Sensitive Files (if they exist in project)
103FM-Members.csv
AtrafMembers.csv
MainUsersAtraf.csv
israelpost_users.csv
israelpost.co.il (orders).csv
Facebook _ © @Osint_IL.csv
israele.csv
csv of all voters ©.csv
fixed.csv
LockerAmbinCustomers.csv
ElectionDBIL.txt
FBDBIL.txt
israel 12M combo.txt
twitter.sql
cig.co.il.sql
*.sql
*.txt
*.csv
*.xlsx

# Analysis Output Files
analysis_results/
output/
results/
"""
    
    create_file(".gitignore", gitignore_content)
    
    # Create README.md
    readme_content = """# Data Integration Project

## Project Overview
This project aims to integrate and link 120 disparate data sources (CSV, SQL, TXT, XLSX files) into a unified, structured database system. The goal is to create comprehensive user profiles by linking related information across multiple sources using entity resolution techniques.

## Project Structure
```
data_integration_project/
├── requirements/                    # Project requirements and specifications
│   └── data_integration_requirements.md
├── context/                        # Data source documentation and analysis
│   ├── index.txt                   # Main context index
│   ├── data_sources_overview.md    # Complete data sources overview
│   ├── field_mapping_schema.md     # Field standardization and mapping
│   ├── entity_resolution_rules.md  # Entity resolution algorithms
│   ├── integration_strategy.md     # Integration approach and methodology
│   ├── data_quality_assessment.md  # Data quality analysis
│   ├── data_analysis_results.json  # Raw analysis results
│   └── data_analysis_summary.md    # Analysis summary report
├── scripts/                        # Processing scripts and tools
│   ├── data_extractor.py          # Data extraction script
│   ├── data_processor.py          # Data processing script
│   ├── entity_resolver.py         # Entity resolution script
│   └── main_pipeline.py           # Main orchestration script
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## Data Sources Summary
- **Total Files**: 120 data sources
- **CSV Files**: 19 (User profiles, member databases, customer records)
- **SQL Files**: 47 (Database dumps, user tables, business systems)
- **TXT Files**: 53 (Email/password lists, user data, credentials)
- **XLSX Files**: 1 (Structured user data)

## Key Features

### 1. Comprehensive Data Analysis
- Automated analysis of all data sources
- Schema extraction and field mapping
- Data quality assessment
- File size and encoding detection

### 2. Entity Resolution System
- Email-based primary linking
- Phone number secondary linking
- Fuzzy name matching
- Confidence scoring system

### 3. Field Standardization
- Unified field naming conventions
- Data type harmonization
- Format standardization
- Encoding handling

### 4. Quality Assurance
- Data validation rules
- Quality monitoring
- Error handling
- Audit trails

## Installation and Setup

### Prerequisites
- Python 3.8+
- MySQL/PostgreSQL database
- Sufficient storage space (10GB+ recommended)

### Installation
1. Clone or download the project
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Data Analysis
Run the data analyzer to examine all data sources:
```bash
cd scripts
python data_analyzer.py
```

### 2. Full Pipeline
Run the complete data extraction and processing pipeline:
```bash
cd scripts
python main_pipeline.py --data-dir ../data_client --output-dir ../pipeline_output
```

### 3. Individual Stages
Run specific stages of the pipeline:
```bash
# Extraction only
python main_pipeline.py --stages extraction

# Processing only
python main_pipeline.py --stages processing

# Resolution only
python main_pipeline.py --stages resolution
```

## Security and Privacy

### Data Security
- Encryption at rest and in transit
- Role-based access control
- Comprehensive audit logging
- Data masking for sensitive information

### Privacy Compliance
- Data minimization principles
- Consent management
- Retention policies
- Right to deletion support

## License and Legal

### Data Usage
- Ensure compliance with data protection regulations
- Respect privacy rights and consent
- Implement appropriate security measures
- Follow ethical data handling practices

### Project License
This project is for educational and research purposes. Ensure proper authorization for data usage.

---

**Note**: This project handles sensitive personal data. Ensure compliance with all applicable privacy laws and regulations before implementation.
"""
    
    create_file("README.md", readme_content)
    
    # Create placeholder files for context
    create_file("context/data_sources_overview.md", "# Data Sources Overview\n\nThis file contains a comprehensive overview of all data sources.\n\n*Content to be populated*")
    create_file("context/field_mapping_schema.md", "# Field Mapping Schema\n\nThis file contains field standardization and mapping rules.\n\n*Content to be populated*")
    create_file("context/entity_resolution_rules.md", "# Entity Resolution Rules\n\nThis file contains entity resolution algorithms and strategies.\n\n*Content to be populated*")
    create_file("context/integration_strategy.md", "# Integration Strategy\n\nThis file contains the integration approach and methodology.\n\n*Content to be populated*")
    create_file("context/data_quality_assessment.md", "# Data Quality Assessment\n\nThis file contains data quality analysis and recommendations.\n\n*Content to be populated*")
    
    # Create placeholder files for scripts
    create_file("scripts/data_extractor.py", "#!/usr/bin/env python3\n\"\"\"\nData Extractor Script\nExtracts and processes data from various file formats\n\"\"\"\n\n# Content to be populated\nprint('Data Extractor - Placeholder')\n")
    create_file("scripts/data_processor.py", "#!/usr/bin/env python3\n\"\"\"\nData Processor Script\nHandles data cleaning, validation, and transformation\n\"\"\"\n\n# Content to be populated\nprint('Data Processor - Placeholder')\n")
    create_file("scripts/entity_resolver.py", "#!/usr/bin/env python3\n\"\"\"\nEntity Resolution Script\nLinks and deduplicates records across different data sources\n\"\"\"\n\n# Content to be populated\nprint('Entity Resolver - Placeholder')\n")
    create_file("scripts/main_pipeline.py", "#!/usr/bin/env python3\n\"\"\"\nMain Data Pipeline Script\nOrchestrates the entire data extraction and processing pipeline\n\"\"\"\n\n# Content to be populated\nprint('Main Pipeline - Placeholder')\n")
    
    print("\nRepository setup completed!")
    print("All files have been created. You can now:")
    print("1. Add files to git: git add .")
    print("2. Commit: git commit -m 'Initial commit'")
    print("3. Push to GitHub: git remote add origin https://github.com/Noamcelermajer/Data_extractor.git")
    print("4. Push: git push -u origin master")

if __name__ == "__main__":
    main() 