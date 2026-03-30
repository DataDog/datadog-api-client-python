"""
Get a presigned URL for downloading a test file returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.synthetics_api import SyntheticsApi
from datadog_api_client.v2.model.synthetics_test_file_download_request import SyntheticsTestFileDownloadRequest

body = SyntheticsTestFileDownloadRequest(
    bucket_key="api-upload-file/abc-def-123/2024-01-01T00:00:00_uuid.json",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.get_test_file_download_url(public_id="abc-def-123", body=body)

    print(response)
