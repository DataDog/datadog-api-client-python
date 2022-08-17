# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class IncidentIntegrationMetadataType(ModelSimple):
    """
    Integration metadata resource type.

    :param value: If omitted defaults to "incident_integrations". Must be one of ["incident_integrations"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "INCIDENT_INTEGRATIONS": "incident_integrations",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
