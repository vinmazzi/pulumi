import pulumi
import pulumi_aws as aws

class Subnet:
    def __init__(self):
        pass

    def aws_create(self, name, vpc_id, assign_public_ip, cidr_block, environment):
        try:
            subnet = aws.ec2.Subnet( 
                       name,
                       vpc_id=vpc_id,
                       cidr_block=cidr_block,
                       map_public_ip_on_launch=assign_public_ip,
                       tags={
                           "Name": name,
                           "Environment": environment
                       }
                    )
        except:
            raise
        return subnet
