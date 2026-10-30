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
    from datadog_api_client.v2.model.ai_guard_evaluate_attributes_response import AIGuardEvaluateAttributesResponse
    from datadog_api_client.v2.model.ai_guard_evaluation_type import AIGuardEvaluationType


class AIGuardEvaluateDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_guard_evaluate_attributes_response import AIGuardEvaluateAttributesResponse
        from datadog_api_client.v2.model.ai_guard_evaluation_type import AIGuardEvaluationType

        return {
            "attributes": (AIGuardEvaluateAttributesResponse,),
            "id": (str,),
            "type": (AIGuardEvaluationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: AIGuardEvaluateAttributesResponse, id: str, type: AIGuardEvaluationType, **kwargs):
        """
        The JSON:API evaluation resource.

        :param attributes: The evaluation result with the recommended action and detected threat information.
        :type attributes: AIGuardEvaluateAttributesResponse

        :param id: The unique identifier of the evaluation.
        :type id: str

        :param type: The JSON:API resource type for AI Guard evaluation requests and responses.
            Its value is ``evaluations`` for the action endpoint ``/api/v2/ai-guard/evaluate``.
        :type type: AIGuardEvaluationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
