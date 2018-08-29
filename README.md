# stop_machines

## Abstract

These scripts stop ec2 instances via python-boto / python-boto3.

## How to use?

Please configure AWS credentials before executing these scripts.
[AWS official manual](https://aws.amazon.com/developers/getting-started/python/?nc1=h_ls) should help you.

Run stop_ec2.py or stop_ec2_boto3.py on your console.

```
$ python stop_ec2_boto3.py
```

You can also use:

* cron on any machines
* AWS CloudWatch and Lambda

to automatically stop instances on a ceartian time.

## How to exclude a certain instances?

You can use "Tags" of AWS to exclude a certain instances.
If some instances have a Tag which has Key=AutoStop and Value=False,
these scripts don't stop them.
