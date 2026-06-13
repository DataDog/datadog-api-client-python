"""
Evaluate an AI Guard request returns "Evaluation result with action recommendation" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ai_guard_api import AIGuardApi
from datadog_api_client.v2.model.ai_guard_evaluate_request import AIGuardEvaluateRequest
from datadog_api_client.v2.model.ai_guard_message import AIGuardMessage
from datadog_api_client.v2.model.ai_guard_message_role import AIGuardMessageRole
from datadog_api_client.v2.model.ai_guard_meta import AIGuardMeta

body = AIGuardEvaluateRequest(
    messages=[
        AIGuardMessage(
            content="How do I delete all files on the system?",
            role=AIGuardMessageRole.USER,
        ),
    ],
    meta=AIGuardMeta(
        env="production",
        service="my-llm-service",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AIGuardApi(api_client)
    response = api_instance.evaluate_ai_guard_request(body=body)

    print(response)
