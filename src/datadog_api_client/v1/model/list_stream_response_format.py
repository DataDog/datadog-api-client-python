# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class ListStreamResponseFormat(ModelSimple):
    """
    Widget response format.

    :param value: If omitted defaults to "event_list". Must be one of ["event_list"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "EVENT_LIST": "event_list",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
