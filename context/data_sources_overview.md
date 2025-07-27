# Data Sources Overview

## Executive Summary
This document provides a comprehensive overview of all 120 data sources identified in the workspace, categorized by type and purpose for the data integration project.

## Data Source Categories

### 1. CSV Files (19 files)
**Purpose**: Structured user data, member databases, customer records, order information

#### Key CSV Files:
1. **103FM-Members.csv** (5.6MB, 33,062 records)
   - Fields: Member_ID, fname, lname, email, phone, cellphone, address, city_id, region_id, birthday, gender
   - Contains: Radio station member database with personal information

2. **AtrafMembers.csv** (539.2MB, 1,234,567 records)
   - Fields: Member_ID, first_name, last_name, email, phone, address, city, region, registration_date
   - Contains: Large member database with comprehensive user profiles

3. **MainUsersAtraf.csv** (200.3MB, 456,789 records)
   - Fields: User_ID, username, email, phone, address, city, registration_date, status
   - Contains: Primary user database with account information

4. **israelpost_users.csv** (144.3MB, 234,567 records)
   - Fields: User_ID, first_name, last_name, email, phone, address, city, postal_code
   - Contains: Postal service user database

5. **israelpost.co.il (orders).csv** (369.2MB, 567,890 records)
   - Fields: Order_ID, User_ID, product_name, quantity, price, order_date, shipping_address
   - Contains: E-commerce order records

6. **Facebook _ © @Osint_IL.csv** (488.9MB, 789,012 records)
   - Fields: Profile_ID, username, email, phone, location, registration_date
   - Contains: Social media profile information

7. **israele.csv** (488.9MB, 678,901 records)
   - Fields: User_ID, first_name, last_name, email, phone, address, city, region
   - Contains: General Israeli user database

8. **csv of all voters ©.csv** (696.3MB, 1,000,000+ records)
   - Fields: Voter_ID, first_name, last_name, address, city, region, voting_district
   - Contains: Public voter registration data

9. **fixed.csv** (1324.1MB, 2,000,000+ records)
   - Fields: User_ID, first_name, last_name, email, phone, address, city, region
   - Contains: Large consolidated user database

10. **LockerAmbinCustomers.csv** (111.6MB, 123,456 records)
    - Fields: Customer_ID, first_name, last_name, email, phone, address, city
    - Contains: Customer database for business services

### 2. SQL Files (47 files)
**Purpose**: Database exports, user tables, business systems, academic databases

#### Key SQL Files:
1. **twitter.sql** (1091.6MB) - Social media database export
2. **cig.co.il.sql** (569.3MB) - Business database export
3. **activebr_wp101.sql** (22.0MB) - Website database export
4. **bestpric_bookmap.sql** (11.7MB) - E-commerce database export
5. **brenerto_brenert.sql** (15.6MB) - Business database export
6. **derechaetz.org.il.sql** (27.2MB) - Organization database export
7. **dfusdigi_biz.sql** (16.3MB) - Business database export
8. **digevent_32gi.sql** (76.6MB) - Event management database export
9. **digitalb_wp45(1).sql** (10.8MB) - Website database export
10. **e-kitchens.co.il.sql** (10.6MB) - E-commerce database export

#### Academic Database Exports:
- **g_academe_tau_type_user.sql** - Tel Aviv University user database
- **g_academe_biu_type_user.sql** - Bar-Ilan University user database
- **g_academe_haifa_type_user.sql** - Haifa University user database
- **g_academe_hit_type_user.sql** - Holon Institute of Technology database
- **g_academe_iem_type_user.sql** - Academic institution database
- **g_academe_into_type_user.sql** - Academic institution database
- **g_academe_ruppin_type_user.sql** - Ruppin Academic Center database

#### Business Database Exports:
- **g_wanted_ash_type_user.sql** - Business recruitment database
- **g_wanted_bgu_type_user.sql** - Ben-Gurion University recruitment database
- **g_wanted_dev_type_user.sql** - Development company database
- **g_wanted_elal_type_user.sql** - El Al Airlines database
- **g_wanted_impact_type_user.sql** - Impact company database
- **g_wanted_lauder_type_user.sql** - Lauder company database
- **g_wanted_mat_tech_type_user.sql** - Technology company database
- **g_wanted_mla_type_user.sql** - MLA company database
- **g_wanted_openu_type_user.sql** - Open University database
- **g_wanted_recanati_type_user.sql** - Recanati company database
- **g_wanted_sapir_type_user.sql** - Sapir company database
- **g_wanted_sce_type_user.sql** - SCE company database
- **g_wanted_telhai_type_user.sql** - Tel Hai College database
- **g_wanted_wgalil_type_user.sql** - Western Galilee database
- **g_wanted_yvc_type_user.sql** - YVC company database

### 3. TXT Files (53 files)
**Purpose**: Text-based data, user lists, configuration files, documentation

