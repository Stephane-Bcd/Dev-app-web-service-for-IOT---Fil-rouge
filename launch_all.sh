# Go to project folder
cd "/media/stephane/DATA/ESILV/A5/Dev Apps et Web services pour l'IOT/TP/Fichiers TP/"
pwd
ls

# delete all containers
echo "removing all containers"
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

# Re-aunching all containers
echo "relaunching all containers"
docker-compose -f ./rabbitmq/docker-compose-rabbitmq.yml up -d
docker-compose -f ./mock\ data/docker-compose-mock-data.yml up
docker-compose -f ./mongodb/docker-compose-mongodb.yml up -d

# Launching data geneation scripts
echo "Launching data geneation scripts"
python3 ./rabbitmq/generate_data.py


