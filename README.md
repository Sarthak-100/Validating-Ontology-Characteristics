# Project Title: Ontology Validation System

## Description
This project develops a robust system that validates ontologies using Language Models (LMs) and publicly available Knowledge Graphs (KGs). The system processes ontology files to perform a series of validation tasks ensuring the correctness and effectiveness of ontological structures and properties.

### Objectives
- Validate the hierarchical relationships within ontologies.
- Ensure the correct definition of property domains and ranges.
- Identify and validate property characteristics such as symmetry, transitivity, and more.
- Maintain coherent property hierarchies

## Features
- **Ontology Hierarchy Validation:** Validates subclass-superclass relationships.
- **Property Domain/Range Validation:** Checks the correctness of domains and ranges assigned to properties.
- **Property Characteristics Identification:** Identifies if properties are symmetric, transitive, functional, or reflexive.
- **Property Hierarchy Validation:** Ensures proper structure in property hierarchies.

## Installation

```bash
git clone https://github.com/yourrepository/ontology-validation-system
cd ontology-validation-system
pip install -r requirements.txt
```

## Usage

To run the ontology validation, use the following command:

```bash
python validate_ontology.py <path_to_ontology_file>
```

Replace `<path_to_ontology_file>` with the path to your ontology file in TTL format.

## Project Structure

- `utils/` - Contains utility scripts and functions for loading models and ontologies.
- `task1.py` - Script for Ontology Hierarchy Validation.
- `task2.py` - Script for Property Domain/Range Validation.
- `task3.py` - Script for Property Characteristics Identification.
- `task4.py` - Script for Property Hierarchy Validation.
- `requirements.txt` - Required libraries and dependencies.

## Examples

### Validating Ontology Hierarchy

To validate the hierarchy of an ontology, run:

```bash
python task1.py 
```

### Checking Property Domains and Ranges

To validate property domains and ranges, run:

```bash
python task2.py 
```

## Contributing
We welcome contributions to improve the ontology validation system. Please feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments
- Thanks to the DBpedia community for providing accessible knowledge graphs.
- This project utilizes the following technologies:
  - [RDFLib](https://github.com/RDFLib/rdflib): A Python library for working with RDF.
  - [SPARQLWrapper](https://rdflib.github.io/sparqlwrapper/): A simple Python wrapper around a SPARQL service.