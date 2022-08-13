# Drug side effects

## Model Identifiers
* Slug: grover-sider
* Ersilia ID: eos77w8
* Tags: toxicity,	side-effect,	ADMET

## Model Description
Prediction of side effects based on Grover, a graph neural network for QSAR modelling based pretrained on a large unlabelled dataset. Grover has been fine-tuned using the using the Side Effect Resource (SIDER) database compiled by MoleculeNet. GROVER predictions consistently outperformed other state-of-the-art methods for SIDER and other benchmark datasets from MoleculeNet.
* Input: SMILES
* Output: Score	(Higher score indicates higher side effect potential)
* Model type: Regression
* Mode of Training: Pretrained
* Training data: 10,000,000	(https://paperswithcode.com/dataset/moleculenet)
* Experimentally validated: No

## Source code
This model was published by Yu R., Yatao B. et al. Self-Supervised Graph Transformer on Large-Scale Molecular Data. *arXiv Labs* 2018. DOI: https://doi.org/10.48550/arXiv.2007.02835
* Code: https://github.com/tencent-ailab/grover
* Checkpoints: https://github.com/tencent-ailab/grover/tree/main/grover/model

## License
The GPL-v3 license applies to all parts of the repository that are not externally maintained libraries. This repository uses the externally maintained library "grover", located at `/model` and licensed under an MIT license

## History
1. Model was downloaded on 12.05.21 from [TencentAILab](https://github.com/tencent-ailab/grover)
2. We duplicated task/predict.py and scripts/save_features.py from Tencent GitHub repository
3. Model was incorporated to Ersilia on 12/05/2021
