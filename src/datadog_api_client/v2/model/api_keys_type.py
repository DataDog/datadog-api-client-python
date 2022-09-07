# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class APIKeysType(ModelSimple):
    """
    API Keys resource type.

    :param value: If omitted defaults to "api_keys". Must be one of ["api_keys"].
    :type value: str
    """

    allowed_values = {
        "api_keys",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


APIKeysType.API_KEYS = APIKeysType("api_keys")
