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
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_response_data import (
        TimeseriesAnomalyInvestigationResponseData,
    )
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_response_meta import (
        TimeseriesAnomalyInvestigationResponseMeta,
    )


class TimeseriesAnomalyInvestigationResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_response_data import (
            TimeseriesAnomalyInvestigationResponseData,
        )
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_response_meta import (
            TimeseriesAnomalyInvestigationResponseMeta,
        )

        return {
            "data": (TimeseriesAnomalyInvestigationResponseData,),
            "meta": (TimeseriesAnomalyInvestigationResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: TimeseriesAnomalyInvestigationResponseData,
        meta: TimeseriesAnomalyInvestigationResponseMeta,
        **kwargs,
    ):
        """
        Response containing the anomaly investigation results and timeseries metadata.

        :param data: JSON:API resource containing anomaly investigation results.
        :type data: TimeseriesAnomalyInvestigationResponseData

        :param meta: Timeseries execution metadata for the single request accepted by this API version.
        :type meta: TimeseriesAnomalyInvestigationResponseMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
