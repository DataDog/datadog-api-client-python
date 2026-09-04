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
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_request_attributes import (
        TimeseriesAnomalyInvestigationRequestAttributes,
    )
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_type import TimeseriesAnomalyInvestigationType


class TimeseriesAnomalyInvestigationRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_request_attributes import (
            TimeseriesAnomalyInvestigationRequestAttributes,
        )
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_type import TimeseriesAnomalyInvestigationType

        return {
            "attributes": (TimeseriesAnomalyInvestigationRequestAttributes,),
            "type": (TimeseriesAnomalyInvestigationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: TimeseriesAnomalyInvestigationRequestAttributes,
        type: TimeseriesAnomalyInvestigationType,
        **kwargs,
    ):
        """
        JSON:API resource containing an anomaly investigation request.

        :param attributes: Attributes of an anomaly investigation request.
        :type attributes: TimeseriesAnomalyInvestigationRequestAttributes

        :param type: Resource type for a timeseries anomaly investigation.
        :type type: TimeseriesAnomalyInvestigationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
