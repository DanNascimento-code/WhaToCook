from core.config import APP_NAME, APP_VERSION

def get_health_status():
    return {
        "app_name": APP_NAME,
        "app_version": APP_VERSION,
        "status": "healthy"
    }