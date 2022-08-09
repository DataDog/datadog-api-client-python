# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class MonitorType(ModelSimple):
    """
    The type of the monitor. For more information about `type`, see the [monitor options](https://docs.datadoghq.com/monitors/guide/monitor_api_options/) docs.

    :param value: Must be one of ["composite", "event alert", "log alert", "metric alert", "process alert", "query alert", "rum alert", "service check", "synthetics alert", "trace-analytics alert", "slo alert", "event-v2 alert", "audit alert", "ci-pipelines alert", "ci-tests alert", "error-tracking alert"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "COMPOSITE": "composite",
            "EVENT_ALERT": "event alert",
            "LOG_ALERT": "log alert",
            "METRIC_ALERT": "metric alert",
            "PROCESS_ALERT": "process alert",
            "QUERY_ALERT": "query alert",
            "RUM_ALERT": "rum alert",
            "SERVICE_CHECK": "service check",
            "SYNTHETICS_ALERT": "synthetics alert",
            "TRACE_ANALYTICS_ALERT": "trace-analytics alert",
            "SLO_ALERT": "slo alert",
            "EVENT_V2_ALERT": "event-v2 alert",
            "AUDIT_ALERT": "audit alert",
            "CI_PIPELINES_ALERT": "ci-pipelines alert",
            "CI_TESTS_ALERT": "ci-tests alert",
            "ERROR_TRACKING_ALERT": "error-tracking alert",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
