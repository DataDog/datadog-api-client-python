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
    from datadog_api_client.v1_20270101.model.composite_referential_data_query_compute_items_aggregation import (
        CompositeReferentialDataQueryComputeItemsAggregation,
    )


class CompositeReferentialDataQueryComputeItems(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.composite_referential_data_query_compute_items_aggregation import (
            CompositeReferentialDataQueryComputeItemsAggregation,
        )

        return {
            "aggregation": (CompositeReferentialDataQueryComputeItemsAggregation,),
            "column": (str,),
            "name": (str,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "column": "column",
        "name": "name",
    }

    def __init__(
        self_,
        aggregation: CompositeReferentialDataQueryComputeItemsAggregation,
        name: str,
        column: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param aggregation: Test-only generated schema for the dashboard versioning proof of concept.
        :type aggregation: CompositeReferentialDataQueryComputeItemsAggregation

        :param column: Test-only generated schema for the dashboard versioning proof of concept.
        :type column: str, optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str
        """
        if column is not unset:
            kwargs["column"] = column
        super().__init__(kwargs)

        self_.aggregation = aggregation
        self_.name = name
