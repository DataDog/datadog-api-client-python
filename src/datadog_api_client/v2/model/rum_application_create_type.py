# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class RUMApplicationCreateType(ModelSimple):
    """
    RUM application creation type.

    :param value: If omitted defaults to "rum_application_create". Must be one of ["rum_application_create"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "RUM_APPLICATION_CREATE": "rum_application_create",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
