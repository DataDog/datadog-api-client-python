# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_entity_risk_score import SecurityEntityRiskScore
    from datadog_api_client.v2.model.security_entity_risk_scores_meta import SecurityEntityRiskScoresMeta


class SecurityEntityRiskScoresResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_entity_risk_score import SecurityEntityRiskScore
        from datadog_api_client.v2.model.security_entity_risk_scores_meta import SecurityEntityRiskScoresMeta

        return {
            "data": ([SecurityEntityRiskScore],),
            "meta": (SecurityEntityRiskScoresMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[SecurityEntityRiskScore], meta: SecurityEntityRiskScoresMeta, **kwargs):
        """
        Response containing a list of entity risk scores

        :param data:
        :type data: [SecurityEntityRiskScore]

        :param meta: Metadata for pagination
        :type meta: SecurityEntityRiskScoresMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
