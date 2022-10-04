import random
import sys
import os
import numpy as np
import torch
import pandas as pd
from rdkit import RDLogger
from pathlib import Path
import tempfile

from grover.util.parsing import parse_args, get_newest_train_args
from grover.util.utils import create_logger
from task.cross_validate import cross_validate
from task.fingerprint import generate_fingerprints
from task.predict import make_predictions, write_prediction
from task.pretrain import pretrain_model
from grover.data.torchvocab import MolVocab
import scripts.save_features as sf

class Namespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

def setup(seed):
    # frozen random seed
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    random.seed(seed)
    torch.backends.cudnn.deterministic = True

def smiles_to_dataframe(txt_file_path):

    
    df = pd.read_csv(txt_file_path, header=None,  names=['smiles'])
    
    dummy_labels = pd.Series(np.zeros(df.shape[0]))

    names =    [    'Hepatobiliary disorders',
                	'Metabolism and nutrition disorders',
                	'Product issues',
                	'Eye disorders',
                  	'Investigations',
                    'Musculoskeletal and connective tissue disorders',
                    'Gastrointestinal disorders',
                    'Social circumstances',
                    'Immune system disorders',
                    'Reproductive system and breast disorders',
                    'Neoplasms benign, malignant and unspecified (incl cysts and polyps)',
                    'General disorders and administration site conditions',
                    'Endocrine disorders',
                    'Surgical and medical procedures',
                    'Vascular disorders',
                    'Blood and lymphatic system disorders',
                    'Skin and subcutaneous tissue disorders',
                    'Congenital, familial and genetic disorders',
                    'Infections and infestations',
                    'Respiratory, thoracic and mediastinal disorders',
                    'Psychiatric disorders',
                    'Renal and urinary disorders',
                    'Pregnancy, puerperium and perinatal conditions',
                    'Ear and labyrinth disorders',
                    'Cardiac disorders',
                    'Nervous system disorders',
                    'Injury, poisoning and procedural complications'     ]
    
    for n in names:
        df[n] = dummy_labels.values

    input_csv_path = txt_file_path.split(".")[0] + ".csv"
    df.to_csv(input_csv_path, index=False)
    
    return input_csv_path

    

if __name__ == '__main__':
    # setup random seed
    setup(seed=42)
    # Avoid the pylint warning.
    a = MolVocab
    # supress rdkit logger
    lg = RDLogger.logger()
    lg.setLevel(RDLogger.CRITICAL)

    # Initialize MolVocab
    mol_vocab = MolVocab

    input_txt_path =  sys.argv[1]
    output_path = sys.argv[2]
    csv_path = smiles_to_dataframe(input_txt_path)

    tmp_folder = tempfile.mkdtemp(prefix="ersilia-")
    tmp_file = os.path.join(tmp_folder, "features.npz")
        
    s = os.path.dirname(os.path.abspath(__file__))
    p = Path(s)
    model_path = str(p.parent.parent.absolute())

    args = Namespace(batch_size=32, checkpoint_dir=model_path+'/framework/finetune/sider', checkpoint_path=None, checkpoint_paths=[model_path+'/framework/finetune/sider/fold_0/model_0/model.pt', model_path+'/framework/finetune/sider/fold_2/model_0/model.pt', model_path+'/framework/finetune/sider/fold_1/model_0/model.pt'], cuda=False, data_path=csv_path, ensemble_size=3, features_generator=None, features_path=tmp_file, fingerprint=False, gpu=0, no_cache=True, no_features_scaling=True, output_path=output_path, parser_name='predict')


    sf.save_features_main(csv_path)

    train_args = get_newest_train_args()
    avg_preds, test_smiles = make_predictions(args, train_args)
    write_prediction(avg_preds, test_smiles, args)

    os.remove(csv_path)
