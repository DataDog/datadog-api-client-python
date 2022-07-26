# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class APIKeysSort(ModelSimple):
    """
    Sorting options

    :param value: If omitted defaults to "name". Must be one of ["created_at", "-created_at", "last4", "-last4", "modified_at", "-modified_at", "name", "-name"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "CREATED_AT_ASCENDING": "created_at",
            "CREATED_AT_DESCENDING": "-created_at",
            "LAST4_ASCENDING": "last4",
            "LAST4_DESCENDING": "-last4",
            "MODIFIED_AT_ASCENDING": "modified_at",
            "MODIFIED_AT_DESCENDING": "-modified_at",
            "NAME_ASCENDING": "name",
            "NAME_DESCENDING": "-name",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
