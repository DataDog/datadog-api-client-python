# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsTriggerCITestRunResult(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_device_id import SyntheticsDeviceID

        return {
            "device": (SyntheticsDeviceID,),
            "location": (int,),
            "public_id": (str,),
            "result_id": (str,),
        }

    attribute_map = {
        "device": "device",
        "location": "location",
        "public_id": "public_id",
        "result_id": "result_id",
    }

    def __init__(self, *args, **kwargs):
        """
        Information about a single test run.

        :param device: The device ID.
        :type device: SyntheticsDeviceID, optional

        :param location: The location ID of the test run.
        :type location: int, optional

        :param public_id: The public ID of the Synthetics test.
        :type public_id: str, optional

        :param result_id: ID of the result.
        :type result_id: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsTriggerCITestRunResult, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
