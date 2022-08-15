# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class WidgetMonitorSummarySort(ModelSimple):
    """
    Widget sorting methods.

    :param value: Must be one of ["name", "group", "status", "tags", "triggered", "group,asc", "group,desc", "name,asc", "name,desc", "status,asc", "status,desc", "tags,asc", "tags,desc", "triggered,asc", "triggered,desc", "priority,asc", "priority,desc"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "NAME": "name",
            "GROUP": "group",
            "STATUS": "status",
            "TAGS": "tags",
            "TRIGGERED": "triggered",
            "GROUP_ASCENDING": "group,asc",
            "GROUP_DESCENDING": "group,desc",
            "NAME_ASCENDING": "name,asc",
            "NAME_DESCENDING": "name,desc",
            "STATUS_ASCENDING": "status,asc",
            "STATUS_DESCENDING": "status,desc",
            "TAGS_ASCENDING": "tags,asc",
            "TAGS_DESCENDING": "tags,desc",
            "TRIGGERED_ASCENDING": "triggered,asc",
            "TRIGGERED_DESCENDING": "triggered,desc",
            "PRIORITY_ASCENDING": "priority,asc",
            "PRIORITY_DESCENDING": "priority,desc",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
