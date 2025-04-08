import pandas as pd
import numpy as np
from causalai.models.tabular.pc import PC
from causalai.models.tabular.lingam import LINGAM
from causalai.models.tabular.ges import GES


from causalai.data.tabular import TabularData
from causalai.data.transforms.time_series import StandardizeTransform
from causalai.models.common.prior_knowledge import PriorKnowledge
from causalai.models.common.CI_tests.partial_correlation import PartialCorrelation

# Load data
df = pd.read_csv('kipchoge-marathon-dummy-data.csv')
analysis_columns = ['finish_time_minutes', 'avg_temperature', 'humidity', 'wind_speed']
data_array = df[analysis_columns].values

# Standardize data
standardizer = StandardizeTransform()
standardizer.fit(data_array)
data_trans = standardizer.transform(data_array)

# Create data object
data_obj = TabularData(data_trans, var_names=analysis_columns)

from causalai.models.common.prior_knowledge import PriorKnowledge

pk = PriorKnowledge(
    root_variables=['finish_time_minutes'],
    leaf_variables=['avg_temperature', 'humidity', 'wind_speed'],)

"""# Run PC algorithm
pc = PC(
    data=data_obj,
    prior_knowledge=pk,
    CI_test=PartialCorrelation(),
    use_multiprocessing=False
)
result = pc.run(pvalue_thres=0.2, max_condition_set_size=2)"""

# Run the GES algorithm
ges = GES(
        data=data_obj,
        prior_knowledge=pk,
        )
result = ges.run()


""""# Run LINGAM algorithm
lingam = LINGAM(
        data=data_obj,
        prior_knowledge=pk,
        )
result = lingam.run(pvalue_thres=0.2)"""


# Generate DOT file
with open('causal_graph.dot', 'w') as f:
    f.write('digraph CausalGraph {\n')
    f.write('    rankdir=LR;\n')

    # Add nodes
    for var in analysis_columns:
        f.write(f'    "{var}";\n')

    f.write('\n')

    # Add edges based on PC results
    for target_var, info in result.items():
        parents = info.get('parents', [])
        for parent in parents:
            f.write(f'    "{target_var}" -> "{parent}";\n')

    f.write('}\n')


# Generate PNG file using Graphviz
import subprocess
subprocess.run(['dot', '-Tpng', 'causal_graph.dot', '-o', 'causal_graph.png'])