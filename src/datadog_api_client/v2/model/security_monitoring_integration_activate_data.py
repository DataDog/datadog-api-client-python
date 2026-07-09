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
    from datadog_api_client.v2.model.security_monitoring_integration_activate_attributes import (
        SecurityMonitoringIntegrationActivateAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_integration_activate_resource_type import (
        SecurityMonitoringIntegrationActivateResourceType,
    )


class SecurityMonitoringIntegrationActivateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_integration_activate_attributes import (
            SecurityMonitoringIntegrationActivateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_integration_activate_resource_type import (
            SecurityMonitoringIntegrationActivateResourceType,
        )

        return {
            "attributes": (SecurityMonitoringIntegrationActivateAttributes,),
            "type": (SecurityMonitoringIntegrationActivateResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[SecurityMonitoringIntegrationActivateAttributes, UnsetType] = unset,
        type: Union[SecurityMonitoringIntegrationActivateResourceType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The configuration overrides for the integration to activate.

        :param attributes: Overrides applied when activating the integration. All fields are optional.
        :type attributes: SecurityMonitoringIntegrationActivateAttributes, optional

        :param type: The type of the resource. The value should always be ``activate_entra_id_request``.
        :type type: SecurityMonitoringIntegrationActivateResourceType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
