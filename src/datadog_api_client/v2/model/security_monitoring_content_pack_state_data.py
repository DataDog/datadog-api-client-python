# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_content_pack_state_attributes import (
        SecurityMonitoringContentPackStateAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_content_pack_state_type import (
        SecurityMonitoringContentPackStateType,
    )


class SecurityMonitoringContentPackStateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_content_pack_state_attributes import (
            SecurityMonitoringContentPackStateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_content_pack_state_type import (
            SecurityMonitoringContentPackStateType,
        )

        return {
            "attributes": (SecurityMonitoringContentPackStateAttributes,),
            "id": (str,),
            "type": (SecurityMonitoringContentPackStateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringContentPackStateAttributes,
        id: str,
        type: SecurityMonitoringContentPackStateType,
        **kwargs,
    ):
        """
        Content pack state data.

        :param attributes: Attributes of a content pack state
        :type attributes: SecurityMonitoringContentPackStateAttributes

        :param id: The content pack identifier.
        :type id: str

        :param type: Type for content pack state object
        :type type: SecurityMonitoringContentPackStateType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
