# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class WidgetGrouping(ModelSimple):
    """
    The kind of grouping to use.

    :param value: Must be one of ["check", "cluster"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "CHECK": "check",
            "CLUSTER": "cluster",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
