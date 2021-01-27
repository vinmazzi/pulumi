from packages.virtasant.vpc import Vpc as vpc
from packages.virtasant.subnet import Subnet as subnet
from packages.virtasant.securitygroup import SecurityGroup as sg
from packages.virtasant.keypair import KeyPair as keypair
from packages.virtasant.volume import Volume as volume
from packages.virtasant.instance import Instance as instance

import pulumi

#TODO: THESE VARIABLES COULD ALSO BE REPLACED BY AN YAML FILE

environment = "development"
#vpc_variables
vpc_core_cidr = "10.90.0.0/16"
vpc_name = "customer1_vpc"
#subnet_variables
subnet_name = "customer1_dev_subnet"
subnet_dev_cidr = "10.90.10.0/24"
subnet_assign_public_ip = False
#provisioning_key variables
provisioning_key_name = "provisioning_ssh_key"
provisioning_public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDLE/nd+R19/dohbUPxaiCHreTBeE/hs1rbGeF8Png6Rl6L9sV2aJXPgJW+jNd/a5OGO2WJUTy3/UZsGscP2jO1tIGKbHhj5Wrztc0B6nGRCjYPQHGbK53Oh7jq4dQ4v0zUilmW9JarsNfB2IEy55O+J7eEwqmOzOdTIwozJQshjj2lPDt1dVJQAyiwQJxzP9V2C9usXkNGV9PSm+Iqyjk2l8xpQI7pbpzEVDzi5MeMQCGWnxYNkAbjSF0ubiSXEU55O7da9YrA1rN7ani+gOPtghK76TzWh87N1NeRc02vvxzlhdMn180QsGi6BXRdT9tj1U4eI+bLoDXlqKNX+DRv"
#instance variables
instance_name = "customer1_dev_nginx_instance"
instance_ami = "ami-0affd4508a5d2481b"
instance_type = "t2.micro"
availability_zone = "us-east-1a"
root_volume_size = 55
root_volume_type = "gp2"

#SecurityGroup Variables
security_group_name = "customer1_dev_nginx_sg"
ingress_rules = [{
     "description": "Nginx port",
     "from_port": 0,
     "to_port": 443,
     "protocol": "tcp",
     "cidr_blocks": '["10.90.10.0/24"]'
    }]

egress_rules = [{
     "description": "All Traffic",
     "to_port": 0,
     "from_port": 0,
     "protocol": "-1"
    }]

customer1_vpc                   = vpc().aws_create(vpc_name, vpc_core_cidr, "core")
customer1_dev_subnet            = subnet().aws_create(subnet_name, customer1_vpc.id, subnet_assign_public_ip, subnet_dev_cidr, environment)
customer1_dev_securitygroup     = sg().aws_create(security_group_name, customer1_vpc.id, egress_rules, ingress_rules, environment)
customer1_dev_provisioning_key  = keypair().aws_create(provisioning_key_name, provisioning_public_key, environment)
customer1_dev_nginx_instance    = instance().aws_create(instance_name, instance_ami, customer1_dev_subnet.id, instance_type, provisioning_key_name, root_volume_size, root_volume_type, subnet_assign_public_ip, [customer1_dev_securitygroup.id], availability_zone, environment)

pulumi.export('Vpc_id', customer1_vpc.id)
pulumi.export('Dev_Subnet_id', customer1_dev_subnet.id)
pulumi.export('Dev_nginx_security_group_id', customer1_dev_securitygroup.id)
pulumi.export('Dev_provisioning_key_id',customer1_dev_provisioning_key.id)
pulumi.export('Dev_nginx_instance_id', customer1_dev_nginx_instance.id)
