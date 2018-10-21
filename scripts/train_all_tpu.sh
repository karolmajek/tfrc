gsutil ls gs://tfrc_karol/configs | while read line ; do
   echo ====== $line ======
   echo python3 ~/tensorflow/models/research/object_detection/model_tpu_main.py --pipeline_config_path=${line}pipeline.config --model_dir=${line} --num_train_steps=50000 --sample_1_of_n_eval_examples=1 --alsologtostderr --tpu_name=node-2
done
