# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsTestFileCompleteMultipartUploadPart(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "e_tag": (str,),
            "part_number": (int,),
        }

    attribute_map = {
        "e_tag": "ETag",
        "part_number": "PartNumber",
    }

    def __init__(self_, e_tag: str, part_number: int, **kwargs):
        """
        A completed part of a multipart upload.

        :param e_tag: The ETag returned by the storage provider after uploading the part.
        :type e_tag: str

        :param part_number: The 1-indexed part number for the multipart upload.
        :type part_number: int
        """
        super().__init__(kwargs)

        self_.e_tag = e_tag
        self_.part_number = part_number
