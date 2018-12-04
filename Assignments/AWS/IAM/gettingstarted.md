# AWS Identity and Access Management

**What is IAM ?**

AWS Identity and Access Management (IAM) is a web service that helps us to:

- securely control & manage the access to aws resources.
- control who is authenticated (signed in) user.
- control who is authorized (has permissions) to use what diffrent available aws resources.

AWS Identity and Access Management (IAM) enables you to manage access to AWS services and resources securely.
- Using IAM, you can create and manage AWS users and groups, and
- Use permissions to allow and deny their access to AWS resources.
- No extra charge for IAM.
- You will be charged only for use of other AWS services by your users.


# IAM assists in creating roles and permissions

**AWS IAM allows you to:**

- Manage IAM users and their access – 

1.  You can create users in IAM,
2.  Assign them individual security credentials (in other words, access keys, passwords, and multi-factor authentication devices),
    or 
3.  Request temporary security credentials to provide users access to AWS services and resources.
4.  You can manage permissions in order to control which operations a user can perform.

- Manage IAM roles and their permissions – 

1.  You can create roles in IAM
2.  Manage permissions to control which operations can be performed by the entity, or AWS service, that assumes the role.
3.  You can also define which entity is allowed to assume the role.
4.  In addition, you can use service-linked roles to delegate permissions to AWS services that create and manage AWS resources on your behalf.

- Manage federated users and their permissions –

1.  You can enable identity federation to allow existing identities (users, groups, and roles) in your enterprise to access the AWS Management Console, call AWS APIs, and access resources, without the need to create an IAM user for each identity.
2.  Use any identity management solution that supports SAML 2.0, or use one of our federation samples (AWS Console SSO or API federation).

# IAM Best Practices

- Users – Create individual users.

- Groups – Manage permissions with groups.

- Permissions – Grant least privilege.

- Auditing – Turn on AWS CloudTrail.

- Password – Configure a strong password policy.

- MFA – Enable MFA for privileged users.

- Roles – Use IAM roles for Amazon EC2 instances.

- Sharing – Use IAM roles to share access.

- Rotate – Rotate security credentials regularly.

- Conditions – Restrict privileged access further with conditions.

- Root – Reduce or remove use of root.
