"""
Update Test Optimization service settings returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.test_optimization_api import TestOptimizationApi
from datadog_api_client.v2.model.test_optimization_update_service_settings_request import (
    TestOptimizationUpdateServiceSettingsRequest,
)
from datadog_api_client.v2.model.test_optimization_update_service_settings_request_attributes import (
    TestOptimizationUpdateServiceSettingsRequestAttributes,
)
from datadog_api_client.v2.model.test_optimization_update_service_settings_request_data import (
    TestOptimizationUpdateServiceSettingsRequestData,
)
from datadog_api_client.v2.model.test_optimization_update_service_settings_request_data_type import (
    TestOptimizationUpdateServiceSettingsRequestDataType,
)

body = TestOptimizationUpdateServiceSettingsRequest(
    data=TestOptimizationUpdateServiceSettingsRequestData(
        attributes=TestOptimizationUpdateServiceSettingsRequestAttributes(
            auto_test_retries_enabled=False,
            auto_test_retries_enabled_inherit=False,
            code_coverage_enabled=False,
            code_coverage_enabled_inherit=False,
            early_flake_detection_enabled=False,
            early_flake_detection_enabled_inherit=False,
            env="prod",
            failed_test_replay_enabled=False,
            failed_test_replay_enabled_inherit=False,
            pr_comments_enabled=False,
            repository_id="github.com/datadog/shopist",
            service_name="shopist",
            test_impact_analysis_enabled=True,
            test_impact_analysis_enabled_inherit=True,
        ),
        type=TestOptimizationUpdateServiceSettingsRequestDataType.TEST_OPTIMIZATION_UPDATE_SERVICE_SETTINGS_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = TestOptimizationApi(api_client)
    response = api_instance.update_test_optimization_service_settings(body=body)

    print(response)
