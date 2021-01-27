import pulumi
import pulumi_aws as aws

class SecurityGroup:

    def __init__(self):
        pass

    def aws_prepare_rules(self, rules, direction):
        formated_rules = []
        for j in rules:
          count = 0
          args = ""
          for i in j.keys():
              if count > 0 and isinstance(j[i], str) and "[" in j[i]:
                  args = "{},{}={}".format(args, i, j[i])
              elif count > 0 and isinstance(j[i], str):
                  args = "{},{}=\"{}\"".format(args, i, j[i])
              elif count > 0 and isinstance(j[i], int):
                  args = "{},{}={}".format(args, i, j[i])
              elif count == 0 and isinstance(j[i], str):
                  args = "{}=\"{}\"".format(i, j[i])
              elif count == 0 and isinstance(j[i], int):
                  args = "{}={}".format(i, j[i])
              elif count == 0 and isinstance(j[i], str) and "[" in j[i]:
                  args = "{}={}".format(i, j[i])
              count += 1
          if direction == "ingress":
              formated_rules.append(eval("aws.ec2.SecurityGroupIngressArgs({})".format(args)))
          elif direction == "egress":
              formated_rules.append(eval("aws.ec2.SecurityGroupEgressArgs({})".format(args)))
        return formated_rules

    def aws_create(self, name, vpc_id, egress_rules, ingress_rules, environment):
        try:
            subnet = aws.ec2.SecurityGroup( 
                       name,
                       vpc_id=vpc_id,
                       ingress=self.aws_prepare_rules(ingress_rules, "ingress"),
                       egress=self.aws_prepare_rules(egress_rules, "egress"),
                       tags={
                           "Name": name,
                           "Environment": environment
                       }
                    )
        except:
            raise
        return subnet
