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
    from datadog_api_client.v1_20270101.model.split_sort_compute import SplitSortCompute
    from datadog_api_client.v1_20270101.model.split_config_sort_order import SplitConfigSortOrder


class SplitConfigSort(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.split_sort_compute import SplitSortCompute
        from datadog_api_client.v1_20270101.model.split_config_sort_order import SplitConfigSortOrder

        return {
            "compute": (SplitSortCompute,),
            "order": (SplitConfigSortOrder,),
        }

    attribute_map = {
        "compute": "compute",
        "order": "order",
    }

    def __init__(self_, order: SplitConfigSortOrder, compute: Union[SplitSortCompute, UnsetType] = unset, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: SplitSortCompute, optional

        :param order: Test-only generated schema for the dashboard versioning proof of concept.
        :type order: SplitConfigSortOrder
        """
        if compute is not unset:
            kwargs["compute"] = compute
        super().__init__(kwargs)

        self_.order = order
