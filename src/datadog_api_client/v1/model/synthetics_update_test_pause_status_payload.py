# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsUpdateTestPauseStatusPayload(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_test_pause_status import SyntheticsTestPauseStatus

        return {
            "new_status": (SyntheticsTestPauseStatus,),
        }

    attribute_map = {
        "new_status": "new_status",
    }

    def __init__(self, *args, **kwargs):
        """
        Object to start or pause an existing Synthetic test.

        :param new_status: Define whether you want to start ( ``live`` ) or pause ( ``paused`` ) a
            Synthetic test.
        :type new_status: SyntheticsTestPauseStatus, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsUpdateTestPauseStatusPayload, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
