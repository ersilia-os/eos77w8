# Adverse Drug Reactions

The model predicts the putative adverse drug reactions (ADR) of a molecule, using the SIDER database (MoleculeNet) that contains pairs of marketed drugs and their described ADRs. This model has been trained using the GROVER transformer (see eos7w6n or grover-embedding for a detail of the molecular featurization step with GROVER).

This model was incorporated on 2021-06-04.

## Information
### Identifiers
- **Ersilia Identifier:** `eos77w8`
- **Slug:** `grover-sider`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Homo sapiens`
- **Tags:** `Toxicity`, `MoleculeNet`, `Side effects`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `27`
- **Output Consistency:** `Fixed`
- **Interpretation:** Predicted ADRs classified in 27 groups

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| hepatobiliary_disorders | float | high | Probability of causing the side effect defined by SIDER |
| metabolism_nutrition_disorders | float | high | Probability of causing the side effect defined by SIDER |
| product_issues | float | high | Probability of causing the side effect defined by SIDER |
| eye_disorders | float | high | Probability of causing the side effect defined by SIDER |
| investigations | float | high | Probability of causing the side effect defined by SIDER |
| musculoskeletal_connective_tissue_disorders | float | high | Probability of causing the side effect defined by SIDER |
| gastrointestinal_disorders | float | high | Probability of causing the side effect defined by SIDER |
| social_circumstances | float | high | Probability of causing the side effect defined by SIDER |
| immune_system_disorders | float | high | Probability of causing the side effect defined by SIDER |
| reproductive_system_breast_disorders | float | high | Probability of causing the side effect defined by SIDER |

_10 of 27 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos77w8](https://hub.docker.com/r/ersiliaos/eos77w8)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos77w8.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos77w8.zip)

### Resource Consumption
- **Model Size (Mb):** `1323`
- **Environment Size (Mb):** `2410`


### References
- **Source Code**: [https://github.com/tencent-ailab/grover](https://github.com/tencent-ailab/grover)
- **Publication**: [https://arxiv.org/abs/2007.02835](https://arxiv.org/abs/2007.02835)
- **Publication Type:** `Preprint`
- **Publication Year:** `2020`
- **Ersilia Contributor:** [Amna-28](https://github.com/Amna-28)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos77w8
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos77w8
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
