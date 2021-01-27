import pulumi
import pulumi_aws as aws

class Volume:
    def __init__(self):
        pass

    def aws_create(self, name, availability_zone, size, volume_type, environment):
        try:
            volume = aws.ebs.Volume( 
                       name,
                       availability_zone=availability_zone,
                       size=size,
                       tags={
                           "Name": name,
                           "Environment": environment
                       }
                    )
        except:
            raise
        return volume
