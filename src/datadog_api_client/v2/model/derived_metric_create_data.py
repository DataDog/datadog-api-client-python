# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.derived_metric_attributes import DerivedMetricAttributes
    from datadog_api_client.v2.model.derived_metrics_type import DerivedMetricsType


class DerivedMetricCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.derived_metric_attributes import DerivedMetricAttributes
        from datadog_api_client.v2.model.derived_metrics_type import DerivedMetricsType

        return {
            "attributes": (DerivedMetricAttributes,),
            "id": (str,),
            "type": (DerivedMetricsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: DerivedMetricAttributes, id: str, type: DerivedMetricsType, **kwargs):
        """
        Data object for creating or updating a derived metric.

        :param attributes: Attributes of a derived metric.
        :type attributes: DerivedMetricAttributes

        :param id: The derived metric name used as the resource ID.
        :type id: str

        :param type: The derived metric resource type.
        :type type: DerivedMetricsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
