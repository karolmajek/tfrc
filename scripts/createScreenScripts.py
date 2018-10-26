with open("tasks_list",'r') as f:
    data = f.readlines()

nodes = ['node-1', 'node-2', 'node-3', 'node-4', 'node-5']

for i in range(1,100+1):
    nodes.append("pretpu-%03d"%i)
print(nodes, len(nodes))
for i in range(105):
    with open("105/%03d.sh"%i,'w') as f:
        pass
for i, d in enumerate(data):
    node_i = i%105
    d=d.replace('\n','')
    print(d,nodes[node_i])
    with open("105/%03d.sh"%node_i,'a') as f:
        f.write("python3 /home/karolmajek/tensorflow/models/research/object_detection/model_tpu_main.py --pipeline_config_path=%spipeline.config --model_dir=%s --num_train_steps=50000 --sample_1_of_n_eval_examples=1 --alsologtostderr --tpu_name=%s 2>&1 > logs/105_20181026/%s_%08d\n"%(d,d.replace('configs','logs/105_20181026/'+nodes[node_i]),nodes[node_i],nodes[node_i],i))
with open("runscreens.sh",'w') as f:
    for i in range(105):
        f.write("screen -S %s -dm bash -c \"sh ./105/%03d.sh\"\n"%(nodes[i],i))
