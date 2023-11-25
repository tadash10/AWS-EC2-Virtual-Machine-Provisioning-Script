def create_ec2_instance(ec2_client, ami_id, instance_type, security_groups, key_name):
    try:
        response = ec2_client.run_instances(
            ImageId=ami_id,
            InstanceType=instance_type,
            SecurityGroups=security_groups,
            KeyName=key_name,
            MinCount=1,
            MaxCount=1,
        )

        instance_id = response['Instances'][0]['InstanceId']
        public_ip = response['Instances'][0].get('PublicIpAddress', 'N/A')

        print("Instance created successfully!")
        print(f"Instance ID: {instance_id}")
        print(f"Public IP: {public_ip}")

        return instance_id
    except Exception as e:
        print(f"Failed to create EC2 instance. Error: {str(e)}")
        return None
