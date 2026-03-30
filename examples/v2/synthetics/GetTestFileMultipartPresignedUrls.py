"""
Get presigned URLs for uploading a test file returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.synthetics_api import SyntheticsApi
from datadog_api_client.v2.model.synthetics_test_file_multipart_presigned_urls_part import (
    SyntheticsTestFileMultipartPresignedUrlsPart,
)
from datadog_api_client.v2.model.synthetics_test_file_multipart_presigned_urls_request import (
    SyntheticsTestFileMultipartPresignedUrlsRequest,
)
from datadog_api_client.v2.model.synthetics_test_file_multipart_presigned_urls_request_bucket_key_prefix import (
    SyntheticsTestFileMultipartPresignedUrlsRequestBucketKeyPrefix,
)

body = SyntheticsTestFileMultipartPresignedUrlsRequest(
    bucket_key_prefix=SyntheticsTestFileMultipartPresignedUrlsRequestBucketKeyPrefix.API_UPLOAD_FILE,
    parts=[
        SyntheticsTestFileMultipartPresignedUrlsPart(
            md5="1B2M2Y8AsgTpgAmY7PhCfg==",
            part_number=1,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.get_test_file_multipart_presigned_urls(public_id="abc-def-123", body=body)

    print(response)
