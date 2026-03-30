# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_test_file_multipart_presigned_urls_request_bucket_key_prefix import (
        SyntheticsTestFileMultipartPresignedUrlsRequestBucketKeyPrefix,
    )
    from datadog_api_client.v2.model.synthetics_test_file_multipart_presigned_urls_part import (
        SyntheticsTestFileMultipartPresignedUrlsPart,
    )


class SyntheticsTestFileMultipartPresignedUrlsRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_file_multipart_presigned_urls_request_bucket_key_prefix import (
            SyntheticsTestFileMultipartPresignedUrlsRequestBucketKeyPrefix,
        )
        from datadog_api_client.v2.model.synthetics_test_file_multipart_presigned_urls_part import (
            SyntheticsTestFileMultipartPresignedUrlsPart,
        )

        return {
            "bucket_key_prefix": (SyntheticsTestFileMultipartPresignedUrlsRequestBucketKeyPrefix,),
            "parts": ([SyntheticsTestFileMultipartPresignedUrlsPart],),
        }

    attribute_map = {
        "bucket_key_prefix": "bucketKeyPrefix",
        "parts": "parts",
    }

    def __init__(
        self_,
        bucket_key_prefix: SyntheticsTestFileMultipartPresignedUrlsRequestBucketKeyPrefix,
        parts: List[SyntheticsTestFileMultipartPresignedUrlsPart],
        **kwargs,
    ):
        """
        Request body for getting presigned URLs for a multipart file upload.

        :param bucket_key_prefix: The bucket key prefix indicating the type of file upload.
        :type bucket_key_prefix: SyntheticsTestFileMultipartPresignedUrlsRequestBucketKeyPrefix

        :param parts: Array of part descriptors for the multipart upload.
        :type parts: [SyntheticsTestFileMultipartPresignedUrlsPart]
        """
        super().__init__(kwargs)

        self_.bucket_key_prefix = bucket_key_prefix
        self_.parts = parts
