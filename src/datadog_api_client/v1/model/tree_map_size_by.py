# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class TreeMapSizeBy(ModelSimple):
    """
    (deprecated) The attribute formerly used to determine size in the widget.

    :param value: Must be one of ["pct_cpu", "pct_mem"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "PCT_CPU": "pct_cpu",
            "PCT_MEM": "pct_mem",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
