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
from datadog_api_client.v2.model.security_filter_exclusion_filter import SecurityFilterExclusionFilter
from datadog_api_client.v2.model.security_filter_filtered_data_type import SecurityFilterFilteredDataType

if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_filter_create_data import SecurityFilterCreateData


@dataclass
class SecurityFilterCreateRequestJSON:
    exclusion_filters: Union[List[SecurityFilterExclusionFilter], UnsetType] = unset
    filtered_data_type: Union[SecurityFilterFilteredDataType, UnsetType] = unset
    is_enabled: Union[bool, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    query: Union[str, UnsetType] = unset


class SecurityFilterCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_filter_create_data import SecurityFilterCreateData

        return {
            "data": (SecurityFilterCreateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = SecurityFilterCreateRequestJSON

    def __init__(self_, data: SecurityFilterCreateData, **kwargs):
        """
        Request object that includes the security filter that you would like to create.

        :param data: Object for a single security filter.
        :type data: SecurityFilterCreateData
        """
        super().__init__(kwargs)

        self_.data = data
