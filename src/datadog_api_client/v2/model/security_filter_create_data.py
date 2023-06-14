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


from datadog_api_client.v2.model.security_filter_exclusion_filter import SecurityFilterExclusionFilter
from datadog_api_client.v2.model.security_filter_filtered_data_type import SecurityFilterFilteredDataType
from datadog_api_client.v2.model.security_filter_create_attributes import SecurityFilterCreateAttributes
from datadog_api_client.v2.model.security_filter_exclusion_filter import SecurityFilterExclusionFilter
from datadog_api_client.v2.model.security_filter_filtered_data_type import SecurityFilterFilteredDataType

if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_filter_type import SecurityFilterType


@dataclass
class SecurityFilterCreateDataJSON:
    exclusion_filters: Union[List[SecurityFilterExclusionFilter], UnsetType] = unset
    filtered_data_type: Union[SecurityFilterFilteredDataType, UnsetType] = unset
    is_enabled: Union[bool, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    query: Union[str, UnsetType] = unset


class SecurityFilterCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_filter_type import SecurityFilterType

        return {
            "attributes": (SecurityFilterCreateAttributes,),
            "type": (SecurityFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }
    json_api_model = SecurityFilterCreateDataJSON

    def __init__(self_, attributes: SecurityFilterCreateAttributes, type: SecurityFilterType, **kwargs):
        """
        Object for a single security filter.

        :param attributes: Object containing the attributes of the security filter to be created.
        :type attributes: SecurityFilterCreateAttributes

        :param type: The type of the resource. The value should always be ``security_filters``.
        :type type: SecurityFilterType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
