from azureml.core.model import InferenceConfig

classifier_inference_config = InferenceConfig(runtime= "python",
                                              source_directory = '',
                                              entry_script="scoring_script.py",
                                              conda_file="env.yml")