# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SyntheticsTestRequestBodyFile(ModelNormal):
    validations = {
        "content": {
            "max_length": 3145728,
        },
        "name": {
            "max_length": 1500,
        },
        "original_file_name": {
            "max_length": 1500,
        },
        "size": {
            "inclusive_maximum": 3145728,
            "inclusive_minimum": 1,
        },
        "type": {
            "max_length": 1500,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "bucket_key": (str,),
            "content": (str,),
            "name": (str,),
            "original_file_name": (str,),
            "size": (int,),
            "type": (str,),
        }

    attribute_map = {
        "bucket_key": "bucketKey",
        "content": "content",
        "name": "name",
        "original_file_name": "originalFileName",
        "size": "size",
        "type": "type",
    }

    def __init__(
        self_,
        bucket_key: Union[str, UnsetType] = unset,
        content: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        original_file_name: Union[str, UnsetType] = unset,
        size: Union[int, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object describing a file to be used as part of the request in the test.

        :param bucket_key: Bucket key of the file.
        :type bucket_key: str, optional

        :param content: Content of the file.
        :type content: str, optional

        :param name: Name of the file.
        :type name: str, optional

        :param original_file_name: Original name of the file.
        :type original_file_name: str, optional

        :param size: Size of the file.
        :type size: int, optional

        :param type: Type of the file.
        :type type: str, optional
        """
        if bucket_key is not unset:
            kwargs["bucket_key"] = bucket_key
        if content is not unset:
            kwargs["content"] = content
        if name is not unset:
            kwargs["name"] = name
        if original_file_name is not unset:
            kwargs["original_file_name"] = original_file_name
        if size is not unset:
            kwargs["size"] = size
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
