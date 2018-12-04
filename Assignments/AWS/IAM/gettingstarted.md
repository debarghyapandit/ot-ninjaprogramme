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

**IAM Features**

IAM gives you the following features:

- Shared access to your AWS account

You can grant other people permission to administer and use resources in your AWS account without having to share your password or access key.

- Granular permissions

You can grant different permissions to different people for different resources.
For example, you might allow some users complete access to Amazon Elastic Compute Cloud (Amazon EC2), Amazon Simple Storage Service (Amazon S3), Amazon DynamoDB, Amazon Redshift, and other AWS services.
For other users, you can allow read-only access to just some S3 buckets, or permission to administer just some EC2 instances, or to access your billing information but nothing else.

- Secure access to AWS resources for applications that run on Amazon EC2
You can use IAM features to securely provide credentials for applications that run on EC2 instances.
These credentials provide permissions for your application to access other AWS resources.
Examples include S3 buckets and DynamoDB tables.

- Multi-factor authentication (MFA)
You can add two-factor authentication to your account and to individual users for extra security.

- Identity federation
You can allow users who already have passwords elsewhere—for example, in your corporate network or with an internet identity provider—to get temporary access to your AWS account.

- Identity information for assurance
If you use AWS CloudTrail, you receive log records that include information about those who made requests for resources in your account. That information is based on IAM identities.

PCI DSS Compliance
IAM supports the processing, storage, and transmission of credit card data by a merchant or service provider, and has been validated as being compliant with Payment Card Industry (PCI) Data Security Standard (DSS). For more information about PCI DSS, including how to request a copy of the AWS PCI Compliance Package, see PCI DSS Level 1.

Integrated with many AWS services
For a list of AWS services that work with IAM, see AWS Services That Work with IAM.

Eventually Consistent
IAM, like many other AWS services, is eventually consistent. IAM achieves high availability by replicating data across multiple servers within Amazon's data centers around the world. If a request to change some data is successful, the change is committed and safely stored. However, the change must be replicated across IAM, which can take some time. Such changes include creating or updating users, groups, roles, or policies. We recommend that you do not include such IAM changes in the critical, high-availability code paths of your application. Instead, make IAM changes in a separate initialization or setup routine that you run less frequently. Also, be sure to verify that the changes have been propagated before production workflows depend on them. For more information, see Changes that I make are not always immediately visible.

Free to use
AWS Identity and Access Management (IAM) and AWS Security Token Service (AWS STS) are features of your AWS account offered at no additional charge. You are charged only when you access other AWS services using your IAM users or AWS STS temporary security credentials. For information about the pricing of other AWS products, see the Amazon Web Services pricing page.
