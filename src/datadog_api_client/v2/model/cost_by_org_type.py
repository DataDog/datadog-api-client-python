# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class CostByOrgType(ModelSimple):
    """
    Type of cost data.

    :param value: If omitted defaults to "cost_by_org". Must be one of ["cost_by_org"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "COST_BY_ORG": "cost_by_org",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
