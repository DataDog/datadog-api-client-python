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
    from datadog_api_client.v2.model.security_monitoring_suppression_create_attributes import (
        SecurityMonitoringSuppressionCreateAttributes,
    )
    from datadog_api_client.v2.model.security_monitoring_suppression_type import SecurityMonitoringSuppressionType


class SecurityMonitoringSuppressionCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_suppression_create_attributes import (
            SecurityMonitoringSuppressionCreateAttributes,
        )
        from datadog_api_client.v2.model.security_monitoring_suppression_type import SecurityMonitoringSuppressionType

        return {
            "attributes": (SecurityMonitoringSuppressionCreateAttributes,),
            "type": (SecurityMonitoringSuppressionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SecurityMonitoringSuppressionCreateAttributes,
        type: SecurityMonitoringSuppressionType,
        **kwargs,
    ):
        """
        Object for a single suppression rule.

        :param attributes: Object containing the attributes of the suppression rule to be created.
        :type attributes: SecurityMonitoringSuppressionCreateAttributes

        :param type: The type of the resource. The value should always be ``suppressions``.
        :type type: SecurityMonitoringSuppressionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
