import urllib
import io
import pandas as pd
from tqdm import tqdm


## dataset_files: Pandas dataframe
## Input csv files to read including columns Dataset,Plate,Link

dataset_files = pd.read_csv("../datasets.csv")


def load_dataset(dataset_id, partition, features):
    """Load dataset from any collection of csv files

    Parameters
    ----------
    dataset_id: string
        Dataset ID
    partition:
        Partition can be "Train" or "Test"
    features:
        Feature type can be "CellProfiler" or "DeepLearning"

    Returns
    -------
    dataframe
        All read selected features from the bucket with given ID and partition

    """
    
    cond1 = dataset_files["Dataset"] == dataset_id
    cond2 = dataset_files["Partition"] == partition
    cond3 = dataset_files["Features"] == features
    df_row = dataset_files[cond1 & cond2 & cond3]
    
    if df_row.empty:
        print("No such partition {} for dataset {} with features {}".format(partition, dataset_id, features)) 
        return None    
    
    dataframes = []

    for key,row in tqdm(df_row.iterrows()):
        response = urllib.request.urlopen(row.Link)
        data = response.read()
        df = pd.read_csv(io.StringIO(data.decode('utf-8')))
        dataframes.append(df)
        
    return pd.concat(dataframes, ignore_index=True)


