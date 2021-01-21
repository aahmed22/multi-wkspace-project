# Author: Abdul-Hameed Ahmed
# DESCRIPTION: 
# The purpose of this script is to pull template info for creating new aws workspace profiles for multiple users.
# The script pulls the record info from a CSV file, primary columns are the following:
# User id, Running Mode, Compute Type, Tag
# END OF DESCRIPTION. 

# Importing both the boto3 and csv module into script.
import boto3
import csv

# Create a session and linking an AWS profile configured in local environment.
# Assign the session manipulating "AWS WorkSpace Service" to variable "prod_client".
session = boto3.Session(profile_name='**********', region_name='us-east-1')
prod_client = session.client('workspaces')

# Created function called "createMultipleWorkspaces". This will take the record info from the csv file 
# and execute the built-in create_workspaces function part of the boto3 package for "aws workspaces" service. 
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
    print(response)
    print("\n\n\n")
    print(f"Creating workspace for user: {username}, Running_mode: {r_mode}, Compute_type: {c_type}, Workspace Tag: {aws_tag} ")
    print("\n\n\n")


# The function "advanceBuildDeployment" will be the first portion of the script to be executed. This will open the "advanceBuild.csv" file
# then begin to iterate through each record of the csv file and take the columns and assign them to the respective values.
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



print("Beginning Process...")
advanceBuildDeployment()
