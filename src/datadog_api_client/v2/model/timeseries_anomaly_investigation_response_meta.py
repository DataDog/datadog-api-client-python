# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_query_status import (
        TimeseriesAnomalyInvestigationQueryStatus,
    )
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_meta_type import (
        TimeseriesAnomalyInvestigationMetaType,
    )
    from datadog_api_client.v2.model.timeseries_anomaly_investigation_results_warning import (
        TimeseriesAnomalyInvestigationResultsWarning,
    )


class TimeseriesAnomalyInvestigationResponseMeta(ModelNormal):
    validations = {
        "interval": {
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_query_status import (
            TimeseriesAnomalyInvestigationQueryStatus,
        )
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_meta_type import (
            TimeseriesAnomalyInvestigationMetaType,
        )
        from datadog_api_client.v2.model.timeseries_anomaly_investigation_results_warning import (
            TimeseriesAnomalyInvestigationResultsWarning,
        )

        return {
            "from_date": (int,),
            "interval": (int,),
            "queries": ([TimeseriesAnomalyInvestigationQueryStatus],),
            "res_type": (TimeseriesAnomalyInvestigationMetaType,),
            "results_warnings": ([TimeseriesAnomalyInvestigationResultsWarning],),
            "to_date": (int,),
        }

    attribute_map = {
        "from_date": "from_date",
        "interval": "interval",
        "queries": "queries",
        "res_type": "res_type",
        "results_warnings": "results_warnings",
        "to_date": "to_date",
    }

    def __init__(
        self_,
        from_date: int,
        interval: int,
        queries: List[TimeseriesAnomalyInvestigationQueryStatus],
        res_type: TimeseriesAnomalyInvestigationMetaType,
        results_warnings: List[TimeseriesAnomalyInvestigationResultsWarning],
        to_date: int,
        **kwargs,
    ):
        """
        Timeseries execution metadata for the single request accepted by this API version.

        :param from_date: Effective start of the timeseries query in milliseconds since the Unix epoch.
        :type from_date: int

        :param interval: Effective timeseries interval in milliseconds.
        :type interval: int

        :param queries: Execution status for the request's queries.
        :type queries: [TimeseriesAnomalyInvestigationQueryStatus]

        :param res_type: Response metadata type for a timeseries anomaly investigation.
        :type res_type: TimeseriesAnomalyInvestigationMetaType

        :param results_warnings: Non-fatal warnings produced while executing the investigation.
        :type results_warnings: [TimeseriesAnomalyInvestigationResultsWarning]

        :param to_date: Effective end of the timeseries query in milliseconds since the Unix epoch.
        :type to_date: int
        """
        super().__init__(kwargs)

        self_.from_date = from_date
        self_.interval = interval
        self_.queries = queries
        self_.res_type = res_type
        self_.results_warnings = results_warnings
        self_.to_date = to_date
