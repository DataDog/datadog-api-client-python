# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class WidgetSummaryType(ModelSimple):
    """
    Which summary type should be used.

    :param value: Must be one of ["monitors", "groups", "combined"].
    :type value: str
    """

    allowed_values = {
        "monitors",
        "groups",
        "combined",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WidgetSummaryType.MONITORS = WidgetSummaryType("monitors")
WidgetSummaryType.GROUPS = WidgetSummaryType("groups")
WidgetSummaryType.COMBINED = WidgetSummaryType("combined")
