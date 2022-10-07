# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_filter_exclusion_filter_response import (
        SecurityFilterExclusionFilterResponse,
    )
    from datadog_api_client.v2.model.security_filter_filtered_data_type import SecurityFilterFilteredDataType


class SecurityFilterAttributes(ModelNormal):
    validations = {
        "version": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_filter_exclusion_filter_response import (
            SecurityFilterExclusionFilterResponse,
        )
        from datadog_api_client.v2.model.security_filter_filtered_data_type import SecurityFilterFilteredDataType

        return {
            "exclusion_filters": ([SecurityFilterExclusionFilterResponse],),
            "filtered_data_type": (SecurityFilterFilteredDataType,),
            "is_builtin": (bool,),
            "is_enabled": (bool,),
            "name": (str,),
            "query": (str,),
            "version": (int,),
        }

    attribute_map = {
        "exclusion_filters": "exclusion_filters",
        "filtered_data_type": "filtered_data_type",
        "is_builtin": "is_builtin",
        "is_enabled": "is_enabled",
        "name": "name",
        "query": "query",
        "version": "version",
    }

    def __init__(
        self_,
        exclusion_filters: Union[List[SecurityFilterExclusionFilterResponse], UnsetType] = unset,
        filtered_data_type: Union[SecurityFilterFilteredDataType, UnsetType] = unset,
        is_builtin: Union[bool, UnsetType] = unset,
        is_enabled: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        The object describing a security filter.

        :param exclusion_filters: The list of exclusion filters applied in this security filter.
        :type exclusion_filters: [SecurityFilterExclusionFilterResponse], optional

        :param filtered_data_type: The filtered data type.
        :type filtered_data_type: SecurityFilterFilteredDataType, optional

        :param is_builtin: Whether the security filter is the built-in filter.
        :type is_builtin: bool, optional

        :param is_enabled: Whether the security filter is enabled.
        :type is_enabled: bool, optional

        :param name: The security filter name.
        :type name: str, optional

        :param query: The security filter query. Logs accepted by this query will be accepted by this filter.
        :type query: str, optional

        :param version: The version of the security filter.
        :type version: int, optional
        """
        if exclusion_filters is not unset:
            kwargs["exclusion_filters"] = exclusion_filters
        if filtered_data_type is not unset:
            kwargs["filtered_data_type"] = filtered_data_type
        if is_builtin is not unset:
            kwargs["is_builtin"] = is_builtin
        if is_enabled is not unset:
            kwargs["is_enabled"] = is_enabled
        if name is not unset:
            kwargs["name"] = name
        if query is not unset:
            kwargs["query"] = query
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
