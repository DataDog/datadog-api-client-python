# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ServiceDefinitionV1Info(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "dd_service": (str,),
            "description": (str,),
            "display_name": (str,),
            "service_tier": (str,),
        }

    attribute_map = {
        "dd_service": "dd-service",
        "description": "description",
        "display_name": "display-name",
        "service_tier": "service-tier",
    }

    def __init__(self_, dd_service, *args, **kwargs):
        """
        Basic information about a service.

        :param dd_service: Unique identifier of the service. Must be unique across all services and is used to match with a service in Datadog.
        :type dd_service: str

        :param description: A short description of the service.
        :type description: str, optional

        :param display_name: A friendly name of the service.
        :type display_name: str, optional

        :param service_tier: Service tier.
        :type service_tier: str, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.dd_service = dd_service
