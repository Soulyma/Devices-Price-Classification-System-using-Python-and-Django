from django.apps import AppConfig
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
import pickle
from DevicesPriceClassification.settings import PIPLINE_DIR,MODEL_DIR

def load_pickle(path):
    with open(path, 'rb') as handle:
        loaded_var = pickle.load(handle)
    return loaded_var


class RestdevicespriceclassificationConfig(AppConfig):
    name = 'restdevicespriceclassification'
    
    pre_proc = load_pickle(PIPLINE_DIR)
    svm = load_pickle(MODEL_DIR)
