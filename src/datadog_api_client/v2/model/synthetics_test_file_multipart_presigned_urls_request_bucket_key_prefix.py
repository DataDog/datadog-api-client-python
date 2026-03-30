# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsTestFileMultipartPresignedUrlsRequestBucketKeyPrefix(ModelSimple):
    """
    The bucket key prefix indicating the type of file upload.

    :param value: Must be one of ["api-upload-file", "browser-upload-file-step"].
    :type value: str
    """

    allowed_values = {
        "api-upload-file",
        "browser-upload-file-step",
    }
    API_UPLOAD_FILE: ClassVar["SyntheticsTestFileMultipartPresignedUrlsRequestBucketKeyPrefix"]
    BROWSER_UPLOAD_FILE_STEP: ClassVar["SyntheticsTestFileMultipartPresignedUrlsRequestBucketKeyPrefix"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsTestFileMultipartPresignedUrlsRequestBucketKeyPrefix.API_UPLOAD_FILE = (
    SyntheticsTestFileMultipartPresignedUrlsRequestBucketKeyPrefix("api-upload-file")
)
SyntheticsTestFileMultipartPresignedUrlsRequestBucketKeyPrefix.BROWSER_UPLOAD_FILE_STEP = (
    SyntheticsTestFileMultipartPresignedUrlsRequestBucketKeyPrefix("browser-upload-file-step")
)
