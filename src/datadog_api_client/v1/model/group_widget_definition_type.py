# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class GroupWidgetDefinitionType(ModelSimple):
    """
    Type of the group widget.

    :param value: If omitted defaults to "group". Must be one of ["group"].
    :type value: str
    """

    allowed_values = {
        "group",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GroupWidgetDefinitionType.GROUP = GroupWidgetDefinitionType("group")
