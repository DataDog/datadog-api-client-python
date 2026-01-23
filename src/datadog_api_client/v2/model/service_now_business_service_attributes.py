# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


class ServiceNowBusinessServiceAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "instance_id": (UUID,),
            "service_name": (str,),
            "service_sys_id": (str,),
        }

    attribute_map = {
        "instance_id": "instance_id",
        "service_name": "service_name",
        "service_sys_id": "service_sys_id",
    }

    def __init__(self_, instance_id: UUID, service_name: str, service_sys_id: str, **kwargs):
        """
        Attributes of a ServiceNow business service

        :param instance_id: The ID of the ServiceNow instance
        :type instance_id: UUID

        :param service_name: The name of the business service
        :type service_name: str

        :param service_sys_id: The system ID of the business service in ServiceNow
        :type service_sys_id: str
        """
        super().__init__(kwargs)

        self_.instance_id = instance_id
        self_.service_name = service_name
        self_.service_sys_id = service_sys_id
