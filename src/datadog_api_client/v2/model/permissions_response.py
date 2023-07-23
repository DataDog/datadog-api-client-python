# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.permission import Permission


@dataclass
class PermissionsResponseJSON:
    id: str
    created: Union[datetime, UnsetType] = unset
    description: Union[str, UnsetType] = unset
    display_name: Union[str, UnsetType] = unset
    display_type: Union[str, UnsetType] = unset
    group_name: Union[str, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    restricted: Union[bool, UnsetType] = unset


class PermissionsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.permission import Permission

        return {
            "data": ([Permission],),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = PermissionsResponseJSON

    def __init__(self_, data: Union[List[Permission], UnsetType] = unset, **kwargs):
        """
        Payload with API-returned permissions.

        :param data: Array of permissions.
        :type data: [Permission], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
