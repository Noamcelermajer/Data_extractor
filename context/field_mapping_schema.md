# Field Mapping Schema

## Overview
This document defines the standardized field mapping schema for the unified data integration system. It maps source-specific field names to standardized field names and defines data type conversions.

## Standardized Field Schema

### Core Personal Information Fields

#### Name Fields
| Standard Field | Data Type | Description | Source Variations |
|----------------|-----------|-------------|-------------------|
| `first_name` | VARCHAR(100) | First name | fname, firstname, name_first, given_name |
| `last_name` | VARCHAR(100) | Last name | lname, lastname, name_last, surname, family |
| `full_name` | VARCHAR(200) | Complete name | name, fullname, display_name, user_name |
| `middle_name` | VARCHAR(100) | Middle name | mname, middle, name_middle |

#### Contact Information Fields
| Standard Field | Data Type | Description | Source Variations |
|----------------|-----------|-------------|-------------------|
| `email` | VARCHAR(255) | Email address | email_address, mail, user_email, e_mail |
| `phone` | VARCHAR(20) | Primary phone number | phone_number, tel, telephone, area_phone |
| `cellphone` | VARCHAR(20) | Mobile phone number | mobile, cell, cellphone, area_cellphone |
| `fax` | VARCHAR(20) | Fax number | fax_number, fax_num |

#### Address Fields
| Standard Field | Data Type | Description | Source Variations |
|----------------|-----------|-------------|-------------------|
| `address` | VARCHAR(500) | Street address | street_address, addr, location, full_address |
| `city` | VARCHAR(100) | City name | city_name, town, municipality, locality |
| `region` | VARCHAR(100) | State/region | state, province, area, district |
| `postal_code` | VARCHAR(20) | Postal/ZIP code | zip, zipcode, postcode, postal |
| `country` | VARCHAR(100) | Country name | country_name, nation |

#### Personal Details Fields
| Standard Field | Data Type | Description | Source Variations |
|----------------|-----------|-------------|-------------------|
| `birth_date` | DATE | Date of birth | birthday, birthdate, dob, date_of_birth |
| `gender` | VARCHAR(10) | Gender | sex, g, gender_code |
| `nationality` | VARCHAR(100) | Nationality | citizenship, country_of_origin |

#### Identification Fields
| Standard Field | Data Type | Description | Source Variations |
|----------------|-----------|-------------|-------------------|
| `user_id` | VARCHAR(50) | User identifier | id, userid, member_id, customer_id |
| `username` | VARCHAR(100) | Username | login, user_name, account_name |
| `password_hash` | VARCHAR(255) | Password hash | password, pwd, pass_hash |

### Business and Professional Fields

#### Employment Fields
| Standard Field | Data Type | Description | Source Variations |
|----------------|-----------|-------------|-------------------|
| `company` | VARCHAR(200) | Company name | employer, organization, business |
| `job_title` | VARCHAR(100) | Job title | position, title, role, occupation |
| `department` | VARCHAR(100) | Department | dept, division, unit |

#### Academic Fields
| Standard Field | Data Type | Description | Source Variations |
|----------------|-----------|-------------|-------------------|
| `university` | VARCHAR(200) | University name | institution, college, school |
| `student_id` | VARCHAR(50) | Student identifier | student_number, academic_id |
| `graduation_year` | INT | Graduation year | grad_year, year_graduated |

### System and Metadata Fields

#### Timestamp Fields
| Standard Field | Data Type | Description | Source Variations |
|----------------|-----------|-------------|-------------------|
| `created_date` | DATETIME | Record creation date | date_created, created_at, registration_date |
| `updated_date` | DATETIME | Last update date | date_updated, modified_at, last_modified |
| `last_login` | DATETIME | Last login date | login_date, last_access |

#### Status Fields
| Standard Field | Data Type | Description | Source Variations |
|----------------|-----------|-------------|-------------------|
| `status` | VARCHAR(50) | Account status | account_status, user_status, is_active |
| `verified` | BOOLEAN | Email verification status | email_verified, verified_status |
| `enabled` | BOOLEAN | Account enabled status | is_enabled, active_status |

## Data Standardization Rules

### Phone Number Standardization
**Israeli Phone Format**: +972-XX-XXXXXXX
- **Mobile**: +972-5X-XXXXXXX (50-59)
- **Landline**: +972-XX-XXXXXXX (02, 03, 04, 08, 09)

**Standardization Process**:
1. Remove all non-digit characters
2. Handle Israeli prefixes (050 → +972-50)
3. Format with international standard

### Email Standardization
**Rules**:
1. Convert to lowercase
2. Remove leading/trailing whitespace
3. Validate email format
4. Handle common variations (gmail.com, googlemail.com)

### Name Standardization
**Rules**:
1. Remove common titles (Mr., Mrs., Dr., Prof.)
2. Convert to title case
3. Handle multiple spaces
4. Remove special characters (except hyphens and apostrophes)

### Date Standardization
**Target Format**: YYYY-MM-DD
**Source Formats**:
- DD/MM/YYYY
- MM/DD/YYYY
- DD-MM-YYYY
- MM-DD-YYYY
- YYYY-MM-DD

### Address Standardization
**Rules**:
1. Normalize street abbreviations (St., Ave., Blvd.)
2. Standardize city names
3. Handle postal code formats
4. Remove extra whitespace

