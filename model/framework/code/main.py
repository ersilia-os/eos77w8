# imports
import os
import csv
import sys
from grover.predict import grover_predict


if __name__ == '__main__':
    # parse arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # current file directory
    root = os.path.dirname(os.path.abspath(__file__))

    #No need to read the smiles from the main.py , the model will read itself.
    outputs, read_smiles = grover_predict(input_txt_path=input_file, output_path=output_file)

    #check input and output have the same lenght
    input_len = len(read_smiles)
    output_len = len(outputs)
    assert input_len == output_len
    
    header= [
    'hepatobiliary_disorders',
    'metabolism_nutrition_disorders',
    'product_issues',
    'eye_disorders',
    'investigations',
    'musculoskeletal_connective_tissue_disorders',
    'gastrointestinal_disorders',
    'social_circumstances',
    'immune_system_disorders',
    'reproductive_system_breast_disorders',
    'neoplasms_benign_malignant_unspecified_incl_cysts_polyps',
    'general_disorders_administration_site_conditions',
    'endocrine_disorders',
    'surgical_medical_procedures',
    'vascular_disorders',
    'blood_lymphatic_system_disorders',
    'skin_subcutaneous_tissue_disorders',
    'congenital_familial_genetic_disorders',
    'infections_infestations',
    'respiratory_thoracic_mediastinal_disorders',
    'psychiatric_disorders',
    'renal_urinary_disorders',
    'pregnancy_puerperium_perinatal_conditions',
    'ear_labyrinth_disorders',
    'cardiac_disorders',
    'nervous_system_disorders',
    'injury_poisoning_procedural_complications'
    ]

    # write output in a .csv file
    with open(output_file, "w") as f:
        writer = csv.writer(f)
        writer.writerow(header)  # header
        for o in outputs:
            writer.writerow(o)