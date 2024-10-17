I have chosen API https://api.citybik.es/v2/#net_resource that has details of all the city bikes in a particular city like city, country, id, company, lat and long. 

I have created a folder called project3 which contains my flask container.

Upon executing the code it will give all the details of networks and details if we give id.

@app.route('/network/<network_id>', methods=['GET'])
def get_network_by_id(network_id):
    response = requests.get(f"{CITYBIKES_API_BASE}/{network_id}")
    network = response.json()
    return jsonify(network)

Next, to run it through the docker I'll create a dockerfile which will have details of port and my python file. It will help me in running it in the docker.

I'll also create a text file which will have the flask and requests versions. 

Flask==2.3.2
requests==2.31.0

Now, i'll start my docker container and enter the powershell.

docker login 

and then 

docker build -t bikeapp .

to built a new container

i'll run it in my port to docker run -p 5000:5000 bikeapp

now you can access the API through docker as well

use docker commit f76 bikeapp to commit

here tag the docker 

docker tag bikeapp aftab1234/bikeapp

use docker push aftab1234/bikeapp to push it to the docker hub

Now you will be able to see your docker repositary in hub.docker.com


