import os
import torch


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DATASET_ROOT = os.path.join(PROJECT_ROOT, "dataset", "dataset_mask_rubsheet")
METEO_ROOT = os.path.join(PROJECT_ROOT, "dataset")
TRAIN_IMAGE_DIR = os.path.join(DATASET_ROOT, "train", "images")
TRAIN_CSV = os.path.join(METEO_ROOT, "meteo_data_train.csv")
VAL_IMAGE_DIR = os.path.join(DATASET_ROOT, "val", "images")
VAL_CSV = os.path.join(METEO_ROOT, "meteo_data_validation.csv")
TEST_IMAGE_DIR = os.path.join(DATASET_ROOT, "test", "images")
TEST_CSV = os.path.join(METEO_ROOT, "meteo_data_test.csv")

MODEL_SAVE_PATH = os.path.join(PROJECT_ROOT, "models", "mask_rubsheet_model.pth")
ANALYSIS_DIR = os.path.join(PROJECT_ROOT, "analysis", "mask_rubsheet")
LOG_DIR = os.path.join(PROJECT_ROOT, "logs")
LOG_FILE = os.path.join(LOG_DIR, "logs_mask_rubsheet.log")

# Hyperparameters
# Image size: 3355x534 (same as rubsheet, but with masked regions)
LEARNING_RATE = 0.0001
BATCH_SIZE = 8
NUM_EPOCHS = 27

# Normalization: [0, 1] -> [-1, 1]
NORMALIZE_MEAN = [0.5, 0.5, 0.5]
NORMALIZE_STD = [0.5, 0.5, 0.5]

# Other
RANDOM_SEED = 42

NUM_WORKERS = 4
PIN_MEMORY = True

DEVICE = torch.device("cuda")
