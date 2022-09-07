# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class WidgetComparator(ModelSimple):
    """
    Comparator to apply.

    :param value: Must be one of [">", ">=", "<", "<="].
    :type value: str
    """

    allowed_values = {
        ">",
        ">=",
        "<",
        "<=",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WidgetComparator.GREATER_THAN = WidgetComparator(">")
WidgetComparator.GREATER_THAN_OR_EQUAL_TO = WidgetComparator(">=")
WidgetComparator.LESS_THAN = WidgetComparator("<")
WidgetComparator.LESS_THAN_OR_EQUAL_TO = WidgetComparator("<=")
