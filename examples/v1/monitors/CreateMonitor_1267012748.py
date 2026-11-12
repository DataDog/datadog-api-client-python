"""
Create a Data Jobs duration monitor returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_data_source import (
    MonitorFormulaAndFunctionDataQualityDataSource,
)
from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_detection_type import (
    MonitorFormulaAndFunctionDataQualityDetectionType,
)
from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_monitor_options import (
    MonitorFormulaAndFunctionDataQualityMonitorOptions,
)
from datadog_api_client.v1.model.monitor_formula_and_function_data_quality_query_definition import (
    MonitorFormulaAndFunctionDataQualityQueryDefinition,
)
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_type import MonitorType

body = Monitor(
    name="Example-Monitor",
    type=MonitorType.DATA_JOBS_ALERT,
    query='formula("job_duration(run_query)").detection(anomaly).by(name,workspace_name,entity_id) > 0',
    message="Data jobs duration alert triggered",
    tags=[
        "test:examplemonitor",
        "env:ci",
    ],
    options=MonitorOptions(
        variables=[
            MonitorFormulaAndFunctionDataQualityQueryDefinition(
                name="run_query",
                data_source=MonitorFormulaAndFunctionDataQualityDataSource.DATA_QUALITY_METRICS,
                schema_version="0.0.1",
                measure="duration",
                filter="search for databricks_job",
                run_filter="env:prod",
                group_by=[
                    "name",
                    "workspace_name",
                    "entity_id",
                ],
                monitor_options=MonitorFormulaAndFunctionDataQualityMonitorOptions(
                    detection_type=MonitorFormulaAndFunctionDataQualityDetectionType.ANOMALY,
                    consecutive_runs=2,
                ),
            ),
        ],
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor(body=body)

    print(response)
