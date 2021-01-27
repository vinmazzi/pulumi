import pulumi
import pulumi_aws as aws

class Instance:
    def __init__(self):
        pass

    def aws_create(self, name, ami_id, subnet_id, instance_type, key_name, root_volume_size, root_volume_type, assossiate_public_ip, security_groups, availability_zone, environment):
        try:
            instance = aws.ec2.Instance( 
                       name,
                       ami=ami_id,
                       availability_zone=availability_zone,
                       instance_type=instance_type,
                       subnet_id=subnet_id,
                       root_block_device=aws.ec2.InstanceRootBlockDeviceArgs(volume_size=root_volume_size, volume_type=root_volume_type, delete_on_termination=True),
                       key_name=key_name,
                       associate_public_ip_address=assossiate_public_ip,
                       vpc_security_group_ids=security_groups,
                       tags={
                           "Name": name,
                           "Environment": environment
                       }
                    )
        except:
            raise
        return instance
