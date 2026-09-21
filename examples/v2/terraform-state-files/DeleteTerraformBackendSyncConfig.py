"""
Delete a Terraform backend sync configuration returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.terraform_state_files_api import TerraformStateFilesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TerraformStateFilesApi(api_client)
    api_instance.delete_terraform_backend_sync_config(
        id="9007199254740993",
    )
