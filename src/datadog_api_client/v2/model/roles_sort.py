# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class RolesSort(ModelSimple):
    """
    Sorting options for roles.

    :param value: If omitted defaults to "name". Must be one of ["name", "-name", "modified_at", "-modified_at", "user_count", "-user_count"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "NAME_ASCENDING": "name",
            "NAME_DESCENDING": "-name",
            "MODIFIED_AT_ASCENDING": "modified_at",
            "MODIFIED_AT_DESCENDING": "-modified_at",
            "USER_COUNT_ASCENDING": "user_count",
            "USER_COUNT_DESCENDING": "-user_count",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
