import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import monitors_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitors_api.MonitorsApi(api_client)
    monitor_id = 1  # int | The ID of the monitor.
    body = MonitorUpdateRequest(
        message="message_example",
        name="name_example",
        options=MonitorOptions(
            enable_logs_sample=True,
            escalation_message="none",
            evaluation_delay=1,
            groupby_simple_monitor=True,
            include_tags=True,
            locked=True,
            min_failure_duration=0,
            min_location_failed=1,
            new_group_delay=1,
            new_host_delay=300,
            no_data_timeframe=1,
            notify_audit=False,
            notify_no_data=False,
            renotify_interval=1,
            renotify_occurrences=1,
            renotify_statuses=[
                MonitorRenotifyStatusType("alert"),
            ],
            require_full_window=True,
            silenced={
                "key": 1,
            },
            synthetics_check_id="synthetics_check_id_example",
            threshold_windows=MonitorThresholdWindowOptions(
                recovery_window="recovery_window_example",
                trigger_window="trigger_window_example",
            ),
            thresholds=MonitorThresholds(
                critical=3.14,
                critical_recovery=3.14,
                ok=3.14,
                unknown=3.14,
                warning=3.14,
                warning_recovery=3.14,
            ),
            timeout_h=1,
            variables=[
                MonitorFormulaAndFunctionQueryDefinition(),
            ],
        ),
        priority=1,
        query="query_example",
        restricted_roles=[
            "restricted_roles_example",
        ],
        tags=[
            "tags_example",
        ],
        type=MonitorType("query alert"),
    )  # MonitorUpdateRequest | Edit a monitor request body.

    # example passing only required values which don't have defaults set
    try:
        # Edit a monitor
        api_response = api_instance.update_monitor(monitor_id, body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MonitorsApi->update_monitor: %s\n" % e)
