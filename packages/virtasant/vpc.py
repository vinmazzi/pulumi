import pulumi
import pulumi_aws as aws

class Vpc:
    def __init__(self):
        pass
    def aws_create(self, name, cidr_block, environment):
        try:
            vpc = aws.ec2.Vpc(name, cidr_block=cidr_block, enable_dns_hostnames=True, enable_dns_support=True)
        except:
            raise
        return vpc
