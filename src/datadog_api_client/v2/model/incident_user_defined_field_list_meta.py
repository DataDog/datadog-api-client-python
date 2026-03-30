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


class IncidentUserDefinedFieldListMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "offset": (int,),
            "size": (int,),
        }

    attribute_map = {
        "offset": "offset",
        "size": "size",
    }

    def __init__(self_, offset: Union[int, UnsetType] = unset, size: Union[int, UnsetType] = unset, **kwargs):
        """
        Pagination metadata for the user-defined field list response.

        :param offset: The offset of the current page.
        :type offset: int, optional

        :param size: The total number of items in the current page.
        :type size: int, optional
        """
        if offset is not unset:
            kwargs["offset"] = offset
        if size is not unset:
            kwargs["size"] = size
        super().__init__(kwargs)
