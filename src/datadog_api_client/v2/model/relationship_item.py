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


class RelationshipItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: Union[str, UnsetType] = unset, type: Union[str, UnsetType] = unset, **kwargs):
        """
        Relationship entry.

        :param id: Associated data id.
        :type id: str, optional

        :param type: Relationship type.
        :type type: str, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
