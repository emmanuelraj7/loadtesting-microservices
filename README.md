

<!-- ABOUT THE PROJECT -->
## About The Demo

![Load Testing](https://github.com/emmanuelraj7/loadtesting-microservices.git/blob/main/images/load_test.png)



The demo is aimed at getting started with load testing a microservice before taking it to production. We use FastAPI microservice (to predict weather) and Locust to load test the service (locally or on cloud). You can find detailed instructions in the [Engineering MLOps](https://www.amazon.com/Engineering-MLOps-Rapidly-production-ready-learning/dp/1800562888) book.



### Built With

Major frameworks used to build the project:
* [FastAPI](https://fastapi.tiangolo.com/)
* [Docker](https://www.docker.com/)
* [Locust](https://locust.io/)


![FASTAPI](https://github.com/emmanuelraj7/loadtesting-microservices.git/blob/main/images/fast_api_service.png)


<!-- GETTING STARTED -->
### Installation

These are instructions to install and get the services up and running. 

1. Clone the repo
   ```sh
   git clone https://github.com/emmanuelraj7/loadtesting-microservices.git
   ```
2. Install Locust.io
   ```sh
   pip install locust
   ```   
3. Go to FastAPI_microservice folder and build the FastAPI service docker image 
   ```sh
   docker build -t fastapi .
   ```
4. Run the FastAPI service docker container locally
   ```sh
   docker run -d -p 80:80 fastapi
   ```
5. Go to Load_testing folder and run locust.io service for load testing
   ```sh
   Locust -f load_test-py
   ```   




<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Emmanuel Raj - [Linkedin](https://www.linkedin.com/in/emmanuelraj7/) 

Project Link: [https://github.com/emmanuelraj7/loadtesting-microservices](https://github.com/emmanuelraj7/loadtesting-microservices)

Engineering MLOps (book): [Amazon](https://www.amazon.com/Engineering-MLOps-Rapidly-production-ready-learning/dp/1800562888)
