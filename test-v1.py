import boto3
import logging

class EC2ProvisioningScript:
    def __init__(self):
        self.ec2_client = boto3.client('ec2')
        self.logging_setup()

    def logging_setup(self):
        logging.basicConfig(filename='ec2_provisioning_log.txt', level=logging.INFO)

    def interactive_menu(self):
        print("Select your preferred Linux distribution:")
        print("1. Ubuntu")
        print("2. Amazon Linux")
        print("3. CentOS")

        choice = input("Enter the number corresponding to your choice: ")
        distributions = ['ubuntu', 'amazon', 'centos']

        try:
            selected_distribution = distributions[int(choice) - 1]
            return selected_distribution
        except IndexError:
            print("Invalid choice. Please select a valid option.")
            return None

    def get_user_configuration(self):
        instance_type = input("Enter the instance type (e.g., t2.micro): ")
        security_groups = input("Enter security groups (comma-separated): ").split(',')
        key_pair_name = input("Enter the key pair name: ")

        user_configuration = {
            'InstanceType': instance_type,
            'SecurityGroups': security_groups,
            'KeyName': key_pair_name,
        }

        return user_configuration

    def create_ec2_instance(self, distribution, user_configuration):
        try:
            response = self.ec2_client.run_instances(
                ImageId=f"ami-for-{distribution}",
                InstanceType=user_configuration['InstanceType'],
                SecurityGroups=user_configuration['SecurityGroups'],
                KeyName=user_configuration['KeyName'],
                MinCount=1,
                MaxCount=1,
            )

            instance_id = response['Instances'][0]['InstanceId']
            public_ip = response['Instances'][0].get('PublicIpAddress', 'N/A')

            print("Instance created successfully!")
            print(f"Instance ID: {instance_id}")
            print(f"Public IP: {public_ip}")

            self.log_instance_creation(instance_id, distribution)
        except Exception as e:
            print(f"Failed to create EC2 instance. Error: {str(e)}")

    def log_instance_creation(self, instance_id, distribution):
        logging.info(f"Instance created - ID: {instance_id}, Distribution: {distribution}, Timestamp: {self.get_timestamp()}")

    def get_timestamp(self):
        import datetime
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    ec2_script = EC2ProvisioningScript()

    distribution_choice = ec2_script.interactive_menu()
    if distribution_choice:
        user_config = ec2_script.get_user_configuration()
        if user_config:
            ec2_script.create_ec2_instance(distribution_choice, user_config)
