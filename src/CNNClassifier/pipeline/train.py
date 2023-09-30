from CNNClassifier.config import ConfigurationManager
from CNNClassifier.components.train import Training
from CNNClassifier import logger

config = ConfigurationManager()

training_config = config.get_training_config()

training = Training(config=training_config)

training.get_base_model()
 
training.train_valid_generator()