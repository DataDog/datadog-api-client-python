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


class AssetVersion(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "first": (str,),
            "last": (str,),
        }

    attribute_map = {
        "first": "first",
        "last": "last",
    }

    def __init__(self_, first: Union[str, UnsetType] = unset, last: Union[str, UnsetType] = unset, **kwargs):
        """
        Asset version.

        :param first: Asset first version.
        :type first: str, optional

        :param last: Asset last version.
        :type last: str, optional
        """
        if first is not unset:
            kwargs["first"] = first
        if last is not unset:
            kwargs["last"] = last
        super().__init__(kwargs)