## Source-Specific Field Mappings

### CSV File Mappings

#### 103FM-Members.csv
```json
{
  "Member_ID": "user_id",
  "fname": "first_name",
  "lname": "last_name",
  "User_NameForum": "username",
  "address": "address",
  "email": "email",
  "area_phone": "phone",
  "phone": "phone",
  "area_cellphone": "cellphone",
  "cellphone": "cellphone",
  "city_id": "city",
  "region_id": "region",
  "password": "password_hash",
  "birthday": "birth_date",
  "gender": "gender",
  "date": "created_date",
  "is_active": "enabled"
}
```

#### AtrafMembers.csv
```json
{
  "Member_ID": "user_id",
  "first_name": "first_name",
  "last_name": "last_name",
  "email": "email",
  "phone": "phone",
  "address": "address",
  "city": "city",
  "region": "region",
  "registration_date": "created_date"
}
```

#### israelpost_users.csv
```json
{
  "User_ID": "user_id",
  "first_name": "first_name",
  "last_name": "last_name",
  "email": "email",
  "phone": "phone",
  "address": "address",
  "city": "city",
  "postal_code": "postal_code"
}
```

### SQL File Mappings

#### Common SQL Field Patterns
```json
{
  "id": "user_id",
  "user_id": "user_id",
  "member_id": "user_id",
  "customer_id": "user_id",
  "email": "email",
  "email_address": "email",
  "phone": "phone",
  "telephone": "phone",
  "mobile": "cellphone",
  "cellphone": "cellphone",
  "first_name": "first_name",
  "fname": "first_name",
  "last_name": "last_name",
  "lname": "last_name",
  "name": "full_name",
  "full_name": "full_name",
  "address": "address",
  "street_address": "address",
  "city": "city",
  "town": "city",
  "state": "region",
  "region": "region",
  "zip": "postal_code",
  "postal_code": "postal_code",
  "birth_date": "birth_date",
  "birthday": "birth_date",
  "dob": "birth_date",
  "gender": "gender",
  "sex": "gender",
  "created_at": "created_date",
  "created_date": "created_date",
  "registration_date": "created_date",
  "updated_at": "updated_date",
  "modified_at": "updated_date",
  "status": "status",
  "is_active": "enabled",
  "active": "enabled"
}
```

### TXT File Mappings

#### Common TXT Field Patterns
```json
{
  "email": "email",
  "password": "password_hash",
  "username": "username",
  "name": "full_name",
  "phone": "phone",
  "address": "address"
}
```

## Field Priority for Confidence Scoring

### High Priority Fields (Weight: 1.0)
- `email` - Unique identifier
- `user_id` - System identifier
- `phone` - Contact identifier

### Medium Priority Fields (Weight: 0.8)
- `birth_date` - Personal identifier
- `full_name` - Name matching
- `address` - Location matching

### Low Priority Fields (Weight: 0.6)
- `city` - Geographic matching
- `region` - Geographic matching
- `gender` - Demographic matching

### Very Low Priority Fields (Weight: 0.4)
- `company` - Professional matching
- `university` - Academic matching
- `job_title` - Professional matching

## Data Type Conversions

### String to Date
```python
def convert_to_date(date_string):
    formats = ['%Y-%m-%d', '%d/%m/%Y', '%m/%d/%Y', '%d-%m-%Y', '%m-%d-%Y']
    for fmt in formats:
        try:
            return datetime.strptime(date_string, fmt).date()
        except ValueError:
            continue
    return None
```

### String to Boolean
```python
def convert_to_boolean(value):
    true_values = ['1', 'true', 'yes', 'active', 'enabled']
    false_values = ['0', 'false', 'no', 'inactive', 'disabled']
    
    if str(value).lower() in true_values:
        return True
    elif str(value).lower() in false_values:
        return False
    return None
```

### Phone Number Normalization
```python
def normalize_phone(phone_string):
    # Remove non-digits
    digits = re.sub(r'[^\d]', '', str(phone_string))
    
    # Handle Israeli numbers
    if len(digits) == 9 and digits.startswith(('50', '51', '52', '53', '54', '55', '56', '57', '58', '59')):
        return f"+972-{digits[1:3]}-{digits[3:]}"
    elif len(digits) == 8 and digits.startswith(('02', '03', '04', '08', '09')):
        return f"+972-{digits[1:3]}-{digits[3:]}"
    
    return phone_string
```

## Implementation Guidelines

### 1. Field Mapping Process
1. **Source Analysis**: Identify all unique field names
2. **Pattern Matching**: Apply standardized field mappings
3. **Manual Review**: Review unmapped fields
4. **Validation**: Verify mapping accuracy

### 2. Data Quality Checks
1. **Completeness**: Check for missing required fields
2. **Format Validation**: Validate data formats
3. **Range Checks**: Verify data within expected ranges
4. **Consistency**: Check for logical inconsistencies

### 3. Performance Optimization
1. **Indexing**: Create indexes on frequently queried fields
2. **Partitioning**: Partition large tables by date or region
3. **Caching**: Cache frequently accessed mappings
4. **Batch Processing**: Process data in batches for efficiency

## Next Steps
1. Implement field mapping algorithms
2. Create data validation rules
3. Develop data quality monitoring
4. Establish automated mapping updates
5. Deploy field standardization pipeline