# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_metric_collection_v2_dto_data_attributes_metrics_items import (
        ExperimentsMetricCollectionV2DTODataAttributesMetricsItems,
    )


class ExperimentsMetricCollectionV2DTODataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_metric_collection_v2_dto_data_attributes_metrics_items import (
            ExperimentsMetricCollectionV2DTODataAttributesMetricsItems,
        )

        return {
            "created_at": (datetime,),
            "description": (str, none_type),
            "is_guardrail": (bool,),
            "metric_count": (int,),
            "metrics": ([ExperimentsMetricCollectionV2DTODataAttributesMetricsItems],),
            "name": (str,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "created_at": "created_at",
        "description": "description",
        "is_guardrail": "is_guardrail",
        "metric_count": "metric_count",
        "metrics": "metrics",
        "name": "name",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        description: Union[str, none_type, UnsetType] = unset,
        is_guardrail: Union[bool, UnsetType] = unset,
        metric_count: Union[int, UnsetType] = unset,
        metrics: Union[List[ExperimentsMetricCollectionV2DTODataAttributesMetricsItems], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Details of the metric collection.

        :param created_at: Time when this resource was created.
        :type created_at: datetime, optional

        :param description: Text that explains the metric collection.
        :type description: str, none_type, optional

        :param is_guardrail: Whether the collection is used for guardrail metrics.
        :type is_guardrail: bool, optional

        :param metric_count: Number of metrics in this collection.
        :type metric_count: int, optional

        :param metrics: Metrics included in this collection.
        :type metrics: [ExperimentsMetricCollectionV2DTODataAttributesMetricsItems], optional

        :param name: Display name of the metric collection.
        :type name: str, optional

        :param updated_at: Time when this resource was last updated.
        :type updated_at: datetime, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if description is not unset:
            kwargs["description"] = description
        if is_guardrail is not unset:
            kwargs["is_guardrail"] = is_guardrail
        if metric_count is not unset:
            kwargs["metric_count"] = metric_count
        if metrics is not unset:
            kwargs["metrics"] = metrics
        if name is not unset:
            kwargs["name"] = name
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        super().__init__(kwargs)
