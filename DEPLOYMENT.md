# Loan App - Separated Frontend and Backend

## Architecture
- **Backend**: FastAPI (deploy to Railway)
- **Frontend**: Static HTML/CSS/JS files (deploy to Railway as separate service)

## Deployment to Railway

### Backend Deployment
1. Deploy the root directory to Railway (contains main.py, Procfile, etc.)
2. Railway will automatically detect it as a Python/FastAPI app
3. Note your backend URL: `https://your-backend-name.railway.app`

### Frontend Deployment
1. Create a NEW Railway service
2. Connect the SAME GitHub repository
3. Set the **Root Directory** to `frontend` in Railway settings
4. Railway will deploy the frontend as a static site
5. Note your frontend URL: `https://your-frontend-name.railway.app`

### Configuration Steps
1. **Deploy backend first** and get the backend URL
2. **Update frontend config**: Edit `frontend/config.js` with your backend URL:
   ```javascript
   API_BASE_URL: 'https://your-actual-backend.railway.app',
   ```
3. **Commit and push** the config change
4. **Deploy frontend** to Railway

## Railway Deployment Steps

### Step 1: Deploy Backend
- Railway service 1: Root directory (contains main.py)
- This becomes your API server

### Step 2: Deploy Frontend  
- Railway service 2: Root directory set to `frontend/`
- This becomes your web interface

### Step 3: Update Configuration
After both are deployed:
1. Copy your backend Railway URL
2. Update `frontend/config.js` with the backend URL
3. Commit and push to update frontend

## Local Development

### Backend:
```bash
uvicorn main:app --reload --port 8000
```

### Frontend:
The config.js automatically detects localhost and uses `http://localhost:8000`

## Railway Service Configuration

### Backend Service:
- **Root Directory**: `/` (default)
- **Build Command**: Auto-detected
- **Start Command**: From Procfile: `uvicorn main:app --host 0.0.0.0 --port $PORT --workers 1`

### Frontend Service:
- **Root Directory**: `frontend`
- **Build Command**: None needed
- **Start Command**: From Procfile: `python -m http.server $PORT`

## API Endpoints
- `GET /` - API health check
- `GET /health` - Detailed health check
- `GET /loans` - Get all loans
- `POST /loans` - Create new loan
- `DELETE /loans/{id}` - Delete loan
- `GET /payments` - Get all payments
- `POST /payments` - Create new payment
- `DELETE /payments/{id}` - Delete payment
