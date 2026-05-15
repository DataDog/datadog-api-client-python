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
    from datadog_api_client.v2.model.cost_metric_type import CostMetricType


class CostMetric(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_metric_type import CostMetricType

        return {
            "id": (str,),
            "type": (CostMetricType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: CostMetricType, **kwargs):
        """
        A Cloud Cost Management metric that has data for the requested period.

        :param id: The metric name, for example ``aws.cost.net.amortized``.
        :type id: str

        :param type: Type of the Cloud Cost Management available metric resource.
        :type type: CostMetricType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
