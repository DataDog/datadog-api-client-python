"""
Investigate a timeseries anomaly returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.timeseries_anomaly_investigations_api import TimeseriesAnomalyInvestigationsApi
from datadog_api_client.v2.model.timeseries_anomaly_investigation_data_source import (
    TimeseriesAnomalyInvestigationDataSource,
)
from datadog_api_client.v2.model.timeseries_anomaly_investigation_formula import TimeseriesAnomalyInvestigationFormula
from datadog_api_client.v2.model.timeseries_anomaly_investigation_metric_query import (
    TimeseriesAnomalyInvestigationMetricQuery,
)
from datadog_api_client.v2.model.timeseries_anomaly_investigation_request import TimeseriesAnomalyInvestigationRequest
from datadog_api_client.v2.model.timeseries_anomaly_investigation_request_attributes import (
    TimeseriesAnomalyInvestigationRequestAttributes,
)
from datadog_api_client.v2.model.timeseries_anomaly_investigation_request_data import (
    TimeseriesAnomalyInvestigationRequestData,
)
from datadog_api_client.v2.model.timeseries_anomaly_investigation_timeseries_request import (
    TimeseriesAnomalyInvestigationTimeseriesRequest,
)
from datadog_api_client.v2.model.timeseries_anomaly_investigation_type import TimeseriesAnomalyInvestigationType

body = TimeseriesAnomalyInvestigationRequest(
    data=TimeseriesAnomalyInvestigationRequestData(
        attributes=TimeseriesAnomalyInvestigationRequestAttributes(
            requests=[
                TimeseriesAnomalyInvestigationTimeseriesRequest(
                    formulas=[
                        TimeseriesAnomalyInvestigationFormula(
                            formula="anomalies(query1, 'agile', 3)",
                        ),
                    ],
                    _from=1754406000000,
                    queries=[
                        TimeseriesAnomalyInvestigationMetricQuery(
                            data_source=TimeseriesAnomalyInvestigationDataSource.METRICS,
                            name="query1",
                            query="avg:system.cpu.user{env:prod} by {service}",
                        ),
                    ],
                    to=1754423940000,
                ),
            ],
        ),
        type=TimeseriesAnomalyInvestigationType.TIMESERIES_ANOMALY_INVESTIGATION,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_timeseries_anomaly_investigation"] = True
with ApiClient(configuration) as api_client:
    api_instance = TimeseriesAnomalyInvestigationsApi(api_client)
    response = api_instance.create_timeseries_anomaly_investigation(body=body)

    print(response)
