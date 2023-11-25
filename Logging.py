def log_instance_creation(instance_id, ami_name):
    logging.info(f"Instance created - ID: {instance_id}, AMI: {ami_name}, Timestamp: {get_timestamp()}")
