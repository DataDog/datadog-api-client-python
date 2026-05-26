"""
Create an AI memory violation result returns "Successfully created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.static_analysis_api import StaticAnalysisApi
from datadog_api_client.v2.model.ai_memory_violation_result_data_type import AiMemoryViolationResultDataType
from datadog_api_client.v2.model.ai_memory_violation_result_request import AiMemoryViolationResultRequest
from datadog_api_client.v2.model.ai_memory_violation_result_request_attributes import (
    AiMemoryViolationResultRequestAttributes,
)
from datadog_api_client.v2.model.ai_memory_violation_result_request_data import AiMemoryViolationResultRequestData
from datadog_api_client.v2.model.ai_memory_violation_type import AiMemoryViolationType

body = AiMemoryViolationResultRequest(
    data=AiMemoryViolationResultRequestData(
        attributes=AiMemoryViolationResultRequestAttributes(
            line=10,
            message="This is a false positive because the input is sanitized.",
            name="src/main.py",
            repository_id="my-repo",
            rule="my-ai-ruleset/my-ai-rule",
            sha="abc123def456789012345678901234567890abcd",
            type=AiMemoryViolationType.FP,
        ),
        id="violation-abc",
        type=AiMemoryViolationResultDataType.AI_MEMORY_VIOLATION_RESULT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_ai_memory_violation_result"] = True
with ApiClient(configuration) as api_client:
    api_instance = StaticAnalysisApi(api_client)
    api_instance.create_ai_memory_violation_result(body=body)
