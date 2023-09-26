# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.spans_filter import SpansFilter
    from datadog_api_client.v2.model.retention_filter_all_type import RetentionFilterAllType


class RetentionFilterAllAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.spans_filter import SpansFilter
        from datadog_api_client.v2.model.retention_filter_all_type import RetentionFilterAllType

        return {
            "created_at": (int,),
            "created_by": (str,),
            "editable": (bool,),
            "enabled": (bool,),
            "execution_order": (int,),
            "filter": (SpansFilter,),
            "filter_type": (RetentionFilterAllType,),
            "modified_at": (int,),
            "modified_by": (str,),
            "name": (str,),
            "rate": (float,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "editable": "editable",
        "enabled": "enabled",
        "execution_order": "execution_order",
        "filter": "filter",
        "filter_type": "filter_type",
        "modified_at": "modified_at",
        "modified_by": "modified_by",
        "name": "name",
        "rate": "rate",
    }

    def __init__(
        self_,
        created_at: Union[int, UnsetType] = unset,
        created_by: Union[str, UnsetType] = unset,
        editable: Union[bool, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        execution_order: Union[int, UnsetType] = unset,
        filter: Union[SpansFilter, UnsetType] = unset,
        filter_type: Union[RetentionFilterAllType, UnsetType] = unset,
        modified_at: Union[int, UnsetType] = unset,
        modified_by: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        rate: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of the retention filter.

        :param created_at: The creation timestamp of the retention filter.
        :type created_at: int, optional

        :param created_by: The creator of the retention filter.
        :type created_by: str, optional

        :param editable: Shows whether the filter can be edited.
        :type editable: bool, optional

        :param enabled: The status of the retention filter (Enabled/Disabled).
        :type enabled: bool, optional

        :param execution_order: The execution order of the retention filter.
        :type execution_order: int, optional

        :param filter: The spans filter used to index spans.
        :type filter: SpansFilter, optional

        :param filter_type: The type of retention filter.
        :type filter_type: RetentionFilterAllType, optional

        :param modified_at: The modification timestamp of the retention filter.
        :type modified_at: int, optional

        :param modified_by: The modifier of the retention filter.
        :type modified_by: str, optional

        :param name: The name of the retention filter.
        :type name: str, optional

        :param rate: Sample rate to apply to spans going through this retention filter,
            a value of 1.0 keeps all spans matching the query.
        :type rate: float, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if editable is not unset:
            kwargs["editable"] = editable
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if execution_order is not unset:
            kwargs["execution_order"] = execution_order
        if filter is not unset:
            kwargs["filter"] = filter
        if filter_type is not unset:
            kwargs["filter_type"] = filter_type
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if modified_by is not unset:
            kwargs["modified_by"] = modified_by
        if name is not unset:
            kwargs["name"] = name
        if rate is not unset:
            kwargs["rate"] = rate
        super().__init__(kwargs)
