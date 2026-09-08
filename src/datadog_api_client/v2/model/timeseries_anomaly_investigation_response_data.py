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
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_response_attributes import (
        TimeseriesAnomalyInvestigationResponseAttributes,
    )
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_response_id import (
        TimeseriesAnomalyInvestigationResponseID,
    )
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_type import TimeseriesAnomalyInvestigationType


class TimeseriesAnomalyInvestigationResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_response_attributes import (
            TimeseriesAnomalyInvestigationResponseAttributes,
        )
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_response_id import (
            TimeseriesAnomalyInvestigationResponseID,
        )
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_type import TimeseriesAnomalyInvestigationType

        return {
            "attributes": (TimeseriesAnomalyInvestigationResponseAttributes,),
            "id": (TimeseriesAnomalyInvestigationResponseID,),
            "type": (TimeseriesAnomalyInvestigationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: TimeseriesAnomalyInvestigationResponseAttributes,
        id: TimeseriesAnomalyInvestigationResponseID,
        type: TimeseriesAnomalyInvestigationType,
        **kwargs,
    ):
        """
        JSON:API resource containing anomaly investigation results.

        :param attributes: Attributes of an anomaly investigation response.
        :type attributes: TimeseriesAnomalyInvestigationResponseAttributes

        :param id: Stable identifier for an anomaly investigation response resource.
        :type id: TimeseriesAnomalyInvestigationResponseID

        :param type: Resource type for a timeseries anomaly investigation.
        :type type: TimeseriesAnomalyInvestigationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
