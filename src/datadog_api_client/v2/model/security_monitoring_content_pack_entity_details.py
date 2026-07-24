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
    from datadog_api_client.v2.model.security_monitoring_content_pack_activation import (
        SecurityMonitoringContentPackActivation,
    )
    from datadog_api_client.v2.model.security_monitoring_content_pack_entity_details_type import (
        SecurityMonitoringContentPackEntityDetailsType,
    )


class SecurityMonitoringContentPackEntityDetails(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_content_pack_activation import (
            SecurityMonitoringContentPackActivation,
        )
        from datadog_api_client.v2.model.security_monitoring_content_pack_entity_details_type import (
            SecurityMonitoringContentPackEntityDetailsType,
        )

        return {
            "cp_activation": (SecurityMonitoringContentPackActivation,),
            "type": (SecurityMonitoringContentPackEntityDetailsType,),
        }

    attribute_map = {
        "cp_activation": "cp_activation",
        "type": "type",
    }

    def __init__(
        self_,
        cp_activation: SecurityMonitoringContentPackActivation,
        type: SecurityMonitoringContentPackEntityDetailsType,
        **kwargs,
    ):
        """
        Details for an entity or identity content pack.

        :param cp_activation: The activation status of a content pack.
        :type cp_activation: SecurityMonitoringContentPackActivation

        :param type: Type for entity content pack details.
        :type type: SecurityMonitoringContentPackEntityDetailsType
        """
        super().__init__(kwargs)

        self_.cp_activation = cp_activation
        self_.type = type
