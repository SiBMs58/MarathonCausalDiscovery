# Marathon Performance Causal Analysis

This project analyzes the causal relationships between weather conditions and marathon performance using causal discovery algorithms. The analysis is currently implemented using the GES (Greedy Equivalence Search) algorithm, with support for PC (Peter-Clark) and LINGAM algorithms as alternative options.

## Data

The project currently uses a dummy dataset (`kipchoge-marathon-dummy-data.csv`) that includes:
- Finish time (in minutes)
- Average temperature
- Humidity
- Wind speed

## Analysis

The project uses causal discovery algorithms to:
1. Identify causal relationships between variables
2. Generate a causal graph showing how different factors influence marathon performance
3. Support multiple causal discovery algorithms (GES, PC, and LINGAM)

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`:
  - pandas
  - numpy
  - causalai (from Salesforce GitHub repository)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/SiBMs58/marathon-causal-analysis.git
cd marathon-causal-analysis
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the analysis:
```bash
python main.py
```

The script will:
1. Load and preprocess the data
2. Run the GES algorithm (by default)
3. Generate a causal graph in DOT format
4. Convert the DOT file to a PNG visualization
5. Save the results as `causal_graph.png`

## Output

The analysis produces:
- `causal_graph.dot`: DOT format representation of the causal graph
- `causal_graph.png`: Visualization of the causal relationships

## Algorithm Selection

The project supports multiple causal discovery algorithms:
- GES (Greedy Equivalence Search) - currently the default
- PC (Peter-Clark) algorithm
- LINGAM (Linear Non-Gaussian Acyclic Model)

To switch between algorithms, uncomment the relevant section in `main.py` and comment out the others.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

[Note: This README.md is Ai generated]
