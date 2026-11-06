"""
Create a Data Jobs monitor with the aastra query dialect returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_formula_and_function_data_jobs_monitor_options import (
    MonitorFormulaAndFunctionDataJobsMonitorOptions,
)
from datadog_api_client.v1.model.monitor_formula_and_function_data_jobs_query_definition import (
    MonitorFormulaAndFunctionDataJobsQueryDefinition,
)
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_type import MonitorType

body = Monitor(
    name="Example-Monitor",
    type=MonitorType.DATA_JOBS_ALERT,
    query='formula("failed_runs(run_query)").by(name,workspace_name,entity_id).last(1d) > 0',
    message="Data jobs alert triggered",
    tags=[
        "test:examplemonitor",
        "env:ci",
    ],
    options=MonitorOptions(
        thresholds=MonitorThresholds(
            critical=0.0,
        ),
        variables=[
            MonitorFormulaAndFunctionDataJobsQueryDefinition(
                name="run_query",
                jobs_query="search for databricks_job",
                job_type="databricks.job",
                query_dialect="aastra",
                run_filter="env:prod",
                monitor_options=MonitorFormulaAndFunctionDataJobsMonitorOptions(
                    alert_on_every_failure=True,
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
