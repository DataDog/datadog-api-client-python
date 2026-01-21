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
    from datadog_api_client.v2.model.security_entity_risk_score_attributes import SecurityEntityRiskScoreAttributes
    from datadog_api_client.v2.model.security_entity_risk_score_type import SecurityEntityRiskScoreType


class SecurityEntityRiskScore(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_entity_risk_score_attributes import SecurityEntityRiskScoreAttributes
        from datadog_api_client.v2.model.security_entity_risk_score_type import SecurityEntityRiskScoreType

        return {
            "attributes": (SecurityEntityRiskScoreAttributes,),
            "id": (str,),
            "type": (SecurityEntityRiskScoreType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: SecurityEntityRiskScoreAttributes, id: str, type: SecurityEntityRiskScoreType, **kwargs
    ):
        """
        An entity risk score containing security risk assessment information

        :param attributes: Attributes of an entity risk score
        :type attributes: SecurityEntityRiskScoreAttributes

        :param id: Unique identifier for the entity
        :type id: str

        :param type: Resource type
        :type type: SecurityEntityRiskScoreType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
