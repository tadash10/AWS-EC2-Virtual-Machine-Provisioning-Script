import boto3

def search_gentoo_ami():
    ec2_client = boto3.client('ec2')

    filters = [
        {'Name': 'name', 'Values': ['gentoo-*']},
        {'Name': 'description', 'Values': ['Gentoo']}
    ]

    response = ec2_client.describe_images(Owners=['gentoo'], Filters=filters)

    if response['Images']:
        return response['Images'][0]
    else:
        print("Gentoo AMI not found.")
        return None
