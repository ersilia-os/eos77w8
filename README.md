# Adverse Drug Reactions

The model predicts the putative adverse drug reactions (ADR) of a molecule, using the SIDER database (MoleculeNet) that contains pairs of marketed drugs and their described ADRs. This model has been trained using the GROVER transformer (see eos7w6n or grover-embedding for a detail of the molecular featurization step with GROVER).

## Identifiers

* EOS model ID: `eos77w8`
* Slug: `grover-sider`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `List`
* Interpretation: Predicted ADRs classified in 27 groups

## References

* [Publication](https://arxiv.org/abs/2007.02835)
* [Source Code](https://github.com/tencent-ailab/grover)
* Ersilia contributor: [Amna-28](https://github.com/Amna-28)

## Citation

If you use this model, please cite the [original authors](https://arxiv.org/abs/2007.02835) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a MIT license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!