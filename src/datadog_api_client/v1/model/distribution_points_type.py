# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class DistributionPointsType(ModelSimple):
    """
    The type of the distribution point.

    :param value: If omitted defaults to "distribution". Must be one of ["distribution"].
    :type value: str
    """

    allowed_values = {
        "distribution",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DistributionPointsType.DISTRIBUTION = DistributionPointsType("distribution")
