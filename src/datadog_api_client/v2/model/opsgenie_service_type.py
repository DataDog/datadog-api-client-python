# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class OpsgenieServiceType(ModelSimple):
    """
    Opsgenie service resource type.

    :param value: If omitted defaults to "opsgenie-service". Must be one of ["opsgenie-service"].
    :type value: str
    """

    allowed_values = {
        "opsgenie-service",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OpsgenieServiceType.OPSGENIE_SERVICE = OpsgenieServiceType("opsgenie-service")
