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
    from datadog_api_client.v2.model.authn_mapping_create_data import AuthNMappingCreateData


@dataclass
class AuthNMappingCreateRequestJSON:
    attribute_key: Union[str, UnsetType] = unset
    attribute_value: Union[str, UnsetType] = unset
    role: Union[str, UnsetType] = unset


class AuthNMappingCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.authn_mapping_create_data import AuthNMappingCreateData

        return {
            "data": (AuthNMappingCreateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = AuthNMappingCreateRequestJSON

    def __init__(self_, data: AuthNMappingCreateData, **kwargs):
        """
        Request for creating an AuthN Mapping.

        :param data: Data for creating an AuthN Mapping.
        :type data: AuthNMappingCreateData
        """
        super().__init__(kwargs)

        self_.data = data
