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


if TYPE_CHECKING:
    from datadog_api_client.v2.model.authn_mapping_update_data import AuthNMappingUpdateData


@dataclass
class AuthNMappingUpdateRequestJSON:
    id: str
    attribute_key: Union[str, UnsetType] = unset
    attribute_value: Union[str, UnsetType] = unset
    role: Union[str, UnsetType] = unset


class AuthNMappingUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.authn_mapping_update_data import AuthNMappingUpdateData

        return {
            "data": (AuthNMappingUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = AuthNMappingUpdateRequestJSON

    def __init__(self_, data: AuthNMappingUpdateData, **kwargs):
        """
        Request to update an AuthN Mapping.

        :param data: Data for updating an AuthN Mapping.
        :type data: AuthNMappingUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
