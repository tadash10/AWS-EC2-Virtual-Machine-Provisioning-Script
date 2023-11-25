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
