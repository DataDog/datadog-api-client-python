# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.rum_application_list_attributes import RUMApplicationListAttributes

if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_application_list_type import RUMApplicationListType


@dataclass
class RUMApplicationListJSON:
    type: str
    application_id: Union[str, UnsetType] = unset
    created_at: Union[int, UnsetType] = unset
    created_by_handle: Union[str, UnsetType] = unset
    hash: Union[str, UnsetType] = unset
    is_active: Union[bool, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    org_id: Union[int, UnsetType] = unset
    updated_at: Union[int, UnsetType] = unset
    updated_by_handle: Union[str, UnsetType] = unset


class RUMApplicationList(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_application_list_type import RUMApplicationListType

        return {
            "attributes": (RUMApplicationListAttributes,),
            "type": (RUMApplicationListType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }
    json_api_model = RUMApplicationListJSON

    def __init__(self_, attributes: RUMApplicationListAttributes, type: RUMApplicationListType, **kwargs):
        """
        RUM application list.

        :param attributes: RUM application list attributes.
        :type attributes: RUMApplicationListAttributes

        :param type: RUM application list type.
        :type type: RUMApplicationListType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
