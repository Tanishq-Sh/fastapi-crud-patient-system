# 🏥 Insurance Premium Prediction System

A machine learning-based API that predicts insurance premium categories based on user health and demographic information. Built with **FastAPI** backend and **Streamlit** frontend.

---

## 📋 Features

- **ML-Powered Predictions**: Predicts insurance premium categories using a pre-trained scikit-learn model
- **Automatic Data Validation**: Pydantic-based input validation with computed fields
- **Health Checks**: API health endpoint with model version tracking
- **Interactive UI**: Streamlit frontend for easy user interaction
- **Docker Support**: Ready to deploy with included Dockerfile
- **Data Processing**: Automatic BMI calculation, lifestyle risk assessment, and age grouping

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- pip or conda

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Tanishq-Sh/fastapi-crud-patient-system.git
   cd fastapi-crud-patient-system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the API server**
   ```bash
   uvicorn app:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`

4. **In a new terminal, run the Streamlit frontend**
   ```bash
   streamlit run frontend.py
   ```
   The UI will open at `http://localhost:8501`

---

## 📊 API Endpoints

### 1. Home
- **Endpoint**: `GET /`
- **Response**: Welcome message

### 2. Health Check
- **Endpoint**: `GET /health`
- **Response**: 
  ```json
  {
    "status": "OK",
    "model_version": "1.0.0",
    "model_loaded": true
  }
  ```

### 3. Predict Premium
- **Endpoint**: `POST /predict`
- **Input**: User health and demographic data
- **Response**: Predicted premium category with probabilities

**Example Request**:
```json
{
  "age": 30,
  "weight": 65.0,
  "height": 1.75,
  "income_lpa": 5.5,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

---

## 🛠️ Project Structure

```
├── app.py                    # FastAPI application
├── frontend.py              # Streamlit UI
├── requirements.txt         # Dependencies
├── Dockerfile              # Docker configuration
├── environment.yml         # Conda environment
├── model/
│   ├── model.pkl          # Pre-trained ML model
│   └── predict.py         # Prediction logic
├── schema/
│   ├── user_input.py      # Input validation schema
│   └── prediction_response.py
├── config/
│   └── city_tier.py       # City tier configuration
└── pydantic/              # Pydantic examples and utilities
```

---

## 📥 Input Parameters

| Parameter | Type | Range | Description |
|-----------|------|-------|-------------|
| `age` | int | 1-119 | User's age in years |
| `weight` | float | > 0 | Weight in kilograms |
| `height` | float | 0.5-2.5 | Height in meters |
| `income_lpa` | float | > 0 | Annual salary in LPA (Lakhs Per Annum) |
| `smoker` | bool | true/false | Smoking status |
| `city` | string | - | City name (auto-normalized) |
| `occupation` | string | See below | Occupation type |

**Occupation Options**:
- `retired`
- `freelancer`
- `student`
- `government_job`
- `business_owner`
- `unemployed`
- `private_job`

---

## 🧮 Computed Fields

The system automatically calculates:

- **BMI**: Body Mass Index from height and weight
- **Age Group**: Categorized as young, adult, middle_aged, or senior
- **Lifestyle Risk**: Assessed as low, medium, or high based on smoking status and BMI

---

## 🐳 Docker Deployment

Build and run with Docker:

```bash
# Build image
docker build -t insurance-premium-predictor .

# Run container
docker run -p 8000:8000 insurance-premium-predictor
```

---

## 📦 Dependencies

- **fastapi**: Web framework
- **uvicorn**: ASGI server
- **pydantic**: Data validation
- **scikit-learn**: ML model
- **pandas**: Data processing
- **streamlit**: Frontend framework
- **requests**: HTTP client

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👤 Author

Tanishq Sharma - [GitHub Profile](https://github.com/Tanishq-Sh)

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues and pull requests.