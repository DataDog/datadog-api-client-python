# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsTestFileDownloadRequest(ModelNormal):
    validations = {
        "bucket_key": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "bucket_key": (str,),
        }

    attribute_map = {
        "bucket_key": "bucketKey",
    }

    def __init__(self_, bucket_key: str, **kwargs):
        """
        Request body for getting a presigned download URL for a test file.

        :param bucket_key: The bucket key referencing the file to download.
        :type bucket_key: str
        """
        super().__init__(kwargs)

        self_.bucket_key = bucket_key
