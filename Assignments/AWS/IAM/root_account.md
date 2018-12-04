# IAM and ROOT Account

When you first create an AWS account, you begin with a single sign-in identity that has complete access
to all AWS services and resources in the account. This identity is called the AWS account **root user**
and is accessed by signing in with the email address and password that you used to create the account.

- strongly recommend that you **do not use the root user** for your everyday tasks,
even the administrative ones.
- Instead, adhere to the best practice of using the root user only to create your **first IAM user**.
- Then securely lock away the root user credentials and use them to perform only a few account and service management tasks.

