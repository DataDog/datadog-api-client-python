# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class OnMissingDataOption(ModelSimple):
    """
    Controls how groups or monitors are treated if an evaluation does not return any data points.
        The default option results in different behavior depending on the monitor query type.
        For monitors using Count queries, an empty monitor evaluation is treated as 0 and is compared to the threshold conditions.
        For monitors using any query type other than Count, for example Gauge, Measure, or Rate, the monitor shows the last known status.
        This option is only available for APM Trace Analytics, Audit Trail, CI, Error Tracking, Event, Logs, and RUM monitors.

    :param value: Must be one of ["default", "show_no_data", "show_and_notify_no_data", "resolve"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "DEFAULT": "default",
            "SHOW_NO_DATA": "show_no_data",
            "SHOW_AND_NOTIFY_NO_DATA": "show_and_notify_no_data",
            "RESOLVE": "resolve",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
