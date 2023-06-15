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
    from datadog_api_client.v2.model.role import Role
    from datadog_api_client.v2.model.response_meta_attributes import ResponseMetaAttributes


@dataclass
class RolesResponseJSON:
    id: str
    created_at: Union[datetime, UnsetType] = unset
    modified_at: Union[datetime, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    user_count: Union[int, UnsetType] = unset
    permissions: Union[List[str], UnsetType] = unset


class RolesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.role import Role
        from datadog_api_client.v2.model.response_meta_attributes import ResponseMetaAttributes

        return {
            "data": ([Role],),
            "meta": (ResponseMetaAttributes,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }
    json_api_model = RolesResponseJSON

    def __init__(
        self_,
        data: Union[List[Role], UnsetType] = unset,
        meta: Union[ResponseMetaAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing information about multiple roles.

        :param data: Array of returned roles.
        :type data: [Role], optional

        :param meta: Object describing meta attributes of response.
        :type meta: ResponseMetaAttributes, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
