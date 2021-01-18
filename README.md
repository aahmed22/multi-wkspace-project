# Creating Multiple Amazon WorkSpaces

Greetings Everyone, the purpose of this script is to automate the creation of multiple AWS Workspaces on your platform. 

Note: If you have an IAM account you will need to have access to the following:
- Permission to Workspaces service
- AWS access keys
- AD Connect is setup in your infrastructure 

For your local environment you will just need to have the following installed:
- Python
- Pip
- Boto3 sdk


## Placing Workspace Data in CSV file

The snippet below focuses on pulling the values set in a csv file called ***advanceBuild.csv*** 

In short the columns will be:  
**AD User id**, **Running Mode** (*ALWAYS_ON* or *AUTO_STOP*), **Compute Type** (*PERFORMANCE*, *POWER*, etc), **Tags**

The information will be pulled from  the CSV file and stored into several variables.  
Aferwards the function call to ***createMultipleWorkspaces*** will be made. 

```python
# The function "advanceBuildDeployment" will be the first portion of the script to be executed. 
# This will open the "advanceBuild.csv" file then begin to iterate through each record of the 
# csv file and take the columns and assign them to the respective values. 
# Finally "createMultipleWorkspaces" will be called.
def advanceBuildDeployment():
    with open("advanceBuild.csv", newline='', encoding='utf-8-sig') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        for record in readCSV:
            user_id = record[0]
            running_mode = record[1]
            compute_type = record[2]
            tag = record[3]

            print(record)
            print(f"User: {user_id}, R_Mode: {running_mode}, C_Type: {compute_type}, Tag: {tag} ")

            createMultipleWorkspaces(user_id, running_mode, compute_type, tag)
```          

## Create Multiple AWS WorkSpaces
The snippet below is rather self explanatory. The Boto3 create_workspaces skeleton is identical to the AWS Cli variation.  
In this portion you will specify the parameters associated with your AWS WorkSpace service.  
You will need to fill the following portions:  
**directory_id**, **bundle_id**, **volume_encryption_key**, **key**  

```python
# Created function called "createMultipleWorkspaces". This will take the record info from the csv file 
# and execute the built-in create_workspaces function from the boto3 package of "workspace service".
def createMultipleWorkspaces(username, r_mode, c_type, aws_tag):
    response = prod_client.create_workspaces(
        Workspaces=[
            {
                'DirectoryId': '**********',
                'UserName': username,
                'BundleId': '**********',
                'VolumeEncryptionKey': '**********',
                'UserVolumeEncryptionEnabled': True,
                'RootVolumeEncryptionEnabled': True,
                'WorkspaceProperties': {
                    'RunningMode': r_mode,
                    'RootVolumeSizeGib': 175,
                    'UserVolumeSizeGib': 100,
                    'ComputeTypeName': c_type
                },
                'Tags': [
                    {
                        'Key': '**********',
                        'Value': aws_tag
                    }
                ]
            }
        ]
    )
    print("\n\n\n")
    print(response)
    print("\n\n\n")
```

