"""
Trigger tests from CI/CD pipelines returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_basic_auth_web import SyntheticsBasicAuthWeb
from datadog_api_client.v1.model.synthetics_basic_auth_web_type import SyntheticsBasicAuthWebType
from datadog_api_client.v1.model.synthetics_ci_batch_metadata import SyntheticsCIBatchMetadata
from datadog_api_client.v1.model.synthetics_ci_batch_metadata_ci import SyntheticsCIBatchMetadataCI
from datadog_api_client.v1.model.synthetics_ci_batch_metadata_git import SyntheticsCIBatchMetadataGit
from datadog_api_client.v1.model.synthetics_ci_batch_metadata_pipeline import SyntheticsCIBatchMetadataPipeline
from datadog_api_client.v1.model.synthetics_ci_batch_metadata_provider import SyntheticsCIBatchMetadataProvider
from datadog_api_client.v1.model.synthetics_ci_test import SyntheticsCITest
from datadog_api_client.v1.model.synthetics_ci_test_body import SyntheticsCITestBody
from datadog_api_client.v1.model.synthetics_device_id import SyntheticsDeviceID
from datadog_api_client.v1.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry

body = SyntheticsCITestBody(
    tests=[
        SyntheticsCITest(
            basic_auth=SyntheticsBasicAuthWeb(
                password="PaSSw0RD!",
                type=SyntheticsBasicAuthWebType.WEB,
                username="my_username",
            ),
            device_ids=[
                SyntheticsDeviceID.LAPTOP_LARGE,
            ],
            locations=[
                "aws:eu-west-3",
            ],
            metadata=SyntheticsCIBatchMetadata(
                ci=SyntheticsCIBatchMetadataCI(
                    pipeline=SyntheticsCIBatchMetadataPipeline(),
                    provider=SyntheticsCIBatchMetadataProvider(),
                ),
                git=SyntheticsCIBatchMetadataGit(),
            ),
            public_id="aaa-aaa-aaa",
            retry=SyntheticsTestOptionsRetry(),
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.trigger_ci_tests(body=body)

    print(response)
