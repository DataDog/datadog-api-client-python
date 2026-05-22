# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_filter_exclusion_filter_response import (
        SecurityFilterExclusionFilterResponse,
    )
    from datadog_api_client.v2.model.security_filter_filtered_data_type import SecurityFilterFilteredDataType


class SecurityFilterVersionEntry(ModelNormal):
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
            "id": (str,),
            "is_builtin": (bool,),
            "is_enabled": (bool,),
            "name": (str,),
            "query": (str,),
            "version": (int,),
        }

    attribute_map = {
        "exclusion_filters": "exclusion_filters",
        "filtered_data_type": "filtered_data_type",
        "id": "id",
        "is_builtin": "is_builtin",
        "is_enabled": "is_enabled",
        "name": "name",
        "query": "query",
        "version": "version",
    }

    def __init__(
        self_,
        exclusion_filters: List[SecurityFilterExclusionFilterResponse],
        filtered_data_type: SecurityFilterFilteredDataType,
        id: str,
        is_builtin: bool,
        is_enabled: bool,
        name: str,
        query: str,
        version: int,
        **kwargs,
    ):
        """
        A single security filter as it existed at a given configuration version.

        :param exclusion_filters: The list of exclusion filters applied in this security filter.
        :type exclusion_filters: [SecurityFilterExclusionFilterResponse]

        :param filtered_data_type: The filtered data type.
        :type filtered_data_type: SecurityFilterFilteredDataType

        :param id: The ID of the security filter.
        :type id: str

        :param is_builtin: Whether the security filter is the built-in filter.
        :type is_builtin: bool

        :param is_enabled: Whether the security filter is enabled.
        :type is_enabled: bool

        :param name: The name of the security filter.
        :type name: str

        :param query: The query of the security filter.
        :type query: str

        :param version: The version of this security filter.
        :type version: int
        """
        super().__init__(kwargs)

        self_.exclusion_filters = exclusion_filters
        self_.filtered_data_type = filtered_data_type
        self_.id = id
        self_.is_builtin = is_builtin
        self_.is_enabled = is_enabled
        self_.name = name
        self_.query = query
        self_.version = version
