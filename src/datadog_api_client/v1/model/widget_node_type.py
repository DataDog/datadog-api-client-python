# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class WidgetNodeType(ModelSimple):
    """
    Which type of node to use in the map.

    :param value: Must be one of ["host", "container"].
    :type value: str
    """

    allowed_values = {
        "host",
        "container",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WidgetNodeType.HOST = WidgetNodeType("host")
WidgetNodeType.CONTAINER = WidgetNodeType("container")
