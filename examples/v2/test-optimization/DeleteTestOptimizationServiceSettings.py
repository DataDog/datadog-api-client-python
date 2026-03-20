"""
Delete Test Optimization service settings returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.test_optimization_api import TestOptimizationApi
from datadog_api_client.v2.model.test_optimization_delete_service_settings_request import (
    TestOptimizationDeleteServiceSettingsRequest,
)
from datadog_api_client.v2.model.test_optimization_delete_service_settings_request_attributes import (
    TestOptimizationDeleteServiceSettingsRequestAttributes,
)
from datadog_api_client.v2.model.test_optimization_delete_service_settings_request_data import (
    TestOptimizationDeleteServiceSettingsRequestData,
)
from datadog_api_client.v2.model.test_optimization_delete_service_settings_request_data_type import (
    TestOptimizationDeleteServiceSettingsRequestDataType,
)

body = TestOptimizationDeleteServiceSettingsRequest(
    data=TestOptimizationDeleteServiceSettingsRequestData(
        attributes=TestOptimizationDeleteServiceSettingsRequestAttributes(
            env="prod",
            repository_id="github.com/datadog/shopist",
            service_name="shopist",
        ),
        type=TestOptimizationDeleteServiceSettingsRequestDataType.TEST_OPTIMIZATION_DELETE_SERVICE_SETTINGS_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["delete_test_optimization_service_settings"] = True
with ApiClient(configuration) as api_client:
    api_instance = TestOptimizationApi(api_client)
    api_instance.delete_test_optimization_service_settings(body=body)
