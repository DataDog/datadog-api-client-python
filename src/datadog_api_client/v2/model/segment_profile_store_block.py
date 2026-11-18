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


class SegmentProfileStoreBlock(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "query": (str,),
        }

    attribute_map = {
        "name": "name",
        "query": "query",
    }

    def __init__(self_, query: str, name: Union[str, UnsetType] = unset, **kwargs):
        """
        Selects users or accounts by their profile attributes.

        :param name: Name of the block, used in ``combination``.
        :type name: str, optional

        :param query: Profile attribute query.
        :type query: str
        """
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.query = query
