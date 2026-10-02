# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_create_metric_collection_v2_request_data_attributes_metrics_items import (
        ExperimentsCreateMetricCollectionV2RequestDataAttributesMetricsItems,
    )


class ExperimentsPatchMetricCollectionV2RequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_create_metric_collection_v2_request_data_attributes_metrics_items import (
            ExperimentsCreateMetricCollectionV2RequestDataAttributesMetricsItems,
        )

        return {
            "description": (str, none_type),
            "is_guardrail": (bool,),
            "metrics": ([ExperimentsCreateMetricCollectionV2RequestDataAttributesMetricsItems],),
            "name": (str,),
        }

    attribute_map = {
        "description": "description",
        "is_guardrail": "is_guardrail",
        "metrics": "metrics",
        "name": "name",
    }

    def __init__(
        self_,
        description: Union[str, none_type, UnsetType] = unset,
        is_guardrail: Union[bool, UnsetType] = unset,
        metrics: Union[List[ExperimentsCreateMetricCollectionV2RequestDataAttributesMetricsItems], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Fields supplied to update the metric collection.

        :param description: Text that explains the metric collection.
        :type description: str, none_type, optional

        :param is_guardrail: Whether the collection is used for guardrail metrics.
        :type is_guardrail: bool, optional

        :param metrics: Metrics included in this collection.
        :type metrics: [ExperimentsCreateMetricCollectionV2RequestDataAttributesMetricsItems], optional

        :param name: Display name of the metric collection.
        :type name: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if is_guardrail is not unset:
            kwargs["is_guardrail"] = is_guardrail
        if metrics is not unset:
            kwargs["metrics"] = metrics
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
