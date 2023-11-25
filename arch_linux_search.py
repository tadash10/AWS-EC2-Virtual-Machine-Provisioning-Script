import boto3

def search_arch_linux_ami():
    ec2_client = boto3.client('ec2')

    filters = [
        {'Name': 'name', 'Values': ['archlinux-*']},
        {'Name': 'description', 'Values': ['Arch Linux']}
    ]

    response = ec2_client.describe_images(Owners=['archlinux'], Filters=filters)

    if response['Images']:
        return response['Images'][0]
    else:
        print("Arch Linux AMI not found.")
        return None
