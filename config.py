"""
Configuração central para todas as secrets e variáveis de ambiente do sistema PIX
"""
import os
import logging

logger = logging.getLogger(__name__)

class PixConfig:
    """Configuração centralizada para APIs PIX"""
    
    def __init__(self):
        # Real PIX Provider Configuration
        self.REAL_PIX_API_KEY = os.environ.get('REAL_PIX_API_KEY')
        self.REAL_PIX_PROVIDER_URL = os.environ.get('REAL_PIX_PROVIDER_URL') or os.environ.get('PIX_API_ENDPOINT')
        self.PIX_MERCHANT_ID = os.environ.get('PIX_MERCHANT_ID')
        
        # Medius Pag Configuration
        self.MEDIUS_PAG_SECRET_KEY = os.environ.get('MEDIUS_PAG_SECRET_KEY')
        self.MEDIUS_PAG_COMPANY_ID = os.environ.get('MEDIUS_PAG_COMPANY_ID', '30427d55-e437-4384-88de-6ba84fc74833')
        self.MEDIUS_PAG_API_DOCUMENTATION = os.environ.get('MEDIUS_PAG_API_DOCUMENTATION')
        
        # Other API Keys
        self.NEW_PIX_API_KEY = os.environ.get('NEW_PIX_API_KEY')
        self.FOR4PAYMENTS_SECRET_KEY = os.environ.get('FOR4PAYMENTS_SECRET_KEY')
        self.CASHTIME_SECRET_KEY = os.environ.get('CASHTIME_SECRET_KEY')
        self.CASHTIME_PUBLIC_KEY = os.environ.get('CASHTIME_PUBLIC_KEY')
        
        # Flask Configuration
        self.SESSION_SECRET = os.environ.get('SESSION_SECRET')
        
        # Database Configuration
        self.DATABASE_URL = os.environ.get('DATABASE_URL')
        
        # Pushcut Configuration
        self.PUSHCUT_WEBHOOK_URL = "https://api.pushcut.io/NiUWvkdg8_MMjxh6DOpez/notifications/Venda%20Pendente"
        
        # Log configuration status
        self._log_config_status()
    
    def _log_config_status(self):
        """Log the status of all configurations without exposing sensitive values"""
        config_status = {
            'REAL_PIX_API_KEY': '✓' if self.REAL_PIX_API_KEY else '✗',
            'REAL_PIX_PROVIDER_URL': '✓' if self.REAL_PIX_PROVIDER_URL else '✗',
            'PIX_MERCHANT_ID': '✓' if self.PIX_MERCHANT_ID else '✗',
            'MEDIUS_PAG_SECRET_KEY': '✓' if self.MEDIUS_PAG_SECRET_KEY else '✗',
            'MEDIUS_PAG_COMPANY_ID': '✓' if self.MEDIUS_PAG_COMPANY_ID else '✗',
            'MEDIUS_PAG_API_DOCUMENTATION': '✓' if self.MEDIUS_PAG_API_DOCUMENTATION else '✗',
            'NEW_PIX_API_KEY': '✓' if self.NEW_PIX_API_KEY else '✗',
            'FOR4PAYMENTS_SECRET_KEY': '✓' if self.FOR4PAYMENTS_SECRET_KEY else '✗',
            'CASHTIME_SECRET_KEY': '✓' if self.CASHTIME_SECRET_KEY else '✗',
            'CASHTIME_PUBLIC_KEY': '✓' if self.CASHTIME_PUBLIC_KEY else '✗',
            'SESSION_SECRET': '✓' if self.SESSION_SECRET else '✗',
            'DATABASE_URL': '✓' if self.DATABASE_URL else '✗',
            'PUSHCUT_WEBHOOK_URL': '✓' if self.PUSHCUT_WEBHOOK_URL else '✗',
        }
        
        logger.info(f"[CONFIG] Status das configurações: {config_status}")
        
        # Check for critical missing configurations
        missing_critical = []
        if not self.REAL_PIX_API_KEY:
            missing_critical.append('REAL_PIX_API_KEY')
        if not self.REAL_PIX_PROVIDER_URL:
            missing_critical.append('REAL_PIX_PROVIDER_URL')
        if not self.PIX_MERCHANT_ID:
            missing_critical.append('PIX_MERCHANT_ID')
            
        if missing_critical:
            logger.warning(f"[CONFIG] Secrets críticas ausentes: {missing_critical}")
        else:
            logger.info("[CONFIG] Todas as secrets críticas do PIX estão configuradas")
    
    def get_real_pix_config(self):
        """Retorna configuração para Real PIX Provider"""
        return {
            'api_key': self.REAL_PIX_API_KEY,
            'provider_url': self.REAL_PIX_PROVIDER_URL,
            'merchant_id': self.PIX_MERCHANT_ID
        }
    
    def get_medius_pag_config(self):
        """Retorna configuração para Medius Pag API"""
        return {
            'secret_key': self.MEDIUS_PAG_SECRET_KEY,
            'company_id': self.MEDIUS_PAG_COMPANY_ID,
            'api_documentation': self.MEDIUS_PAG_API_DOCUMENTATION
        }
    
    def validate_pix_config(self):
        """Valida se todas as configurações necessárias estão presentes"""
        errors = []
        
        if not self.REAL_PIX_API_KEY:
            errors.append("REAL_PIX_API_KEY é obrigatória")
        
        if not self.REAL_PIX_PROVIDER_URL:
            errors.append("REAL_PIX_PROVIDER_URL é obrigatória")
        
        if not self.PIX_MERCHANT_ID:
            errors.append("PIX_MERCHANT_ID é obrigatório")
        
        if errors:
            raise ValueError(f"Configurações PIX ausentes: {', '.join(errors)}")
        
        return True

# Instância global da configuração
pix_config = PixConfig()

def get_pix_config():
    """Factory function para obter a configuração PIX"""
    return pix_config