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
    from datadog_api_client.v2.model.ai_guard_evaluate_request_data_attributes import (
        AIGuardEvaluateRequestDataAttributes,
    )
    from datadog_api_client.v2.model.ai_guard_evaluation_type import AIGuardEvaluationType


class AIGuardEvaluateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_guard_evaluate_request_data_attributes import (
            AIGuardEvaluateRequestDataAttributes,
        )
        from datadog_api_client.v2.model.ai_guard_evaluation_type import AIGuardEvaluationType

        return {
            "attributes": (AIGuardEvaluateRequestDataAttributes,),
            "type": (AIGuardEvaluationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: AIGuardEvaluateRequestDataAttributes, type: AIGuardEvaluationType, **kwargs):
        """
        The JSON:API request envelope for an AI Guard evaluation.

        :param attributes: The conversation to evaluate and its metadata.
        :type attributes: AIGuardEvaluateRequestDataAttributes

        :param type: The JSON:API resource type for AI Guard evaluation requests and responses.
            Its value is ``evaluations`` for the action endpoint ``/api/v2/ai-guard/evaluate``.
        :type type: AIGuardEvaluationType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
