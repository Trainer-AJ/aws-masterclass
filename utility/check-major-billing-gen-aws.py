import boto3
import json

def list_dms_replication_instances(dms_client):
    instances = dms_client.describe_replication_instances()
    return [instance['ReplicationInstanceIdentifier'] for instance in instances['ReplicationInstances']]

def list_eips(ec2_client):
    eips = ec2_client.describe_addresses()
    return [eip['PublicIp'] for eip in eips['Addresses']]

def list_ebs_volumes(ec2_client):
    volumes = ec2_client.describe_volumes()
    return [volume['VolumeId'] for volume in volumes['Volumes']]

def list_ebs_snapshots(ec2_client):
    snapshots = ec2_client.describe_snapshots(OwnerIds=['self'])
    return [snapshot['SnapshotId'] for snapshot in snapshots['Snapshots']]

def list_ec2_instances(ec2_client):
    instances = ec2_client.describe_instances()
    return [instance['InstanceId'] for reservation in instances['Reservations'] for instance in reservation['Instances']]

def list_config_rules(config_client):
    rules = config_client.describe_config_rules()
    return [rule['ConfigRuleName'] for rule in rules['ConfigRules']]

def list_rds_instances(rds_client):
    instances = rds_client.describe_db_instances()
    return [instance['DBInstanceIdentifier'] for instance in instances['DBInstances']]

def list_macie_findings(macie_client):
    findings = macie_client.list_findings()
    return [finding['Id'] for finding in findings['FindingIds']]

def list_ecs_clusters(ecs_client):
    clusters = ecs_client.list_clusters()
    return [cluster_arn for cluster_arn in clusters['clusterArns']]

def get_all_regions():
    ec2_client = boto3.client('ec2')
    regions = ec2_client.describe_regions()
    return [region['RegionName'] for region in regions['Regions']]

def main():
    regions = get_all_regions()
    print("AWS Regions:", regions)

    for region in regions:
        print(f"\nChecking resources in region: {region}")
        
        # Initialize clients for each service
        dms_client = boto3.client('dms', region_name=region)
        ec2_client = boto3.client('ec2', region_name=region)
        config_client = boto3.client('config', region_name=region)
        rds_client = boto3.client('rds', region_name=region)
        macie_client = boto3.client('macie2', region_name=region)
        ecs_client = boto3.client('ecs', region_name=region)
        
        # List DMS Replication Instances
        dms_instances = list_dms_replication_instances(dms_client)
        print(f"DMS Replication Instances: {dms_instances}")
        
        # List EIPs
        eips = list_eips(ec2_client)
        print(f"Elastic IPs: {eips}")
        
        # List EBS Volumes
        ebs_volumes = list_ebs_volumes(ec2_client)
        print(f"EBS Volumes: {ebs_volumes}")
        
        # List EBS Snapshots
        ebs_snapshots = list_ebs_snapshots(ec2_client)
        print(f"EBS Snapshots: {ebs_snapshots}")
        
        # List EC2 Instances
        ec2_instances = list_ec2_instances(ec2_client)
        print(f"EC2 Instances: {ec2_instances}")
        
        # List AWS Config Rules
        config_rules = list_config_rules(config_client)
        print(f"AWS Config Rules: {config_rules}")
        
        # List RDS Instances
        rds_instances = list_rds_instances(rds_client)
        print(f"RDS Instances: {rds_instances}")
        
        # List Macie Findings
        macie_findings = list_macie_findings(macie_client)
        print(f"Macie Findings: {macie_findings}")
        
        # List ECS Clusters
        ecs_clusters = list_ecs_clusters(ecs_client)
        print(f"ECS Clusters: {ecs_clusters}")

if __name__ == "__main__":
    main()
