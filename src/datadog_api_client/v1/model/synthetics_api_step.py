# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class SyntheticsAPIStep(ModelComposed):
    def __init__(self, **kwargs):
        """
        The steps used in a Synthetic multi-step API test.

        :param allow_failure: Determines whether or not to continue with test if this step fails.
        :type allow_failure: bool, optional

        :param assertions: Array of assertions used for the test.
        :type assertions: [SyntheticsAssertion]

        :param extracted_values: Array of values to parse and save as variables from the response.
        :type extracted_values: [SyntheticsParsingOptions], optional

        :param is_critical: Determines whether or not to consider the entire test as failed if this step fails.
            Can be used only if `allowFailure` is `true`.
        :type is_critical: bool, optional

        :param name: The name of the step.
        :type name: str

        :param request: Object describing the Synthetic test request.
        :type request: SyntheticsTestRequest

        :param retry: Object describing the retry strategy to apply to a Synthetic test.
        :type retry: SyntheticsTestOptionsRetry, optional

        :param subtype: The subtype of the Synthetic multi-step API test step.
        :type subtype: SyntheticsAPITestStepSubtype

        :param value: The time to wait in seconds. Minimum value: 0. Maximum value: 180.
        :type value: int
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1.model.synthetics_api_test_step import SyntheticsAPITestStep
        from datadog_api_client.v1.model.synthetics_api_wait_step import SyntheticsAPIWaitStep

        return {
            "oneOf": [
                SyntheticsAPITestStep,
                SyntheticsAPIWaitStep,
            ],
        }
