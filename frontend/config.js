// Configuration for the frontend
const CONFIG = {
    // Update this URL to your Railway backend URL
    API_BASE_URL: 'https://your-backend-app.railway.app',
    
    // For local development, uncomment this line:
    // API_BASE_URL: 'http://localhost:8000',
    
    // For production with same domain, use:
    // API_BASE_URL: window.location.origin,
};

// Export for use in HTML files
window.CONFIG = CONFIG;
