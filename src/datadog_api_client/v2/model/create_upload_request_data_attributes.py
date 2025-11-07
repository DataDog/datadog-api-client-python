# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CreateUploadRequestDataAttributes(ModelNormal):
    validations = {
        "part_count": {
            "inclusive_maximum": 20,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "headers": ([str],),
            "part_count": (int,),
            "part_size": (int,),
            "table_name": (str,),
        }

    attribute_map = {
        "headers": "headers",
        "part_count": "part_count",
        "part_size": "part_size",
        "table_name": "table_name",
    }

    def __init__(self_, headers: List[str], part_count: int, part_size: int, table_name: str, **kwargs):
        """
        Upload configuration specifying how data is uploaded by the user, and properties of the table to associate the upload with.

        :param headers: The CSV file headers that define the schema fields, provided in the same order as the columns in the uploaded file.
        :type headers: [str]

        :param part_count: Number of parts to split the file into for multipart upload.
        :type part_count: int

        :param part_size: The size of each part in the upload in bytes. All parts except the last one must be at least 5,000,000 bytes.
        :type part_size: int

        :param table_name: Name of the table to associate with this upload.
        :type table_name: str
        """
        super().__init__(kwargs)

        self_.headers = headers
        self_.part_count = part_count
        self_.part_size = part_size
        self_.table_name = table_name
