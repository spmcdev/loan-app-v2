# Loan App - Separated Frontend and Backend

## Architecture
- **Backend**: FastAPI (deploy to Railway)
- **Frontend**: Static HTML/CSS/JS files (deploy to static hosting)

## Backend Deployment (Railway)
The backend API is in the root directory and will be deployed to Railway.

**Backend URL**: Your Railway app URL (e.g., `https://your-backend.railway.app`)

## Frontend Deployment Options

### Option 1: Vercel (Recommended)
1. Create a new repository for just the frontend
2. Copy the `frontend/` folder contents to the new repo
3. Connect to Vercel
4. Update `config.js` with your Railway backend URL

### Option 2: Netlify
1. Drag and drop the `frontend/` folder to Netlify
2. Update `config.js` with your Railway backend URL

### Option 3: GitHub Pages
1. Create a new GitHub repository
2. Copy `frontend/` contents to the repo
3. Enable GitHub Pages in repository settings
4. Update `config.js` with your Railway backend URL

### Option 4: Railway Static Site
1. Create a new Railway service
2. Deploy the `frontend/` folder as a static site
3. Update `config.js` with your backend Railway URL

## Configuration

1. Deploy the backend first and get the URL
2. Update `frontend/config.js` with your backend URL:
   ```javascript
   const CONFIG = {
       API_BASE_URL: 'https://your-actual-backend.railway.app',
   };
   ```
3. Deploy the frontend to your chosen static hosting service

## Local Development

### Backend:
```bash
uvicorn main:app --reload --port 8000
```

### Frontend:
Update `config.js` to use localhost:
```javascript
API_BASE_URL: 'http://localhost:8000',
```
Then serve the frontend folder with any static server or open HTML files directly.

## API Endpoints
- `GET /` - API health check
- `GET /health` - Detailed health check
- `GET /loans` - Get all loans
- `POST /loans` - Create new loan
- `DELETE /loans/{id}` - Delete loan
- `GET /payments` - Get all payments
- `POST /payments` - Create new payment
- `DELETE /payments/{id}` - Delete payment
