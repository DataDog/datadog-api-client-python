"""
Create a Terraform backend sync configuration returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.terraform_state_files_api import TerraformStateFilesApi
from datadog_api_client.v2.model.terraform_backend_create_attributes import TerraformBackendCreateAttributes
from datadog_api_client.v2.model.terraform_backend_create_data import TerraformBackendCreateData
from datadog_api_client.v2.model.terraform_backend_create_request import TerraformBackendCreateRequest
from datadog_api_client.v2.model.terraform_backend_kind import TerraformBackendKind
from datadog_api_client.v2.model.terraform_backend_type import TerraformBackendType

body = TerraformBackendCreateRequest(
    data=TerraformBackendCreateData(
        attributes=TerraformBackendCreateAttributes(
            account_id="123456789012",
            backend_type=TerraformBackendKind.TERRAFORM,
            bucket_names=[
                "terraform-state-bucket",
            ],
            region="us-east-1",
        ),
        type=TerraformBackendType.TERRAFORM_BACKENDS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TerraformStateFilesApi(api_client)
    response = api_instance.create_terraform_backend_sync_config(body=body)

    print(response)
