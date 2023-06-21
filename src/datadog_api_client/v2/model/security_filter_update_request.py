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


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_filter_update_data import SecurityFilterUpdateData
    from datadog_api_client.v2.model.security_filter_exclusion_filter import SecurityFilterExclusionFilter
    from datadog_api_client.v2.model.security_filter_filtered_data_type import SecurityFilterFilteredDataType


@dataclass
class SecurityFilterUpdateRequestJSON:
    exclusion_filters: Union[List[SecurityFilterExclusionFilter], UnsetType] = unset
    filtered_data_type: Union[SecurityFilterFilteredDataType, UnsetType] = unset
    is_enabled: Union[bool, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    query: Union[str, UnsetType] = unset
    version: Union[int, UnsetType] = unset


class SecurityFilterUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_filter_update_data import SecurityFilterUpdateData

        return {
            "data": (SecurityFilterUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = SecurityFilterUpdateRequestJSON

    def __init__(self_, data: SecurityFilterUpdateData, **kwargs):
        """
        The new security filter body.

        :param data: The new security filter properties.
        :type data: SecurityFilterUpdateData
        """
        super().__init__(kwargs)

        self_.data = data
