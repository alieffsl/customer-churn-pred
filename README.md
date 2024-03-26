## Ujian Tengah Semester - Cloud Computing RK-A1

## Anggota Kelompok 12:
- M. Alief Faisal Hakim     162112233026
- Edbert Fernando           162112233030
- Kevin Oktavio Reyhannada	162112233016
- Muhamad Ridho Al Isya     162112233009
- Christopher Geoffrey	    162112233071

### Public URL: [http://34.128.67.116:8501/](http://34.128.67.116:8501/)

### Test the streamlit app on local:

1. Navigate to the `web_app/` directory:

```bash
    cd web_app/
```

2. Install required dependencies on local:

```commandline
pip install -r requirements.txt
```

3. Test the streamlit app on local:

```
streamlit run app.py
```


### Building the docker image

(Note: Run as administrator on Windows and remove "sudo" in commands)

1. Important - Make sure you have installed Docker on your PC:
- Linux: Docker
- Windows/Mac: Docker Desktop

2. Start Docker:
- Linux (Home Directory):
  ```
  sudo systemctl start docker
  ```
- Windows: You can start Docker engine from Docker Desktop.

#### Flask API:

3. Navigate to the `flask_api/` directory:

    ```bash
    cd flask_api/
    ```

4. Build the Docker image:

    ```bash
    docker build -t flask_api_image .
    ```

5. Run the Docker container:

    ```bash
    docker run -p 5000:5000 flask_api_image
    ```

#### Web App:

3. Navigate to the `web_app/` directory:

    ```bash
    cd ../web_app/
    ```

4. Build the Docker image:

    ```bash
    docker build -t web_app_image .
    ```

5. Run the Docker container:

    ```bash
    docker run -p 8501:8501 web_app_image
    ```

#### Access URLs

- Flask API: http://localhost:5000
- Web App: http://localhost:8501

6. In a different terminal window, you can check the running containers with:
```
sudo docker ps
```

7. Stop the container:
 - Use `ctrl + c` or stop it from Docker Desktop.

8. Check all containers:
 ```
 sudo docker ps -a
 ```

9. Delete the container if you are not going to run this again:
 ```
 sudo docker container prune
 ```

### Pushing the docker image to Docker Hub

10. Sign up on Docker Hub.

11. Create a repository on Docker Hub.

12. Log in to Docker Hub from the terminal. You can log in with your password or access token.
```
sudo docker login
```

13. Tag your local Docker image to the Docker Hub repository:
 ```
 sudo docker tag Image_ID username/repo-name:tag
 ```

14. Push the local Docker image to the Docker Hub repository:
 ```
 sudo docker push username/repo-name:tag
 ```

(If you want to delete the image, you can delete the repository in Docker Hub and force delete it locally.)

15. Command to force delete an image (but don't do this yet):
 ```
 $ sudo docker rmi -f IMAGE_ID
 ```
