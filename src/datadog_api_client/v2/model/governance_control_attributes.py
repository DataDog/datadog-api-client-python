# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.governance_control_parameters_map import GovernanceControlParametersMap
    from datadog_api_client.v2.model.governance_control_mitigation_definition import (
        GovernanceControlMitigationDefinition,
    )
    from datadog_api_client.v2.model.governance_control_parameter_definition import GovernanceControlParameterDefinition


class GovernanceControlAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.governance_control_parameters_map import GovernanceControlParametersMap
        from datadog_api_client.v2.model.governance_control_mitigation_definition import (
            GovernanceControlMitigationDefinition,
        )
        from datadog_api_client.v2.model.governance_control_parameter_definition import (
            GovernanceControlParameterDefinition,
        )

        return {
            "active_detections_count": (int,),
            "category": (str,),
            "created_at": (datetime,),
            "created_by": (str,),
            "description": (str,),
            "detection_frequency": (str,),
            "detection_parameters": (GovernanceControlParametersMap,),
            "detection_type": (str,),
            "feature_flags": ([str],),
            "insights": ([str],),
            "last_detection_at": (datetime, none_type),
            "mitigated_detections_count": (int,),
            "mitigation_parameters": (GovernanceControlParametersMap,),
            "mitigation_type": (str,),
            "mitigations": ([GovernanceControlMitigationDefinition],),
            "name": (str,),
            "next_steps": (str,),
            "notification_frequency": (str,),
            "notification_parameters": (GovernanceControlParametersMap,),
            "notification_type": (str,),
            "priority": (str,),
            "product": (str,),
            "release_status": (str,),
            "resource_type": (str,),
            "resource_type_display_name": (str,),
            "supported_detection_parameters": ([GovernanceControlParameterDefinition],),
            "supported_notification_parameters": ([GovernanceControlParameterDefinition],),
            "task": (str,),
            "type": (str,),
            "usage_concern": (str,),
        }

    attribute_map = {
        "active_detections_count": "active_detections_count",
        "category": "category",
        "created_at": "created_at",
        "created_by": "created_by",
        "description": "description",
        "detection_frequency": "detection_frequency",
        "detection_parameters": "detection_parameters",
        "detection_type": "detection_type",
        "feature_flags": "feature_flags",
        "insights": "insights",
        "last_detection_at": "last_detection_at",
        "mitigated_detections_count": "mitigated_detections_count",
        "mitigation_parameters": "mitigation_parameters",
        "mitigation_type": "mitigation_type",
        "mitigations": "mitigations",
        "name": "name",
        "next_steps": "next_steps",
        "notification_frequency": "notification_frequency",
        "notification_parameters": "notification_parameters",
        "notification_type": "notification_type",
        "priority": "priority",
        "product": "product",
        "release_status": "release_status",
        "resource_type": "resource_type",
        "resource_type_display_name": "resource_type_display_name",
        "supported_detection_parameters": "supported_detection_parameters",
        "supported_notification_parameters": "supported_notification_parameters",
        "task": "task",
        "type": "type",
        "usage_concern": "usage_concern",
    }

    def __init__(
        self_,
        active_detections_count: int,
        category: str,
        created_at: datetime,
        created_by: str,
        description: str,
        detection_frequency: str,
        detection_parameters: GovernanceControlParametersMap,
        detection_type: str,
        feature_flags: List[str],
        insights: List[str],
        last_detection_at: Union[datetime, none_type],
        mitigated_detections_count: int,
        mitigation_parameters: GovernanceControlParametersMap,
        mitigation_type: str,
        mitigations: List[GovernanceControlMitigationDefinition],
        name: str,
        next_steps: str,
        notification_frequency: str,
        notification_parameters: GovernanceControlParametersMap,
        notification_type: str,
        priority: str,
        product: str,
        release_status: str,
        resource_type: str,
        resource_type_display_name: str,
        supported_detection_parameters: List[GovernanceControlParameterDefinition],
        supported_notification_parameters: List[GovernanceControlParameterDefinition],
        task: str,
        type: str,
        usage_concern: str,
        **kwargs,
    ):
        """
        The attributes of a governance control.

        :param active_detections_count: The number of active detections for the control.
        :type active_detections_count: int

        :param category: The value driver the control is grouped under, such as ``security`` or ``cost``.
        :type category: str

        :param created_at: The time the control configuration was created.
        :type created_at: datetime

        :param created_by: The UUID of the user who created the control configuration.
        :type created_by: str

        :param description: A human-readable description of what the control detects.
        :type description: str

        :param detection_frequency: How often detections are evaluated for the control.
        :type detection_frequency: str

        :param detection_parameters: A free-form map of parameter names to their configured values.
        :type detection_parameters: GovernanceControlParametersMap

        :param detection_type: The detection type that uniquely identifies the control.
        :type detection_type: str

        :param feature_flags: The feature flags that gate the control.
        :type feature_flags: [str]

        :param insights: The insight slugs associated with the control.
        :type insights: [str]

        :param last_detection_at: The time of the most recent detection for the control. ``null`` when there are no detections.
        :type last_detection_at: datetime, none_type

        :param mitigated_detections_count: The number of mitigated detections for the control.
        :type mitigated_detections_count: int

        :param mitigation_parameters: A free-form map of parameter names to their configured values.
        :type mitigation_parameters: GovernanceControlParametersMap

        :param mitigation_type: The configured mitigation type for the control. Empty when not configured.
        :type mitigation_type: str

        :param mitigations: The mitigations available for a control.
        :type mitigations: [GovernanceControlMitigationDefinition]

        :param name: Human-readable name of the control.
        :type name: str

        :param next_steps: Guidance on the next steps to remediate detections for the control.
        :type next_steps: str

        :param notification_frequency: The configured notification frequency for the control. Empty when not configured.
        :type notification_frequency: str

        :param notification_parameters: A free-form map of parameter names to their configured values.
        :type notification_parameters: GovernanceControlParametersMap

        :param notification_type: The configured notification type for the control. Empty when not configured.
        :type notification_type: str

        :param priority: The priority of the control, such as ``High``.
        :type priority: str

        :param product: The product the control belongs to.
        :type product: str

        :param release_status: The release status of the control, such as ``prod`` or ``beta``.
        :type release_status: str

        :param resource_type: The type of resource the control evaluates.
        :type resource_type: str

        :param resource_type_display_name: The human-readable name of the resource type.
        :type resource_type_display_name: str

        :param supported_detection_parameters: An array of parameter definitions.
        :type supported_detection_parameters: [GovernanceControlParameterDefinition]

        :param supported_notification_parameters: An array of parameter definitions.
        :type supported_notification_parameters: [GovernanceControlParameterDefinition]

        :param task: A short description of the remediation task for the control.
        :type task: str

        :param type: The control type, such as ``Proactive`` or ``Detection``.
        :type type: str

        :param usage_concern: The usage concern the control addresses, such as ``Security`` or ``Cost Optimization``.
        :type usage_concern: str
        """
        super().__init__(kwargs)

        self_.active_detections_count = active_detections_count
        self_.category = category
        self_.created_at = created_at
        self_.created_by = created_by
        self_.description = description
        self_.detection_frequency = detection_frequency
        self_.detection_parameters = detection_parameters
        self_.detection_type = detection_type
        self_.feature_flags = feature_flags
        self_.insights = insights
        self_.last_detection_at = last_detection_at
        self_.mitigated_detections_count = mitigated_detections_count
        self_.mitigation_parameters = mitigation_parameters
        self_.mitigation_type = mitigation_type
        self_.mitigations = mitigations
        self_.name = name
        self_.next_steps = next_steps
        self_.notification_frequency = notification_frequency
        self_.notification_parameters = notification_parameters
        self_.notification_type = notification_type
        self_.priority = priority
        self_.product = product
        self_.release_status = release_status
        self_.resource_type = resource_type
        self_.resource_type_display_name = resource_type_display_name
        self_.supported_detection_parameters = supported_detection_parameters
        self_.supported_notification_parameters = supported_notification_parameters
        self_.task = task
        self_.type = type
        self_.usage_concern = usage_concern
