# Go to project folder
# cd "/media/stephane/DATA/ESILV/A5/Dev Apps et Web services pour l'IOT/TP/Fichiers TP/"
pwd
ls

# delete all containers
printf "\n\nRemoving all containers\n"
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

# Re-aunching all containers
printf "\n\nRelaunching all containers\n"
docker-compose -f rabbitmq/docker-compose-rabbitmq.yml up -d
docker-compose -f mongodb/docker-compose-mongodb.yml up -d

sleep 5

# Re-launching all the configuration scripts
printf "\n\nRe-launching all the configuration scripts\n"
sh rabbitmq/rabbitmq-generate-config.sh

# Launching data geneation scripts
printf "\n\nLaunching data generation scripts\n"
docker-compose -f mock\ data/docker-compose-mock-data.yml up
# python3 ./rabbitmq/generate_data.py


