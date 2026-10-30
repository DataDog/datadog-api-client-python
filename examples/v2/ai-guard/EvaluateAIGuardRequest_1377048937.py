"""
Evaluate an AI Guard request with per-category confidence thresholds
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_guard_api import AIGuardApi
from datadog_api_client.v2.model.ai_guard_confidence_threshold import AIGuardConfidenceThreshold
from datadog_api_client.v2.model.ai_guard_evaluate_request import AIGuardEvaluateRequest
from datadog_api_client.v2.model.ai_guard_evaluate_request_data import AIGuardEvaluateRequestData
from datadog_api_client.v2.model.ai_guard_evaluate_request_data_attributes import AIGuardEvaluateRequestDataAttributes
from datadog_api_client.v2.model.ai_guard_evaluation_type import AIGuardEvaluationType
from datadog_api_client.v2.model.ai_guard_message import AIGuardMessage
from datadog_api_client.v2.model.ai_guard_message_role import AIGuardMessageRole
from datadog_api_client.v2.model.ai_guard_meta import AIGuardMeta

body = AIGuardEvaluateRequest(
    data=AIGuardEvaluateRequestData(
        type=AIGuardEvaluationType.EVALUATIONS,
        attributes=AIGuardEvaluateRequestDataAttributes(
            messages=[
                AIGuardMessage(
                    role=AIGuardMessageRole.USER,
                    content="Hello world!",
                ),
            ],
            meta=AIGuardMeta(
                confidence_threshold=AIGuardConfidenceThreshold(
                    flagging_global=0.6,
                    policy_evasion=0.9,
                    indirect_prompt_injection=0.4,
                ),
            ),
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["evaluate_ai_guard_request"] = True
with ApiClient(configuration) as api_client:
    api_instance = AIGuardApi(api_client)
    response = api_instance.evaluate_ai_guard_request(body=body)

    print(response)
