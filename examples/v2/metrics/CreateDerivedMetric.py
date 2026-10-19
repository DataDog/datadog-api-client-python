"""
Create a derived metric returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.derived_metric_attributes import DerivedMetricAttributes
from datadog_api_client.v2.model.derived_metric_create_data import DerivedMetricCreateData
from datadog_api_client.v2.model.derived_metric_create_request import DerivedMetricCreateRequest
from datadog_api_client.v2.model.derived_metric_definition import DerivedMetricDefinition
from datadog_api_client.v2.model.derived_metric_query import DerivedMetricQuery
from datadog_api_client.v2.model.derived_metrics_type import DerivedMetricsType

body = DerivedMetricCreateRequest(
    data=DerivedMetricCreateData(
        attributes=DerivedMetricAttributes(
            definition=DerivedMetricDefinition(
                formula="a",
                queries=[
                    DerivedMetricQuery(
                        data_source="metrics",
                        name="a",
                        query="avg:system.cpu.user{*}",
                    ),
                ],
            ),
        ),
        id="test.derived.examplemetric",
        type=DerivedMetricsType.DERIVED_METRICS,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.create_derived_metric(body=body)

    print(response)
