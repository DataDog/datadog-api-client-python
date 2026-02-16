"""
Generate data transformation description returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.workflow_automation_api import WorkflowAutomationApi
from datadog_api_client.v2.model.data_transformation_description_request import DataTransformationDescriptionRequest

body = DataTransformationDescriptionRequest(
    action_id="com.datadoghq.transform.timestamp",
    script="return new Date(data.timestamp).toISOString();",
)

configuration = Configuration()
configuration.unstable_operations["create_data_transformation_description"] = True
with ApiClient(configuration) as api_client:
    api_instance = WorkflowAutomationApi(api_client)
    response = api_instance.create_data_transformation_description(body=body)

    print(response)
