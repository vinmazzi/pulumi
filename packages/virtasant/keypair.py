import pulumi
import pulumi_aws as aws

class KeyPair:
    def __init__(self):
        pass

    def aws_create(self, name, public_key, environment):
        try:
            subnet = aws.ec2.KeyPair( 
                       name,
                       public_key=public_key,
                       key_name=name,
                       tags={
                           "Name": name,
                           "Environment": environment
                       }
                    )
        except:
            raise
        return subnet
