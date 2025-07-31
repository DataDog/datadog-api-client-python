# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.service_now_credentials import ServiceNowCredentials
    from datadog_api_client.v2.model.service_now_integration_type import ServiceNowIntegrationType
    from datadog_api_client.v2.model.service_now_basic_auth import ServiceNowBasicAuth


class ServiceNowIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_now_credentials import ServiceNowCredentials
        from datadog_api_client.v2.model.service_now_integration_type import ServiceNowIntegrationType

        return {
            "credentials": (ServiceNowCredentials,),
            "type": (ServiceNowIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_, credentials: Union[ServiceNowCredentials, ServiceNowBasicAuth], type: ServiceNowIntegrationType, **kwargs
    ):
        """
        The definition of the ``ServiceNowIntegration`` object.

        :param credentials: The definition of the ``ServiceNowCredentials`` object.
        :type credentials: ServiceNowCredentials

        :param type: The definition of the ``ServiceNowIntegrationType`` object.
        :type type: ServiceNowIntegrationType
        """
        super().__init__(kwargs)

        self_.credentials = credentials
        self_.type = type
