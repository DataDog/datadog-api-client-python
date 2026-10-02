# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_create_metric_v2_request_data_attributes import (
        ExperimentsCreateMetricV2RequestDataAttributes,
    )
    from datadog_api_client.v2.model.metric_type import MetricType
    from datadog_api_client.v2.model.experiments_create_metric_numerator_attributes import (
        ExperimentsCreateMetricNumeratorAttributes,
    )
    from datadog_api_client.v2.model.experiments_create_metric_percentile_attributes import (
        ExperimentsCreateMetricPercentileAttributes,
    )


class ExperimentsCreateMetricV2RequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_create_metric_v2_request_data_attributes import (
            ExperimentsCreateMetricV2RequestDataAttributes,
        )
        from datadog_api_client.v2.model.metric_type import MetricType

        return {
            "attributes": (ExperimentsCreateMetricV2RequestDataAttributes,),
            "type": (MetricType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[
            ExperimentsCreateMetricV2RequestDataAttributes,
            ExperimentsCreateMetricNumeratorAttributes,
            ExperimentsCreateMetricPercentileAttributes,
        ],
        type: MetricType,
        **kwargs,
    ):
        """
        Metric resource to create.

        :param attributes: Configuration for the new metric. Supply either numerator_aggregation or percentile_aggregation. A denominator_aggregation requires numerator_aggregation. Omit unused aggregation fields; do not send them as null.
        :type attributes: ExperimentsCreateMetricV2RequestDataAttributes

        :param type: The metric resource type.
        :type type: MetricType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
