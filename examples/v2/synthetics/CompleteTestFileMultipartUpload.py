"""
Complete a multipart upload of a test file returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.synthetics_api import SyntheticsApi
from datadog_api_client.v2.model.synthetics_test_file_complete_multipart_upload_part import (
    SyntheticsTestFileCompleteMultipartUploadPart,
)
from datadog_api_client.v2.model.synthetics_test_file_complete_multipart_upload_request import (
    SyntheticsTestFileCompleteMultipartUploadRequest,
)

body = SyntheticsTestFileCompleteMultipartUploadRequest(
    key="org-123/api-upload-file/abc-def-123/2024-01-01T00:00:00_uuid.json",
    parts=[
        SyntheticsTestFileCompleteMultipartUploadPart(
            e_tag='"d41d8cd98f00b204e9800998ecf8427e"',
            part_number=1,
        ),
    ],
    upload_id="upload-id-abc123",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    api_instance.complete_test_file_multipart_upload(public_id="abc-def-123", body=body)
