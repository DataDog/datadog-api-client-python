# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsBatchResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_device_id import SyntheticsDeviceID
        from datadog_api_client.v1.model.synthetics_test_execution_rule import SyntheticsTestExecutionRule
        from datadog_api_client.v1.model.synthetics_status import SyntheticsStatus
        from datadog_api_client.v1.model.synthetics_test_details_type import SyntheticsTestDetailsType

        return {
            "device": (SyntheticsDeviceID,),
            "duration": (float,),
            "execution_rule": (SyntheticsTestExecutionRule,),
            "location": (str,),
            "result_id": (str,),
            "retries": (float,),
            "status": (SyntheticsStatus,),
            "test_name": (str,),
            "test_public_id": (str,),
            "test_type": (SyntheticsTestDetailsType,),
        }

    attribute_map = {
        "device": "device",
        "duration": "duration",
        "execution_rule": "execution_rule",
        "location": "location",
        "result_id": "result_id",
        "retries": "retries",
        "status": "status",
        "test_name": "test_name",
        "test_public_id": "test_public_id",
        "test_type": "test_type",
    }

    def __init__(self, *args, **kwargs):
        """
        Object with the results of a Synthetics batch.

        :param device: The device ID.
        :type device: SyntheticsDeviceID, optional

        :param duration: Total duration in millisecond of the test.
        :type duration: float, optional

        :param execution_rule: Execution rule for a Synthetics test.
        :type execution_rule: SyntheticsTestExecutionRule, optional

        :param location: Name of the location.
        :type location: str, optional

        :param result_id: The ID of the result to get.
        :type result_id: str, optional

        :param retries: Number of times this result has been retried.
        :type retries: float, optional

        :param status: Determines whether or not the batch has passed, failed, or is in progress.
        :type status: SyntheticsStatus, optional

        :param test_name: Name of the test.
        :type test_name: str, optional

        :param test_public_id: The public ID of the Synthetic test.
        :type test_public_id: str, optional

        :param test_type: Type of the Synthetic test, either ``api`` or ``browser``.
        :type test_type: SyntheticsTestDetailsType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsBatchResult, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
