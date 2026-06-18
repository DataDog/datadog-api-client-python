"""
Create Vercel access token returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.vercel_api import VercelApi
from datadog_api_client.v2.model.vercel_token_create_request import VercelTokenCreateRequest

body = VercelTokenCreateRequest(
    auth_grant_code="code",
    vercel_configuration_id="icfg_abc123",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = VercelApi(api_client)
    api_instance.create_vercel_token(body=body)
