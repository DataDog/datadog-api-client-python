# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class ApmStatsQueryRowType(ModelSimple):
    """
    The level of detail for the request.

    :param value: Must be one of ["service", "resource", "span"].
    :type value: str
    """

    allowed_values = {
        "service",
        "resource",
        "span",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ApmStatsQueryRowType.SERVICE = ApmStatsQueryRowType("service")
ApmStatsQueryRowType.RESOURCE = ApmStatsQueryRowType("resource")
ApmStatsQueryRowType.SPAN = ApmStatsQueryRowType("span")
