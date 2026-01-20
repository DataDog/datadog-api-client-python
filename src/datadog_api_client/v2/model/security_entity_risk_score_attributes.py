# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_entity_config_risks import SecurityEntityConfigRisks
    from datadog_api_client.v2.model.security_entity_metadata import SecurityEntityMetadata
    from datadog_api_client.v2.model.security_entity_risk_score_attributes_severity import (
        SecurityEntityRiskScoreAttributesSeverity,
    )


class SecurityEntityRiskScoreAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_entity_config_risks import SecurityEntityConfigRisks
        from datadog_api_client.v2.model.security_entity_metadata import SecurityEntityMetadata
        from datadog_api_client.v2.model.security_entity_risk_score_attributes_severity import (
            SecurityEntityRiskScoreAttributesSeverity,
        )

        return {
            "config_risks": (SecurityEntityConfigRisks,),
            "entity_id": (str,),
            "entity_metadata": (SecurityEntityMetadata,),
            "entity_name": (str,),
            "entity_providers": ([str],),
            "entity_roles": ([str],),
            "entity_type": (str,),
            "first_detected": (int,),
            "last_activity_title": (str,),
            "last_detected": (int,),
            "risk_score": (float,),
            "risk_score_evolution": (float,),
            "severity": (SecurityEntityRiskScoreAttributesSeverity,),
            "signals_detected": (int,),
        }

    attribute_map = {
        "config_risks": "configRisks",
        "entity_id": "entityID",
        "entity_metadata": "entityMetadata",
        "entity_name": "entityName",
        "entity_providers": "entityProviders",
        "entity_roles": "entityRoles",
        "entity_type": "entityType",
        "first_detected": "firstDetected",
        "last_activity_title": "lastActivityTitle",
        "last_detected": "lastDetected",
        "risk_score": "riskScore",
        "risk_score_evolution": "riskScoreEvolution",
        "severity": "severity",
        "signals_detected": "signalsDetected",
    }

    def __init__(
        self_,
        config_risks: SecurityEntityConfigRisks,
        entity_id: str,
        entity_metadata: SecurityEntityMetadata,
        entity_providers: List[str],
        entity_type: str,
        first_detected: int,
        last_activity_title: str,
        last_detected: int,
        risk_score: float,
        risk_score_evolution: float,
        severity: SecurityEntityRiskScoreAttributesSeverity,
        signals_detected: int,
        entity_name: Union[str, UnsetType] = unset,
        entity_roles: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an entity risk score

        :param config_risks: Configuration risks associated with the entity
        :type config_risks: SecurityEntityConfigRisks

        :param entity_id: Unique identifier for the entity
        :type entity_id: str

        :param entity_metadata: Metadata about the entity from cloud providers
        :type entity_metadata: SecurityEntityMetadata

        :param entity_name: Human-readable name of the entity
        :type entity_name: str, optional

        :param entity_providers: Cloud providers associated with the entity
        :type entity_providers: [str]

        :param entity_roles: Roles associated with the entity
        :type entity_roles: [str], optional

        :param entity_type: Type of the entity (e.g., aws_iam_user, aws_ec2_instance)
        :type entity_type: str

        :param first_detected: Timestamp when the entity was first detected (Unix milliseconds)
        :type first_detected: int

        :param last_activity_title: Title of the most recent signal detected for this entity
        :type last_activity_title: str

        :param last_detected: Timestamp when the entity was last detected (Unix milliseconds)
        :type last_detected: int

        :param risk_score: Current risk score for the entity
        :type risk_score: float

        :param risk_score_evolution: Change in risk score compared to previous period
        :type risk_score_evolution: float

        :param severity: Severity level based on risk score
        :type severity: SecurityEntityRiskScoreAttributesSeverity

        :param signals_detected: Number of security signals detected for this entity
        :type signals_detected: int
        """
        if entity_name is not unset:
            kwargs["entity_name"] = entity_name
        if entity_roles is not unset:
            kwargs["entity_roles"] = entity_roles
        super().__init__(kwargs)

        self_.config_risks = config_risks
        self_.entity_id = entity_id
        self_.entity_metadata = entity_metadata
        self_.entity_providers = entity_providers
        self_.entity_type = entity_type
        self_.first_detected = first_detected
        self_.last_activity_title = last_activity_title
        self_.last_detected = last_detected
        self_.risk_score = risk_score
        self_.risk_score_evolution = risk_score_evolution
        self_.severity = severity
        self_.signals_detected = signals_detected
