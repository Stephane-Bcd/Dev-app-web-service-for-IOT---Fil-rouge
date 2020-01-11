# Go to project folder
# cd "/media/stephane/DATA/ESILV/A5/Dev Apps et Web services pour l'IOT/TP/Fichiers TP/"
pwd
ls



# Installing prerequisites
printf "\n\nInstalling prerequisites\n"
sudo apt-get -y install python3-pip
pip3 install pymongo
pip3 install pika

# delete all containers
while true; do
    read -p "Do you wish to DELETE ALL CONTAINERS?" yn
    case $yn in
        [Yy]* ) printf "\n\nRemoving all containers\n"
            docker stop $(docker ps -a -q)
            docker rm $(docker ps -a -q); break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done


# Re-aunching all containers
printf "\n\nRelaunching all containers\n"
docker-compose -f rabbitmq/docker-compose-rabbitmq.yml up -d
docker-compose -f mongodb/docker-compose-mongodb.yml up -d

sleep 5

# Re-launching all the configuration scripts
printf "\n\nRe-launching all the configuration scripts\n"
sh rabbitmq/rabbitmq-generate-config.sh
python3 mongodb/mongodb_generate_config.py


# Launching data geneation scripts
printf "\n\nLaunching data generation scripts\n"
# docker-compose -f mock\ data/docker-compose-mock-data.yml up
python3 rabbitmq/generate_data.py


