# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_test_file_multipart_presigned_urls_params import (
        SyntheticsTestFileMultipartPresignedUrlsParams,
    )


class SyntheticsTestFileMultipartPresignedUrlsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_file_multipart_presigned_urls_params import (
            SyntheticsTestFileMultipartPresignedUrlsParams,
        )

        return {
            "bucket_key": (str,),
            "multipart_presigned_urls_params": (SyntheticsTestFileMultipartPresignedUrlsParams,),
        }

    attribute_map = {
        "bucket_key": "bucketKey",
        "multipart_presigned_urls_params": "multipart_presigned_urls_params",
    }

    def __init__(
        self_,
        bucket_key: Union[str, UnsetType] = unset,
        multipart_presigned_urls_params: Union[SyntheticsTestFileMultipartPresignedUrlsParams, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing presigned URLs for multipart file upload and the bucket key.

        :param bucket_key: The bucket key that references the uploaded file after completion.
        :type bucket_key: str, optional

        :param multipart_presigned_urls_params: Presigned URL parameters returned for a multipart upload.
        :type multipart_presigned_urls_params: SyntheticsTestFileMultipartPresignedUrlsParams, optional
        """
        if bucket_key is not unset:
            kwargs["bucket_key"] = bucket_key
        if multipart_presigned_urls_params is not unset:
            kwargs["multipart_presigned_urls_params"] = multipart_presigned_urls_params
        super().__init__(kwargs)
