# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class HostMuteResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "action": (str,),
            "end": (int,),
            "hostname": (str,),
            "message": (str,),
        }

    attribute_map = {
        "action": "action",
        "end": "end",
        "hostname": "hostname",
        "message": "message",
    }

    def __init__(self, *args, **kwargs):
        """
        Response with the list of muted host for your organization.

        :param action: Action applied to the hosts.
        :type action: str, optional

        :param end: POSIX timestamp in seconds when the host is unmuted.
        :type end: int, optional

        :param hostname: The host name.
        :type hostname: str, optional

        :param message: Message associated with the mute.
        :type message: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(HostMuteResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
