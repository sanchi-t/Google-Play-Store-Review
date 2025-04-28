# Play Store Sentiment Analyzer

This project is a full-stack application that fetches reviews from the Google Play Store and performs sentiment analysis on them. It consists of a **backend** (FastAPI) and a **frontend** (Next.js).

## Prerequisites

Ensure you have the following installed on your system:
- **Node.js** (v18 or higher)
- **Python** (v3.10 or higher)
- **pip** (Python package manager)
- **virtualenv** (optional but recommended for Python dependencies)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/sanchi-t/playstore-sentiment.git
cd playstore-sentiment
```

### 1. Backend Setup
#### 1. Navigate to the backend directory:
```bash
cd backend
```

#### 2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install the required Python dependencies:
```bash
pip install -r requirements.txt
```


#### 4. Start the backend:
```bash
fastapi run
```


### 2. Frontend Setup
#### 1. Navigate to the backend directory:
```bash
cd ../client
```

#### 2. Navigate to the client directory:
```bash
npm install
```

#### 3. Start the frontend development server:

```bash
npx next dev
```


#### 4. View webpage at `localhost:3000`

### Limitations:

- Language Limitation: The current approach is limited to fetching data for a single language at a time.

- Emojis Handling: The method does not account for emojis in reviews.



### Working of project:



https://github.com/user-attachments/assets/d0d76571-75cd-4a7e-a1e6-9803a293c6e7

