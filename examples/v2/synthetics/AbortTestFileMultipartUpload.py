"""
Abort a multipart upload of a test file returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.synthetics_api import SyntheticsApi
from datadog_api_client.v2.model.synthetics_test_file_abort_multipart_upload_request import (
    SyntheticsTestFileAbortMultipartUploadRequest,
)

body = SyntheticsTestFileAbortMultipartUploadRequest(
    key="org-123/api-upload-file/abc-def-123/2024-01-01T00:00:00_uuid.json",
    upload_id="upload-id-abc123",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    api_instance.abort_test_file_multipart_upload(public_id="abc-def-123", body=body)
