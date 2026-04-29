"""
Get Test Optimization service settings returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.test_optimization_api import TestOptimizationApi
from datadog_api_client.v2.model.test_optimization_get_service_settings_request import (
    TestOptimizationGetServiceSettingsRequest,
)
from datadog_api_client.v2.model.test_optimization_get_service_settings_request_attributes import (
    TestOptimizationGetServiceSettingsRequestAttributes,
)
from datadog_api_client.v2.model.test_optimization_get_service_settings_request_data import (
    TestOptimizationGetServiceSettingsRequestData,
)
from datadog_api_client.v2.model.test_optimization_get_service_settings_request_data_type import (
    TestOptimizationGetServiceSettingsRequestDataType,
)

body = TestOptimizationGetServiceSettingsRequest(
    data=TestOptimizationGetServiceSettingsRequestData(
        attributes=TestOptimizationGetServiceSettingsRequestAttributes(
            env="prod",
            repository_id="github.com/datadog/shopist",
            service_name="shopist",
        ),
        type=TestOptimizationGetServiceSettingsRequestDataType.TEST_OPTIMIZATION_GET_SERVICE_SETTINGS_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TestOptimizationApi(api_client)
    response = api_instance.get_test_optimization_service_settings(body=body)

    print(response)
