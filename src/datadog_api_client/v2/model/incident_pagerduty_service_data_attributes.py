# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentPagerdutyServiceDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "handle": (str,),
            "name": (str,),
            "service_id": (str,),
            "webhooks_enabled": (bool,),
        }

    attribute_map = {
        "handle": "handle",
        "name": "name",
        "service_id": "service_id",
        "webhooks_enabled": "webhooks_enabled",
    }

    def __init__(self_, handle: str, name: str, service_id: str, webhooks_enabled: bool, **kwargs):
        """
        Attributes of a PagerDuty service.

        :param handle: The handle for the PagerDuty service.
        :type handle: str

        :param name: The name of the PagerDuty service.
        :type name: str

        :param service_id: The PagerDuty service identifier.
        :type service_id: str

        :param webhooks_enabled: Whether webhooks are enabled for this service.
        :type webhooks_enabled: bool
        """
        super().__init__(kwargs)

        self_.handle = handle
        self_.name = name
        self_.service_id = service_id
        self_.webhooks_enabled = webhooks_enabled
