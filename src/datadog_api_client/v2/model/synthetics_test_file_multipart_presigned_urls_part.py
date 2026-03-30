# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsTestFileMultipartPresignedUrlsPart(ModelNormal):
    validations = {
        "md5": {
            "max_length": 24,
            "min_length": 22,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "md5": (str,),
            "part_number": (int,),
        }

    attribute_map = {
        "md5": "md5",
        "part_number": "partNumber",
    }

    def __init__(self_, md5: str, part_number: int, **kwargs):
        """
        A part descriptor for initiating a multipart upload.

        :param md5: Base64-encoded MD5 digest of the part content.
        :type md5: str

        :param part_number: The 1-indexed part number for the multipart upload.
        :type part_number: int
        """
        super().__init__(kwargs)

        self_.md5 = md5
        self_.part_number = part_number
