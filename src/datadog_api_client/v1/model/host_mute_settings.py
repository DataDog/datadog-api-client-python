# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class HostMuteSettings(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "end": (int,),
            "message": (str,),
            "override": (bool,),
        }

    attribute_map = {
        "end": "end",
        "message": "message",
        "override": "override",
    }

    def __init__(self, *args, **kwargs):
        """
        Combination of settings to mute a host.

        :param end: POSIX timestamp in seconds when the host is unmuted. If omitted, the host remains muted until explicitly unmuted.
        :type end: int, optional

        :param message: Message to associate with the muting of this host.
        :type message: str, optional

        :param override: If true and the host is already muted, replaces existing host mute settings.
        :type override: bool, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(HostMuteSettings, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
