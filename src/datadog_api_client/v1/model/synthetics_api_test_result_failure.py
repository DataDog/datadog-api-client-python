# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsApiTestResultFailure(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_api_test_failure_code import SyntheticsApiTestFailureCode

        return {
            "code": (SyntheticsApiTestFailureCode,),
            "message": (str,),
        }

    attribute_map = {
        "code": "code",
        "message": "message",
    }

    def __init__(self, *args, **kwargs):
        """
        The API test failure details.

        :param code: Error code that can be returned by a Synthetic test.
        :type code: SyntheticsApiTestFailureCode, optional

        :param message: The API test error message.
        :type message: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsApiTestResultFailure, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
