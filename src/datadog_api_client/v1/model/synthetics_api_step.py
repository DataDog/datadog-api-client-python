# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_api_step_subtype import SyntheticsAPIStepSubtype
    from datadog_api_client.v1.model.synthetics_assertion import SyntheticsAssertion
    from datadog_api_client.v1.model.synthetics_parsing_options import SyntheticsParsingOptions
    from datadog_api_client.v1.model.synthetics_test_options_retry import SyntheticsTestOptionsRetry
    from datadog_api_client.v1.model.synthetics_test_request import SyntheticsTestRequest

    globals()["SyntheticsAPIStepSubtype"] = SyntheticsAPIStepSubtype
    globals()["SyntheticsAssertion"] = SyntheticsAssertion
    globals()["SyntheticsParsingOptions"] = SyntheticsParsingOptions
    globals()["SyntheticsTestOptionsRetry"] = SyntheticsTestOptionsRetry
    globals()["SyntheticsTestRequest"] = SyntheticsTestRequest


class SyntheticsAPIStep(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
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

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """SyntheticsAPIStep - a model defined in OpenAPI

        Keyword Args:
            allow_failure (bool): [optional] Determines whether or not to continue with test if this step fails.
            assertions ([SyntheticsAssertion]): [optional] Array of assertions used for the test. If omitted the server will use the default value of [].
            extracted_values ([SyntheticsParsingOptions]): [optional] Array of values to parse and save as variables from the response.
            is_critical (bool): [optional] Determines whether or not to consider the entire test as failed if this step fails. Can be used only if `allowFailure` is `true`.
            name (str): [optional] The name of the step.
            request (SyntheticsTestRequest): [optional]
            retry (SyntheticsTestOptionsRetry): [optional]
            subtype (SyntheticsAPIStepSubtype): [optional]
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsAPIStep, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
