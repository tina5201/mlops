# House Price Prediction — MLOps Project

A machine-learning project that predicts house prices using a trained regression model. This repository demonstrates model training, a Flask web application, API testing, Docker containerization, Kubernetes deployment, AWS EC2 hosting, and CI/CD automation with GitHub Actions.

## Project Overview

The application accepts house details such as area, bedrooms, bathrooms, and age, then returns a predicted price using the trained model.

### Key Features
- Machine-learning model training and saved model artifact
- Flask web interface for house-price prediction
- Health-check endpoint
- Input validation and error handling
- Automated tests using pytest
- Docker image configuration
- Kubernetes Deployment and Service manifests
- AWS EC2 deployment workflow
- GitHub Actions CI/CD workflow

## Technology Stack

- **Language:** Python
- **Machine Learning:** scikit-learn, NumPy, pandas
- **Web Application:** Flask
- **API Framework:** FastAPI and Uvicorn (where configured)
- **Testing:** pytest, httpx
- **Containerization:** Docker
- **Orchestration:** Kubernetes / k3s
- **Cloud:** AWS EC2
- **CI/CD:** GitHub Actions

## Repository Structure

```text
mlops/
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── schemas.py
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── model/
│   └── train.py
├── models/
│   └── house_price_model.pkl
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── tests/
│   ├── __init__.py
│   └── test_api.py
├── app.py
├── Dockerfile
├── environment.yml
├── requirements.txt
├── .dockerignore
├── .gitignore
└── README.md
```

## Prerequisites

Install the following tools before running the project:

- Python
- Git
- Docker (for containerization)
- kubectl and a Kubernetes cluster (for Kubernetes deployment)
- AWS account and EC2 access (for cloud deployment)

## 1. Clone the Repository

```bash
git clone https://github.com/tina5201/mlops.git
cd mlops
```

## 2. Install Dependencies

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Install the required packages:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If PowerShell blocks environment activation, you can run the environment's Python executable directly or use an appropriate terminal configuration.

## 3. Train the Machine-Learning Model

Run the training script from the project root:

```bash
python model/train.py
```

The training script should save the trained model under the `models/` directory. Confirm the output path in `model/train.py` if your script uses a different filename.

## 4. Run the Flask Web Application

Start the Flask application:

```bash
python app.py
```

Open the application in your browser:

- **Local application:** http://127.0.0.1:5000
- **Health check:** http://127.0.0.1:5000/health

The health endpoint reports the application status and whether the model is loaded.

The prediction endpoint is:

```text
POST /prediction
```

Example JSON request:

```json
{
  "area": 1500,
  "bedrooms": 3,
  "bathrooms": 2,
  "age": 5
}
```

Send JSON to `http://127.0.0.1:5000/prediction` using Postman or curl. The response contains the predicted price or an error message if the input is invalid.

Stop the local server with `Ctrl+C`.

## 5. Run the API Application

The repository also contains API-related files under `app/`. If `app/main.py` defines a FastAPI application named `app`, start it from the repository root with:

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Open the API documentation:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **OpenAPI schema:** http://127.0.0.1:8000/openapi.json

These commands apply to the FastAPI application only. The actual routes depend on the implementation in `app/main.py`.

## 6. Run Tests

Run the test suite from the project root:

```bash
pytest -v
```

To run a specific test file:

```bash
pytest tests/test_api.py -v
```

Review the test output and resolve any failures before deployment.

## 7. Build and Run with Docker

Build the Docker image:

```bash
docker build -t house-price-api .
```

Run the container:

```bash
docker run --rm -p 8000:8000 house-price-api
```

If the Dockerfile starts the FastAPI application on port 8000, open:

http://127.0.0.1:8000/docs

**Note:** The Docker command must match the port and startup command configured in the repository's `Dockerfile`. If the application uses a different internal port, update the port mapping accordingly.

## 8. Kubernetes Deployment

The repository includes Kubernetes manifests under `k8s/`.

Check your cluster connection:

```bash
kubectl get nodes
```

Apply the deployment and service:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Check the deployed resources:

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

Inspect application logs:

```bash
kubectl logs deployment/house-price-api
```

The deployment name in the logs command must match the name configured in `k8s/deployment.yaml`.

For a NodePort service, check the assigned port:

```bash
kubectl get service
```

If the service is configured to use NodePort `30080`, the application may be reachable at:

```text
http://<SERVER_PUBLIC_IP>:30080
```

The exact endpoint depends on the application and service configuration.

## 9. AWS EC2 Deployment

The project was previously accessed using an AWS EC2 public IP and Kubernetes NodePort.

### Previously Used Deployment Links

- **API Swagger Documentation:** http://16.171.199.228:30080/docs
- **Health Check:** http://16.171.199.228:30080/health

These are the previously used URLs, not a guarantee that the deployment is currently online. The EC2 instance must be running, the public IP must still match, the Kubernetes service and application must be healthy, and the required inbound port must be allowed by the EC2 security group.

### Verify the Deployment

1. Open the AWS Management Console.
2. Navigate to EC2 → Instances.
3. Select the deployment instance and check its state and Public IPv4 address.
4. Connect to the instance and verify Kubernetes pods and services.
5. Confirm the service port and security-group rules.
6. Open the Swagger or health-check URL in a browser.

If the public IP has changed, replace the IP in the URLs with the current EC2 public IP.

## 10. CI/CD with GitHub Actions

The workflow is located at:

```text
.github/workflows/ci-cd.yml
```

GitHub Actions can automate configured steps such as dependency installation, testing, image building, or deployment. The actual jobs and triggers are defined in the workflow file.

To review workflow results:

1. Open the repository on GitHub.
2. Select the **Actions** tab.
3. Open the latest workflow run.
4. Review each job and its logs.

Any required secrets or cloud credentials should be configured through GitHub repository secrets, not committed to source control.

## 11. Security Notes

- Never commit private keys, passwords, access tokens, or cloud credentials.
- Keep `.pem` files and other sensitive deployment files out of Git.
- Do not commit local virtual environments or temporary archives.
- Restrict cloud security-group rules to the required ports and trusted sources.
- Avoid exposing development servers or debug mode publicly.

## 12. Troubleshooting

**Model file not found**

Check that `models/house_price_model.pkl` exists and that the model path in the application matches its location.

**Port already in use**

Stop the process using the port or configure a different port.

**API documentation does not open**

Check that the correct application is running and that the expected port is exposed.

**Kubernetes pod is not running**

Use `kubectl get pods` and `kubectl describe pod <POD_NAME>` to investigate the issue.

**AWS URL is unavailable**

Verify the EC2 instance state, current public IP, application health, Kubernetes service, and inbound security-group rules.

## Future Improvements

- Add model evaluation metrics and experiment tracking.
- Improve input validation and API documentation.
- Add monitoring and structured logging.
- Automate deployment through a verified CI/CD pipeline.
- Add model versioning and reproducible training.

## Author

**GitHub:** [tina5201](https://github.com/tina5201)

---

This project demonstrates an end-to-end machine-learning deployment workflow, from model training and application development to containerization, testing, and cloud deployment.
