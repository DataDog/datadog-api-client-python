# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsAPIStep(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_assertion import SyntheticsAssertion
        from datadog_api_client.v1.model.synthetics_parsing_options import SyntheticsParsingOptions
        from datadog_api_client.v1.model.synthetics_test_request import SyntheticsTestRequest
        from datadog_api_client.v1.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry
        from datadog_api_client.v1.model.synthetics_api_step_subtype import SyntheticsAPIStepSubtype

        return {
            "allow_failure": (bool,),
            "assertions": ([SyntheticsAssertion],),
            "extracted_values": ([SyntheticsParsingOptions],),
            "is_critical": (bool,),
            "name": (str,),
            "request": (SyntheticsTestRequest,),
            "retry": (SyntheticsTestOptionsRetry,),
            "subtype": (SyntheticsAPIStepSubtype,),
        }

    attribute_map = {
        "allow_failure": "allowFailure",
        "assertions": "assertions",
        "extracted_values": "extractedValues",
        "is_critical": "isCritical",
        "name": "name",
        "request": "request",
        "retry": "retry",
        "subtype": "subtype",
    }

    def __init__(self_, name, request, subtype, *args, **kwargs):
        """
        The steps used in a Synthetics multistep API test.

        :param allow_failure: Determines whether or not to continue with test if this step fails.
        :type allow_failure: bool, optional

        :param assertions: Array of assertions used for the test.
        :type assertions: [SyntheticsAssertion]

        :param extracted_values: Array of values to parse and save as variables from the response.
        :type extracted_values: [SyntheticsParsingOptions], optional

        :param is_critical: Determines whether or not to consider the entire test as failed if this step fails.
            Can be used only if ``allowFailure`` is ``true``.
        :type is_critical: bool, optional

        :param name: The name of the step.
        :type name: str

        :param request: Object describing the Synthetic test request.
        :type request: SyntheticsTestRequest

        :param retry: Object describing the retry strategy to apply to a Synthetic test.
        :type retry: SyntheticsTestOptionsRetry, optional

        :param subtype: The subtype of the Synthetic multistep API test step, currently only supporting ``http``.
        :type subtype: SyntheticsAPIStepSubtype
        """
        super().__init__(kwargs)
        assertions = kwargs.get("assertions", [])

        self_._check_pos_args(args)

        self_.assertions = assertions
        self_.name = name
        self_.request = request
        self_.subtype = subtype
