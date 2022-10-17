# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.security_filter_exclusion_filter_response import SecurityFilterExclusionFilterResponse
from datadog_api_client.v2.model.security_filter_filtered_data_type import SecurityFilterFilteredDataType
from datadog_api_client.v2.model.security_filter_attributes import SecurityFilterAttributes
from datadog_api_client.v2.model.security_filter_exclusion_filter_response import SecurityFilterExclusionFilterResponse
from datadog_api_client.v2.model.security_filter_filtered_data_type import SecurityFilterFilteredDataType

if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_filter_type import SecurityFilterType


@dataclass
class SecurityFilterJSON:
    id: str
    exclusion_filters: Union[List[SecurityFilterExclusionFilterResponse], UnsetType] = unset
    filtered_data_type: Union[SecurityFilterFilteredDataType, UnsetType] = unset
    is_builtin: Union[bool, UnsetType] = unset
    is_enabled: Union[bool, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    query: Union[str, UnsetType] = unset
    version: Union[int, UnsetType] = unset


class SecurityFilter(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_filter_type import SecurityFilterType

        return {
            "attributes": (SecurityFilterAttributes,),
            "id": (str,),
            "type": (SecurityFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    json_api_model = SecurityFilterJSON

    def __init__(
        self_,
        attributes: Union[SecurityFilterAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[SecurityFilterType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The security filter's properties.

        :param attributes: The object describing a security filter.
        :type attributes: SecurityFilterAttributes, optional

        :param id: The ID of the security filter.
        :type id: str, optional

        :param type: The type of the resource. The value should always be ``security_filters``.
        :type type: SecurityFilterType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
