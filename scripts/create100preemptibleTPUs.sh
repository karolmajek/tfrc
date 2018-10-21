for i in {1..100}
do
	ii=$(printf "%03d" $i)
	echo $i
	gcloud compute tpus create pretpu-$ii --network=default  --range=10.10.$i.0/29 --version=1.11   --preemptible --zone=us-central1-f & 
done
