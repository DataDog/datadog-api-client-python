"""
Edit a mobile test returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_check_type import SyntheticsCheckType
from datadog_api_client.v1.model.synthetics_config_variable import SyntheticsConfigVariable
from datadog_api_client.v1.model.synthetics_config_variable_type import SyntheticsConfigVariableType
from datadog_api_client.v1.model.synthetics_mobile_step import SyntheticsMobileStep
from datadog_api_client.v1.model.synthetics_mobile_step_params import SyntheticsMobileStepParams
from datadog_api_client.v1.model.synthetics_mobile_step_params_direction import SyntheticsMobileStepParamsDirection
from datadog_api_client.v1.model.synthetics_mobile_step_params_element import SyntheticsMobileStepParamsElement
from datadog_api_client.v1.model.synthetics_mobile_step_params_element_context_type import (
    SyntheticsMobileStepParamsElementContextType,
)
from datadog_api_client.v1.model.synthetics_mobile_step_params_element_relative_position import (
    SyntheticsMobileStepParamsElementRelativePosition,
)
from datadog_api_client.v1.model.synthetics_mobile_step_params_element_user_locator import (
    SyntheticsMobileStepParamsElementUserLocator,
)
from datadog_api_client.v1.model.synthetics_mobile_step_params_element_user_locator_values_items import (
    SyntheticsMobileStepParamsElementUserLocatorValuesItems,
)
from datadog_api_client.v1.model.synthetics_mobile_step_params_element_user_locator_values_items_type import (
    SyntheticsMobileStepParamsElementUserLocatorValuesItemsType,
)
from datadog_api_client.v1.model.synthetics_mobile_step_params_positions_items import (
    SyntheticsMobileStepParamsPositionsItems,
)
from datadog_api_client.v1.model.synthetics_mobile_step_params_variable import SyntheticsMobileStepParamsVariable
from datadog_api_client.v1.model.synthetics_mobile_step_type import SyntheticsMobileStepType
from datadog_api_client.v1.model.synthetics_mobile_test import SyntheticsMobileTest
from datadog_api_client.v1.model.synthetics_mobile_test_config import SyntheticsMobileTestConfig
from datadog_api_client.v1.model.synthetics_mobile_test_options import SyntheticsMobileTestOptions
from datadog_api_client.v1.model.synthetics_mobile_test_type import SyntheticsMobileTestType
from datadog_api_client.v1.model.synthetics_mobile_tests_mobile_application import (
    SyntheticsMobileTestsMobileApplication,
)
from datadog_api_client.v1.model.synthetics_mobile_tests_mobile_application_reference_type import (
    SyntheticsMobileTestsMobileApplicationReferenceType,
)
from datadog_api_client.v1.model.synthetics_restricted_roles import SyntheticsRestrictedRoles
from datadog_api_client.v1.model.synthetics_test_ci_options import SyntheticsTestCiOptions
from datadog_api_client.v1.model.synthetics_test_execution_rule import SyntheticsTestExecutionRule
from datadog_api_client.v1.model.synthetics_test_options_monitor_options import SyntheticsTestOptionsMonitorOptions
from datadog_api_client.v1.model.synthetics_test_options_monitor_options_notification_preset_name import (
    SyntheticsTestOptionsMonitorOptionsNotificationPresetName,
)
from datadog_api_client.v1.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry
from datadog_api_client.v1.model.synthetics_test_options_scheduling import SyntheticsTestOptionsScheduling
from datadog_api_client.v1.model.synthetics_test_options_scheduling_timeframe import (
    SyntheticsTestOptionsSchedulingTimeframe,
)
from datadog_api_client.v1.model.synthetics_test_pause_status import SyntheticsTestPauseStatus
from datadog_api_client.v1.model.synthetics_test_restriction_policy_binding import (
    SyntheticsTestRestrictionPolicyBinding,
)
from datadog_api_client.v1.model.synthetics_test_restriction_policy_binding_relation import (
    SyntheticsTestRestrictionPolicyBindingRelation,
)

body = SyntheticsMobileTest(
    config=SyntheticsMobileTestConfig(
        variables=[
            SyntheticsConfigVariable(
                name="VARIABLE_NAME",
                secure=False,
                type=SyntheticsConfigVariableType.TEXT,
            ),
        ],
    ),
    device_ids=[
        "chrome.laptop_large",
    ],
    message="Notification message",
    name="Example test name",
    options=SyntheticsMobileTestOptions(
        bindings=[
            SyntheticsTestRestrictionPolicyBinding(
                principals=[],
                relation=SyntheticsTestRestrictionPolicyBindingRelation.EDITOR,
            ),
        ],
        ci=SyntheticsTestCiOptions(
            execution_rule=SyntheticsTestExecutionRule.BLOCKING,
        ),
        device_ids=[
            "synthetics:mobile:device:apple_ipad_10th_gen_2022_ios_16",
        ],
        mobile_application=SyntheticsMobileTestsMobileApplication(
            application_id="00000000-0000-0000-0000-aaaaaaaaaaaa",
            reference_id="00000000-0000-0000-0000-aaaaaaaaaaab",
            reference_type=SyntheticsMobileTestsMobileApplicationReferenceType.LATEST,
        ),
        monitor_options=SyntheticsTestOptionsMonitorOptions(
            notification_preset_name=SyntheticsTestOptionsMonitorOptionsNotificationPresetName.SHOW_ALL,
        ),
        restricted_roles=SyntheticsRestrictedRoles(
            [
                "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            ]
        ),
        retry=SyntheticsTestOptionsRetry(),
        scheduling=SyntheticsTestOptionsScheduling(
            timeframes=[
                SyntheticsTestOptionsSchedulingTimeframe(
                    day=1,
                    _from="07:00",
                    to="16:00",
                ),
                SyntheticsTestOptionsSchedulingTimeframe(
                    day=3,
                    _from="07:00",
                    to="16:00",
                ),
            ],
            timezone="America/New_York",
        ),
        tick_every=300,
    ),
    status=SyntheticsTestPauseStatus.LIVE,
    steps=[
        SyntheticsMobileStep(
            name="",
            params=SyntheticsMobileStepParams(
                check=SyntheticsCheckType.EQUALS,
                direction=SyntheticsMobileStepParamsDirection.UP,
                element=SyntheticsMobileStepParamsElement(
                    context_type=SyntheticsMobileStepParamsElementContextType.NATIVE,
                    relative_position=SyntheticsMobileStepParamsElementRelativePosition(),
                    user_locator=SyntheticsMobileStepParamsElementUserLocator(
                        values=[
                            SyntheticsMobileStepParamsElementUserLocatorValuesItems(
                                type=SyntheticsMobileStepParamsElementUserLocatorValuesItemsType.ACCESSIBILITY_ID,
                            ),
                        ],
                    ),
                ),
                positions=[
                    SyntheticsMobileStepParamsPositionsItems(),
                ],
                variable=SyntheticsMobileStepParamsVariable(
                    example="",
                    name="VAR_NAME",
                ),
            ),
            public_id="pub-lic-id0",
            type=SyntheticsMobileStepType.ASSERTELEMENTCONTENT,
        ),
    ],
    tags=[
        "env:production",
    ],
    type=SyntheticsMobileTestType.MOBILE,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.update_mobile_test(public_id="public_id", body=body)

    print(response)
