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


class SyntheticsTestResultFileRef(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "bucket_key": (str,),
            "encoding": (str,),
            "name": (str,),
            "size": (int,),
            "type": (str,),
        }

    attribute_map = {
        "bucket_key": "bucket_key",
        "encoding": "encoding",
        "name": "name",
        "size": "size",
        "type": "type",
    }

    def __init__(
        self_,
        bucket_key: Union[str, UnsetType] = unset,
        encoding: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        size: Union[int, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Reference to a file attached to a Synthetic test request.

        :param bucket_key: Storage bucket key where the file is stored.
        :type bucket_key: str, optional

        :param encoding: Encoding of the file contents.
        :type encoding: str, optional

        :param name: File name.
        :type name: str, optional

        :param size: File size in bytes.
        :type size: int, optional

        :param type: File MIME type.
        :type type: str, optional
        """
        if bucket_key is not unset:
            kwargs["bucket_key"] = bucket_key
        if encoding is not unset:
            kwargs["encoding"] = encoding
        if name is not unset:
            kwargs["name"] = name
        if size is not unset:
            kwargs["size"] = size
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
