"""
List Terraform backend sync configurations returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.terraform_state_files_api import TerraformStateFilesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TerraformStateFilesApi(api_client)
    response = api_instance.list_terraform_backend_sync_configs(
        account_id="123456789012",
    )

    print(response)
