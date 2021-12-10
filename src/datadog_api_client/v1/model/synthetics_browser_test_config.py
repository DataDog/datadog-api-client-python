# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_assertion import SyntheticsAssertion
    from datadog_api_client.v1.model.synthetics_browser_variable import SyntheticsBrowserVariable
    from datadog_api_client.v1.model.synthetics_config_variable import SyntheticsConfigVariable
    from datadog_api_client.v1.model.synthetics_test_request import SyntheticsTestRequest

    globals()["SyntheticsAssertion"] = SyntheticsAssertion
    globals()["SyntheticsBrowserVariable"] = SyntheticsBrowserVariable
    globals()["SyntheticsConfigVariable"] = SyntheticsConfigVariable
    globals()["SyntheticsTestRequest"] = SyntheticsTestRequest


class SyntheticsBrowserTestConfig(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "assertions": ([SyntheticsAssertion],),
            "config_variables": ([SyntheticsConfigVariable],),
            "request": (SyntheticsTestRequest,),
            "set_cookie": (str,),
            "variables": ([SyntheticsBrowserVariable],),
        }

    attribute_map = {
        "assertions": "assertions",
        "request": "request",
        "config_variables": "configVariables",
        "set_cookie": "setCookie",
        "variables": "variables",
    }

    read_only_vars = {}

    def __init__(self, request, *args, **kwargs):
        """SyntheticsBrowserTestConfig - a model defined in OpenAPI

        Args:
            request (SyntheticsTestRequest):

        Keyword Args:
            assertions ([SyntheticsAssertion]): Array of assertions used for the test. Defaults to [].
            config_variables ([SyntheticsConfigVariable]): [optional] Array of variables used for the test.
            set_cookie (str): [optional] Cookies to be used for the request, using the [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie) syntax.
            variables ([SyntheticsBrowserVariable]): [optional] Array of variables used for the test steps.
        """
        super().__init__(kwargs)

        assertions = kwargs.get("assertions", [])

        self._check_pos_args(args)

        self.assertions = assertions
        self.request = request

    @classmethod
    def _from_openapi_data(cls, request, *args, **kwargs):
        """Helper creating a new instance from a response."""
        assertions = kwargs.get("assertions", [])

        self = super(SyntheticsBrowserTestConfig, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.assertions = assertions
        self.request = request
        return self
