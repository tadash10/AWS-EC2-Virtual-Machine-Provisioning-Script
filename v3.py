import boto3
import logging

class EC2ProvisioningScript:
    def __init__(self):
        self.ec2_client = boto3.client('ec2')
        self.logging_setup()

    def logging_setup(self):
        logging.basicConfig(filename='ec2_provisioning_log.txt', level=logging.INFO)

    def friendly_menu(self):
        print("Welcome to the EC2 Provisioning Script!")
        ami_options = self.get_ami_options()
        selected_ami = select_ami(ami_options)
        return selected_ami

    def get_ami_options(self):
        response = self.ec2_client.describe_images(Owners=['amazon'])
        ami_options = [{'Name': image['Name'], 'ImageId': image['ImageId']} for image in response['Images']]
        return ami_options

    def get_user_configuration(self):
        instance_type = get_user_input("Enter the instance type (e.g., t2.micro): ")
        security_groups = get_user_input("Enter security groups (comma-separated): ", input_type=lambda x: x.split(','))
        key_pair_name = get_user_input("Enter the key pair name: ")

        user_configuration = {
            'InstanceType': instance_type,
            'SecurityGroups': security_groups,
            'KeyName': key_pair_name,
        }

        return user_configuration

    def create_ec2_instance(self, selected_ami, user_configuration):
        try:
            response = self.ec2_client.run_instances(
                ImageId=selected_ami['ImageId'],
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

            self.log_instance_creation(instance_id, selected_ami['Name'])
        except Exception as e:
            print(f"Failed to create EC2 instance. Error: {str(e)}")

    def log_instance_creation(self, instance_id, ami_name):
        logging.info(f"Instance created - ID: {instance_id}, AMI: {ami_name}, Timestamp: {self.get_timestamp()}")

    def get_timestamp(self):
        import datetime
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    def select_ami(ami_options):
        print("Choose an EC2 AMI:")
        for i, ami in enumerate(ami_options, start=1):
            print(f"{i}. {ami['Name']} ({ami['ImageId']})")

        choice = input("Enter the number corresponding to your choice: ")

        try:
            selected_ami = ami_options[int(choice) - 1]
            return selected_ami
        except (ValueError, IndexError):
            print("Invalid choice. Please select a valid option.")
            return None

    def get_user_input(prompt, input_type=str):
        while True:
            try:
                user_input = input(prompt)
                return input_type(user_input)
            except ValueError:
                print("Invalid input. Please enter a valid value.")

    def main():
        ec2_script = EC2ProvisioningScript()
        selected_ami = ec2_script.friendly_menu()

        if selected_ami:
            user_config = ec2_script.get_user_configuration()
            if user_config:
                ec2_script.create_ec2_instance(selected_ami, user_config)

    main()
