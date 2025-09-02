# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.service_now_credentials_update import ServiceNowCredentialsUpdate
    from datadog_api_client.v2.model.service_now_integration_type import ServiceNowIntegrationType
    from datadog_api_client.v2.model.service_now_basic_auth_update import ServiceNowBasicAuthUpdate


class ServiceNowIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_now_credentials_update import ServiceNowCredentialsUpdate
        from datadog_api_client.v2.model.service_now_integration_type import ServiceNowIntegrationType

        return {
            "credentials": (ServiceNowCredentialsUpdate,),
            "type": (ServiceNowIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: ServiceNowIntegrationType,
        credentials: Union[ServiceNowCredentialsUpdate, ServiceNowBasicAuthUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``ServiceNowIntegrationUpdate`` object.

        :param credentials: The definition of the ``ServiceNowCredentialsUpdate`` object.
        :type credentials: ServiceNowCredentialsUpdate, optional

        :param type: The definition of the ``ServiceNowIntegrationType`` object.
        :type type: ServiceNowIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
