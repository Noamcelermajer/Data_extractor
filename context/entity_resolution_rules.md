# Entity Resolution Rules

## Overview
This document defines the entity resolution rules and algorithms for linking and deduplicating records across all data sources in the unified database system.

## Entity Resolution Strategy

### Primary Linking Fields (Exact Match)
These fields provide the highest confidence for entity resolution:

#### 1. Email Address (Confidence: 1.0)
- **Matching Rule**: Exact match (case-insensitive)
- **Normalization**: Convert to lowercase, trim whitespace
- **Validation**: Basic email format validation
- **Priority**: Highest priority for linking

#### 2. User ID (Confidence: 1.0)
- **Matching Rule**: Exact match across systems
- **Normalization**: Standardize ID format
- **Validation**: Check for valid ID patterns
- **Priority**: High priority for system-level linking

#### 3. Phone Number (Confidence: 0.95)
- **Matching Rule**: Exact match after normalization
- **Normalization**: Israeli phone format (+972-XX-XXXXXXX)
- **Validation**: Phone number format validation
- **Priority**: High priority for contact linking

### Secondary Linking Fields (Fuzzy Match)

#### 4. Full Name (Confidence: 0.7-0.9)
- **Matching Rule**: Fuzzy string matching
- **Algorithm**: Levenshtein distance, Jaro-Winkler similarity
- **Normalization**: Remove titles, standardize case
- **Threshold**: 0.8 similarity for high confidence

#### 5. Birth Date (Confidence: 0.8)
- **Matching Rule**: Exact date match
- **Normalization**: Standardize to YYYY-MM-DD format
- **Validation**: Valid date range (1900-2024)
- **Priority**: High confidence when combined with name

#### 6. Address (Confidence: 0.6-0.8)
- **Matching Rule**: Address similarity matching
- **Algorithm**: Geographic clustering, address normalization
- **Normalization**: Standardize street names, city names
- **Threshold**: 0.7 similarity for medium confidence

## Entity Resolution Algorithms

### 1. Exact Match Algorithm
```python
def exact_match_resolution(records):
    """
    Perform exact match entity resolution
    """
    entities = {}
    
    for record in records:
        # Check email match
        email = normalize_email(record.get('email'))
        if email and email in entities:
            entities[email].append(record)
            continue
            
        # Check phone match
        phone = normalize_phone(record.get('phone'))
        if phone and phone in entities:
            entities[phone].append(record)
            continue
            
        # Check user ID match
        user_id = record.get('user_id')
        if user_id and user_id in entities:
            entities[user_id].append(record)
            continue
            
        # Create new entity
        entity_key = email or phone or user_id or generate_hash(record)
        entities[entity_key] = [record]
    
    return entities
```

### 2. Fuzzy Match Algorithm
```python
def fuzzy_match_resolution(records, threshold=0.8):
    """
    Perform fuzzy match entity resolution
    """
    entities = exact_match_resolution(records)
    
    for entity_key, entity_records in entities.items():
        for i, record1 in enumerate(entity_records):
            for j, record2 in enumerate(entity_records[i+1:], i+1):
                similarity = calculate_similarity(record1, record2)
                if similarity >= threshold:
                    # Merge records into same entity
                    merge_records(entity_records, i, j)
    
    return entities
```

### 3. Name Similarity Algorithm
```python
def calculate_name_similarity(name1, name2):
    """
    Calculate similarity between two names
    """
    # Normalize names
    norm1 = normalize_name(name1)
    norm2 = normalize_name(name2)
    
    # Exact match
    if norm1.lower() == norm2.lower():
        return 1.0
    
    # Levenshtein distance
    distance = levenshtein_distance(norm1, norm2)
    max_length = max(len(norm1), len(norm2))
    similarity = 1 - (distance / max_length)
    
    # Jaro-Winkler similarity
    jaro_similarity = jaro_winkler_similarity(norm1, norm2)
    
    # Return average of both similarities
    return (similarity + jaro_similarity) / 2
```

### 4. Address Similarity Algorithm
```python
def calculate_address_similarity(addr1, addr2):
    """
    Calculate similarity between two addresses
    """
    # Normalize addresses
    norm1 = normalize_address(addr1)
    norm2 = normalize_address(addr2)
    
    # Split into components
    components1 = norm1.split()
    components2 = norm2.split()
    
    # Calculate component similarity
    matches = 0
    for comp1 in components1:
        for comp2 in components2:
            if comp1.lower() == comp2.lower():
                matches += 1
                break
    
    # Calculate similarity score
    total_components = max(len(components1), len(components2))
    return matches / total_components if total_components > 0 else 0.0
```

## Confidence Scoring System

