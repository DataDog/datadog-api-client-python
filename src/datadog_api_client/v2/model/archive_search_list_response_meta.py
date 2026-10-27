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


class ArchiveSearchListResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "truncated": (bool,),
        }

    attribute_map = {
        "truncated": "truncated",
    }

    def __init__(self_, truncated: Union[bool, UnsetType] = unset, **kwargs):
        """
        Metadata of the Archive Searches response.

        :param truncated: Whether more Archive Searches exist beyond the ones returned.
        :type truncated: bool, optional
        """
        if truncated is not unset:
            kwargs["truncated"] = truncated
        super().__init__(kwargs)
