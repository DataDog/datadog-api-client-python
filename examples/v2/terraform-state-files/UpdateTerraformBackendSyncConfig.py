"""
Update a Terraform backend sync configuration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.terraform_state_files_api import TerraformStateFilesApi
from datadog_api_client.v2.model.terraform_backend_type import TerraformBackendType
from datadog_api_client.v2.model.terraform_backend_update_attributes import TerraformBackendUpdateAttributes
from datadog_api_client.v2.model.terraform_backend_update_data import TerraformBackendUpdateData
from datadog_api_client.v2.model.terraform_backend_update_request import TerraformBackendUpdateRequest

body = TerraformBackendUpdateRequest(
    data=TerraformBackendUpdateData(
        attributes=TerraformBackendUpdateAttributes(
            bucket_names=[
                "terraform-state-bucket",
            ],
        ),
        id="9007199254740993",
        type=TerraformBackendType.TERRAFORM_BACKENDS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TerraformStateFilesApi(api_client)
    response = api_instance.update_terraform_backend_sync_config(id="9007199254740993", body=body)

    print(response)