### Confidence Calculation
```python
def calculate_confidence_score(record1, record2):
    """
    Calculate confidence score for entity resolution
    """
    scores = {}
    
    # Email matching (highest weight)
    email1 = normalize_email(record1.get('email'))
    email2 = normalize_email(record2.get('email'))
    if email1 and email2:
        scores['email'] = 1.0 if email1 == email2 else 0.0
    
    # Phone matching
    phone1 = normalize_phone(record1.get('phone'))
    phone2 = normalize_phone(record2.get('phone'))
    if phone1 and phone2:
        scores['phone'] = 1.0 if phone1 == phone2 else 0.0
    
    # Name matching
    name1 = record1.get('full_name') or f"{record1.get('first_name', '')} {record1.get('last_name', '')}"
    name2 = record2.get('full_name') or f"{record2.get('first_name', '')} {record2.get('last_name', '')}"
    if name1 and name2:
        scores['name'] = calculate_name_similarity(name1, name2)
    
    # Birth date matching
    birth1 = record1.get('birth_date')
    birth2 = record2.get('birth_date')
    if birth1 and birth2:
        scores['birth_date'] = 1.0 if birth1 == birth2 else 0.0
    
    # Address matching
    addr1 = record1.get('address')
    addr2 = record2.get('address')
    if addr1 and addr2:
        scores['address'] = calculate_address_similarity(addr1, addr2)
    
    # Calculate weighted average
    weights = {
        'email': 1.0,
        'phone': 0.95,
        'name': 0.7,
        'birth_date': 0.8,
        'address': 0.6
    }
    
    if not scores:
        return 0.0
    
    weighted_sum = sum(scores[field] * weights[field] for field in scores)
    total_weight = sum(weights[field] for field in scores)
    
    return weighted_sum / total_weight
```

## Deduplication Rules

### 1. Exact Duplicate Detection
- **Criteria**: All fields match exactly
- **Action**: Keep one record, mark others as duplicates
- **Confidence**: 1.0

### 2. Near-Duplicate Detection
- **Criteria**: High similarity score (>0.9)
- **Action**: Merge records, keep best quality data
- **Confidence**: 0.9-1.0

### 3. Potential Duplicate Detection
- **Criteria**: Medium similarity score (0.7-0.9)
- **Action**: Flag for manual review
- **Confidence**: 0.7-0.9

### 4. Non-Duplicate
- **Criteria**: Low similarity score (<0.7)
- **Action**: Treat as separate entities
- **Confidence**: <0.7

## Record Merging Strategy

### 1. Field Priority for Merging
```python
FIELD_PRIORITY = {
    'email': 1,
    'phone': 2,
    'user_id': 3,
    'full_name': 4,
    'birth_date': 5,
    'address': 6,
    'city': 7,
    'region': 8,
    'gender': 9,
    'created_date': 10
}
```

### 2. Merge Algorithm
```python
def merge_records(records):
    """
    Merge multiple records into a single entity
    """
    merged_record = {}
    
    # Sort records by data quality score
    sorted_records = sorted(records, key=lambda x: calculate_data_quality(x), reverse=True)
    
    for field in FIELD_PRIORITY:
        # Find the best value for this field
        best_value = None
        for record in sorted_records:
            if record.get(field):
                best_value = record[field]
                break
        
        if best_value:
            merged_record[field] = best_value
    
    return merged_record
```

### 3. Data Quality Assessment
```python
def calculate_data_quality(record):
    """
    Calculate data quality score for a record
    """
    quality_score = 0
    total_fields = 0
    
    for field, value in record.items():
        if value:
            total_fields += 1
            # Add quality points based on field completeness and format
            if is_valid_format(field, value):
                quality_score += 1
            else:
                quality_score += 0.5
    
    return quality_score / total_fields if total_fields > 0 else 0.0
```

## Source Trust Scoring

### 1. Source Reliability Factors
- **Data Freshness**: Recent data gets higher trust
- **Data Completeness**: Complete records get higher trust
- **Data Accuracy**: Validated data gets higher trust
- **Source Reputation**: Known reliable sources get higher trust

### 2. Trust Score Calculation
```python
def calculate_source_trust(source_name, record):
    """
    Calculate trust score for a data source
    """
    base_trust = SOURCE_TRUST_SCORES.get(source_name, 0.5)
    
    # Adjust based on data quality
    quality_factor = calculate_data_quality(record)
    
    # Adjust based on data freshness
    freshness_factor = calculate_freshness_factor(record)
    
    # Adjust based on validation status
    validation_factor = calculate_validation_factor(record)
    
    return base_trust * quality_factor * freshness_factor * validation_factor
```

## Implementation Guidelines

### 1. Performance Optimization
- **Indexing**: Create indexes on linking fields
- **Batch Processing**: Process records in batches
- **Parallel Processing**: Use multiple threads for large datasets
- **Caching**: Cache similarity calculations

### 2. Quality Assurance
- **Manual Review**: Review low-confidence matches
- **Validation Rules**: Implement strict validation
- **Audit Trail**: Track all resolution decisions
- **Metrics Monitoring**: Monitor resolution quality

### 3. Scalability Considerations
- **Incremental Processing**: Process new data incrementally
- **Partitioning**: Partition data by geographic regions
- **Sharding**: Distribute processing across multiple servers
- **Memory Management**: Optimize memory usage for large datasets

## Confidence Thresholds

### 1. High Confidence (0.9-1.0)
- **Action**: Automatic linking
- **Review**: Not required
- **Use Case**: Production systems

### 2. Medium Confidence (0.7-0.9)
- **Action**: Flag for review
- **Review**: Automated + manual
- **Use Case**: Quality assurance

### 3. Low Confidence (0.5-0.7)
- **Action**: Manual review required
- **Review**: Manual only
- **Use Case**: Research and analysis

### 4. Very Low Confidence (<0.5)
- **Action**: No linking
- **Review**: Not applicable
- **Use Case**: Separate entities

## Next Steps
1. Implement entity resolution algorithms
2. Create confidence scoring system
3. Develop record merging strategy
4. Establish quality monitoring
5. Deploy resolution pipeline