# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.synthetics_browser_test_failure_code import SyntheticsBrowserTestFailureCode

    globals()["SyntheticsBrowserTestFailureCode"] = SyntheticsBrowserTestFailureCode


class SyntheticsBrowserTestResultFailure(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    validations = {}

    @cached_property
    def openapi_types():
        lazy_import()
        return {
            "code": (SyntheticsBrowserTestFailureCode,),
            "message": (str,),
        }

    attribute_map = {
        "code": "code",
        "message": "message",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """SyntheticsBrowserTestResultFailure - a model defined in OpenAPI


        :type code: SyntheticsBrowserTestFailureCode, optional

        :param message: The browser test error message.
        :type message: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsBrowserTestResultFailure, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
