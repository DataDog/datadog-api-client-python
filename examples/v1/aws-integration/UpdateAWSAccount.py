"""
Update an AWS integration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v1.model.aws_account import AWSAccount

body = AWSAccount(
    account_id="123456789012",
    account_specific_namespace_rules=dict(
        auto_scaling=False,
    ),
    cspm_resource_collection_enabled=True,
    excluded_regions=[
        "us-east-1",
        "us-west-2",
    ],
    filter_tags=[
        "$KEY:$VALUE",
    ],
    host_tags=[
        "$KEY:$VALUE",
    ],
    metrics_collection_enabled=False,
    resource_collection_enabled=True,
    role_name="datadog-role",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.update_aws_account(account_id="123456789012", role_name="datadog-role", body=body)

    print(response)
