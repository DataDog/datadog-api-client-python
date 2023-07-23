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
    from datadog_api_client.v2.model.security_filter import SecurityFilter
    from datadog_api_client.v2.model.security_filter_meta import SecurityFilterMeta
    from datadog_api_client.v2.model.security_filter_exclusion_filter_response import (
        SecurityFilterExclusionFilterResponse,
    )
    from datadog_api_client.v2.model.security_filter_filtered_data_type import SecurityFilterFilteredDataType


@dataclass
class SecurityFilterResponseJSON:
    id: str
    exclusion_filters: Union[List[SecurityFilterExclusionFilterResponse], UnsetType] = unset
    filtered_data_type: Union[SecurityFilterFilteredDataType, UnsetType] = unset
    is_builtin: Union[bool, UnsetType] = unset
    is_enabled: Union[bool, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    query: Union[str, UnsetType] = unset
    version: Union[int, UnsetType] = unset


class SecurityFilterResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_filter import SecurityFilter
        from datadog_api_client.v2.model.security_filter_meta import SecurityFilterMeta

        return {
            "data": (SecurityFilter,),
            "meta": (SecurityFilterMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }
    json_api_model = SecurityFilterResponseJSON

    def __init__(
        self_,
        data: Union[SecurityFilter, UnsetType] = unset,
        meta: Union[SecurityFilterMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response object which includes a single security filter.

        :param data: The security filter's properties.
        :type data: SecurityFilter, optional

        :param meta: Optional metadata associated to the response.
        :type meta: SecurityFilterMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
