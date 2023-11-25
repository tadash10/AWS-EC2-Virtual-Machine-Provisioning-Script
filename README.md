# AWS-EC2-Virtual-Machine-Provisioning-Script

#Overview

The EC2 Provisioning Script is a Python-based tool that automates the process of provisioning EC2 instances on Amazon Web Services (AWS). This script is designed to provide users with a streamlined and interactive experience for creating EC2 instances, allowing them to choose their preferred Amazon Machine Image (AMI), configure instance details, and receive real-time feedback.
Features

    Interactive Menu:
        An interactive menu allows users to choose from a list of available EC2 AMIs, enhancing the user experience and making the selection process intuitive.

    Parameterized Configuration:
        Users can specify instance details such as the type of EC2 instance, security groups, and key pairs, tailoring the configuration to their specific requirements.

    AWS SDK Integration:
        The script integrates with the AWS SDK (Boto3) to programmatically create EC2 instances based on user-defined parameters.

    Feedback and Confirmation:
        Users receive immediate feedback on the status of instance creation, including details such as instance ID and public IP address. Confirmation prompts ensure intentional execution.

    Error Handling:
        Robust error handling is implemented to manage potential issues during instance creation. Meaningful error messages and guidance are provided to users in case of errors.

    Logging:
        The script incorporates logging functionality to record information about instance creation, including timestamps and user details. This facilitates auditing and troubleshooting.

Usage
Prerequisites

    Python 3.x
    AWS credentials configured locally (AWS CLI)

Installation

    Clone the repository:

    bash

git clone https://github.com/your-username/ec2-provisioning-script.git

Navigate to the project directory:

bash

cd ec2-provisioning-script

Install dependencies:

bash

    pip install -r requirements.txt

Running the Script

Execute the script by running the following command:

bash

python main.py

Follow the on-screen prompts to choose an EC2 AMI and provide configuration details for the new instance.
Contributing

If you would like to contribute to the development of this script, please follow the guidelines outlined in CONTRIBUTING.md.
License

This project is licensed under the MIT License.

###     The search_arch_linux_ami function searches for an Arch Linux Server AMI owned by the 'archlinux' account.
    The search_gentoo_ami function searches for a Gentoo AMI owned by the 'gentoo' account.
    Each function returns the first matching AMI found or None if no matching AMI is found.
    Feel free to customize the filters or handling logic based on specific requirements.

You can integrate these functions into your main provisioning script by importing them and calling them as needed.