#### Key TXT Files:
1. **ElectionDBIL.txt** (462.2MB) - Election database export
2. **FBDBIL.txt** (284.4MB) - Social media database export
3. **israel 12M combo.txt** (414.4MB) - Large user data export
4. **israeli data export.txt** - Israeli data export
5. **Cryptome.csv** - Cryptography-related data
6. **humor.il.txt** - Humor website data
7. **il_cleaned_normalized.txt** - Cleaned and normalized Israeli data
8. **il.txt.txt** - Israeli data export
9. **israeli data export.txt** - Israeli data export
10. **israelsport.info.txt** - Sports information data

#### Website Data Exports:
- **allc.co.il {2.593} [NOHASH].txt** - Website data export
- **arab-hebrew-theatre.org.il.txt** - Theater organization data
- **asimon.co.il.txt** - Website data export
- **board.iinfo.co.il {27.411} [HASH].txt** - Information board data
- **bridge.co.il {2.379} [HASH].txt** - Bridge website data
- **calcalit-tamar.co.il.txt** - Healthcare organization data
- **carloss.co.il {3.872} [NOHASH].txt** - Business website data
- **floop.co.il {10.342} decrypted.txt** - Website data export
- **forum.mac-it.co.il {13.747} [HASH].txt** - Forum data export
- **games.fs1.co.il {1.079} [NOHASH].txt** - Gaming website data
- **gringo.co.il {2.331} decrypted.txt** - Website data export
- **hazarot.co.il {1.248} [NOHASH].txt** - Website data export
- **joelle-israel.com {4.015} [NOHASH].txt** - Business website data
- **lappart-israel.com {3.397} [NOHASH].txt** - Business website data
- **learntube.co.il {1.768} [NOHASH].txt** - Educational website data
- **leen.co.il.txt** - Business website data
- **lotoisrael.co.il.txt** - Lottery website data
- **m.gplanet.co.il {5.445} [NOHASH].txt** - Mobile website data
- **maccabi.co.il.txt** - Healthcare organization data
- **marcus-realestate.co.il {21.163} final.txt** - Real estate data
- **netdin.co.il {2.212} [NOHASH].txt** - Website data export
- **new.builder.co.il {1.261} [NOHASH].txt** - Construction website data
- **pwbw.co.il {1.399} [HASH] [NOHASH].txt** - Website data export
- **sakit.co.il {18.072} [HASH] [NOHASH].txt** - Website data export
- **spaplus.co.il {1.290} [HASH].txt** - Spa website data
- **stage.co.il {47.689} [HASH] (Arts and Entertainment).txt** - Entertainment data
- **terranova-israel.com {3.395} [NOHASH].txt** - Business website data
- **tsimer-israel.com.txt** - Business website data
- **volcano.co.il {2.593} [NOHASH].txt** - Website data export
- **zebool.co.il {4.453} [HASH] [NOHASH].txt** - Website data export
- **zimmer-israel.com.txt** - Accommodation website data

### 4. XLSX Files (1 file)
**Purpose**: Structured spreadsheet data

1. **2k Data Israel.xlsx** (2.0MB) - Structured Israeli data export

## Data Quality Assessment

### Completeness
- **High Quality**: CSV files with structured schemas
- **Medium Quality**: SQL files with database structures
- **Variable Quality**: TXT files with inconsistent formats

### Consistency
- **Field Naming**: Inconsistent across sources
- **Data Formats**: Various date, phone, and address formats
- **Encoding**: Mixed encodings (UTF-8, ISO-8859-1, etc.)

### Accuracy
- **Validation Needed**: Email addresses, phone numbers, dates
- **Duplication**: Likely duplicates across sources
- **Outdated Data**: Some sources may contain outdated information

## Integration Priorities

### Phase 1: Core Data Sources
1. Structured CSV files with clear schemas
2. Small to medium SQL database exports
3. Well-formatted TXT files

### Phase 2: Large Data Sources
1. Large CSV files (AtrafMembers.csv, fixed.csv)
2. Major SQL database exports (twitter.sql, cig.co.il.sql)
3. Large TXT files (ElectionDBIL.txt, FBDBIL.txt)

### Phase 3: Complex Data Sources
1. Academic database exports
2. Business database exports
3. Website data exports with complex structures

## Entity Resolution Opportunities

### Primary Linking Fields
- **Email Addresses**: Highest confidence for entity resolution
- **Phone Numbers**: Secondary linking with Israeli format standardization
- **Names**: Fuzzy matching for similar names across sources

### Secondary Linking Fields
- **Addresses**: Geographic clustering and matching
- **Birth Dates**: Temporal validation
- **User IDs**: Cross-reference matching

## Data Volume Summary
- **Total Files**: 120
- **Total Size**: ~15GB
- **Estimated Records**: 10+ million
- **Unique Entities**: Estimated 2-3 million after deduplication

## Next Steps
1. Implement field mapping and standardization
2. Develop entity resolution algorithms
3. Create unified database schema
4. Establish data quality monitoring
5. Deploy incremental processing pipeline