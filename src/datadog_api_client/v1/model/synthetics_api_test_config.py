# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.synthetics_assertion import SyntheticsAssertion
    from datadog_api_client.v1.model.synthetics_config_variable import SyntheticsConfigVariable
    from datadog_api_client.v1.model.synthetics_test_request import SyntheticsTestRequest
    from datadog_api_client.v1.model.synthetics_api_step import SyntheticsAPIStep
    from datadog_api_client.v1.model.synthetics_assertion_target import SyntheticsAssertionTarget
    from datadog_api_client.v1.model.synthetics_assertion_body_hash_target import SyntheticsAssertionBodyHashTarget
    from datadog_api_client.v1.model.synthetics_assertion_json_path_target import SyntheticsAssertionJSONPathTarget
    from datadog_api_client.v1.model.synthetics_assertion_json_schema_target import SyntheticsAssertionJSONSchemaTarget
    from datadog_api_client.v1.model.synthetics_assertion_x_path_target import SyntheticsAssertionXPathTarget
    from datadog_api_client.v1.model.synthetics_api_test_step import SyntheticsAPITestStep
    from datadog_api_client.v1.model.synthetics_api_wait_step import SyntheticsAPIWaitStep


class SyntheticsAPITestConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_assertion import SyntheticsAssertion
        from datadog_api_client.v1.model.synthetics_config_variable import SyntheticsConfigVariable
        from datadog_api_client.v1.model.synthetics_test_request import SyntheticsTestRequest
        from datadog_api_client.v1.model.synthetics_api_step import SyntheticsAPIStep

        return {
            "assertions": ([SyntheticsAssertion],),
            "config_variables": ([SyntheticsConfigVariable],),
            "request": (SyntheticsTestRequest,),
            "steps": ([SyntheticsAPIStep],),
            "variables_from_script": (str,),
        }

    attribute_map = {
        "assertions": "assertions",
        "config_variables": "configVariables",
        "request": "request",
        "steps": "steps",
        "variables_from_script": "variablesFromScript",
    }

    def __init__(
        self_,
        assertions: Union[
            List[
                Union[
                    SyntheticsAssertion,
                    SyntheticsAssertionTarget,
                    SyntheticsAssertionBodyHashTarget,
                    SyntheticsAssertionJSONPathTarget,
                    SyntheticsAssertionJSONSchemaTarget,
                    SyntheticsAssertionXPathTarget,
                ]
            ],
            UnsetType,
        ] = unset,
        config_variables: Union[List[SyntheticsConfigVariable], UnsetType] = unset,
        request: Union[SyntheticsTestRequest, UnsetType] = unset,
        steps: Union[List[Union[SyntheticsAPIStep, SyntheticsAPITestStep, SyntheticsAPIWaitStep]], UnsetType] = unset,
        variables_from_script: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration object for a Synthetic API test.

        :param assertions: Array of assertions used for the test. Required for single API tests.
        :type assertions: [SyntheticsAssertion], optional

        :param config_variables: Array of variables used for the test.
        :type config_variables: [SyntheticsConfigVariable], optional

        :param request: Object describing the Synthetic test request.
        :type request: SyntheticsTestRequest, optional

        :param steps: When the test subtype is ``multi`` , the steps of the test.
        :type steps: [SyntheticsAPIStep], optional

        :param variables_from_script: Variables defined from JavaScript code.
        :type variables_from_script: str, optional
        """
        if assertions is not unset:
            kwargs["assertions"] = assertions
        if config_variables is not unset:
            kwargs["config_variables"] = config_variables
        if request is not unset:
            kwargs["request"] = request
        if steps is not unset:
            kwargs["steps"] = steps
        if variables_from_script is not unset:
            kwargs["variables_from_script"] = variables_from_script
        super().__init__(kwargs)
