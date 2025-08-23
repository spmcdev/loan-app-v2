// Configuration for the frontend
const CONFIG = {
    // Railway Backend URL - Update this with your actual backend Railway URL
    API_BASE_URL: 'https://loan-app-v2-production.up.railway.app/',
    
    // For local development, uncomment this line:
    // API_BASE_URL: 'http://localhost:8000',
    
    // Auto-detect in Railway if both frontend and backend are on Railway
    // and you want to use relative URLs (not recommended for separate services)
};

// Auto-detect if running locally
if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    CONFIG.API_BASE_URL = 'http://localhost:8000';
}

// Export for use in HTML files
window.CONFIG = CONFIG;
