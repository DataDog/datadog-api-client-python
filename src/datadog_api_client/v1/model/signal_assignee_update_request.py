# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SignalAssigneeUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "assignee": (str,),
            "version": (int,),
        }

    attribute_map = {
        "assignee": "assignee",
        "version": "version",
    }

    def __init__(self, assignee, *args, **kwargs):
        """
        Attributes describing an assignee update operation over a security signal.

        :param assignee: The UUID of the user being assigned. Use empty string to return signal to unassigned.
        :type assignee: str

        :param version: Version of the updated signal. If server side version is higher, update will be rejected.
        :type version: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.assignee = assignee

    @classmethod
    def _from_openapi_data(cls, assignee, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SignalAssigneeUpdateRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.assignee = assignee
        return self
