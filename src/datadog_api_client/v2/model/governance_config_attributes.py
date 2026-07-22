# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class GovernanceConfigAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "assignment_notifications_enabled": (bool,),
            "enabled": (bool,),
            "usage_attribution_configured": (bool,),
        }

    attribute_map = {
        "assignment_notifications_enabled": "assignment_notifications_enabled",
        "enabled": "enabled",
        "usage_attribution_configured": "usage_attribution_configured",
    }

    def __init__(
        self_, assignment_notifications_enabled: bool, enabled: bool, usage_attribution_configured: bool, **kwargs
    ):
        """
        The attributes of a Governance Console configuration.

        :param assignment_notifications_enabled: Whether notifications are sent to users when detections are assigned to them.
        :type assignment_notifications_enabled: bool

        :param enabled: Whether the Governance Console is enabled for the organization.
        :type enabled: bool

        :param usage_attribution_configured: Whether usage attribution is configured for the organization.
        :type usage_attribution_configured: bool
        """
        super().__init__(kwargs)

        self_.assignment_notifications_enabled = assignment_notifications_enabled
        self_.enabled = enabled
        self_.usage_attribution_configured = usage_attribution_configured
