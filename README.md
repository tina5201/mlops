# MLOps House Price Prediction

An educational MLOps project demonstrating house-price prediction through model training, API development, automated testing, containerization, Kubernetes deployment, and CI/CD.

## Project Components

- **Machine Learning:** Model training using `model/train.py`
- **Flask Web App:** Browser-based house-price prediction form
- **FastAPI:** REST API with prediction and health-check endpoints
- **Testing:** Pytest
- **Containerization:** Docker
- **Orchestration:** Kubernetes manifests
- **Cloud Deployment:** AWS EC2 with k3s
- **CI/CD:** GitHub Actions workflow

## Project Structure

```text
.
├── app.py                  # Flask web application
├── app/
│   ├── main.py             # FastAPI application
│   └── schemas.py          # API schemas
├── model/
│   └── train.py            # Model training
├── models/
│   └── house_price_model.pkl
├── templates/
│   └── index.html          # Flask web interface
├── static/
│   └── style.css           # Web styling
├── tests/
│   └── test_api.py         # API tests
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── .github/workflows/
│   └── ci-cd.yml
├── Dockerfile
├── environment.yml
└── requirements.txt
