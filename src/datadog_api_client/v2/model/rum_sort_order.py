# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class RUMSortOrder(ModelSimple):
    """
    The order to use, ascending or descending.

    :param value: Must be one of ["asc", "desc"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "ASCENDING": "asc",
            "DESCENDING": "desc",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
