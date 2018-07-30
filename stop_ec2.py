from boto import ec2

ec2conn = ec2.connect_to_region("ap-northeast-1")
all_instances = [i for r in ec2conn.get_all_instances() for i in r.instances]

instances_to_stop = []
for instance in all_instances:
    tags = instance.tags 
    if tags.get('AutoStop') != 'false':
        instances_to_stop.append(instance.id)

print('# the target to be stopped')
for instance in instances_to_stop:
    print(instance) 

ec2conn.stop_instances(instances_to_stop)
