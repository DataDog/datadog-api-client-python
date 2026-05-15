"""
Create a Data Jobs monitor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.monitors_api import MonitorsApi
from datadog_api_client.v1.model.monitor import Monitor
from datadog_api_client.v1.model.monitor_formula_and_function_data_jobs_query_definition import (
    MonitorFormulaAndFunctionDataJobsQueryDefinition,
)
from datadog_api_client.v1.model.monitor_options import MonitorOptions
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v1.model.monitor_type import MonitorType

body = Monitor(
    name="Example-Monitor",
    type=MonitorType.DATA_JOBS_ALERT,
    query='formula("failed_runs(run_query)").by(job_name,workspace_name).last(10d) > 0',
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
                jobs_query="job_name:*",
                job_type="databricks.job",
                query_dialect="metric",
            ),
        ],
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = MonitorsApi(api_client)
    response = api_instance.create_monitor(body=body)

    print(response)
