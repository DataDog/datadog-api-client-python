# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsTiming(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "dns": (float,),
            "download": (float,),
            "first_byte": (float,),
            "handshake": (float,),
            "redirect": (float,),
            "ssl": (float,),
            "tcp": (float,),
            "total": (float,),
            "wait": (float,),
        }

    attribute_map = {
        "dns": "dns",
        "download": "download",
        "first_byte": "firstByte",
        "handshake": "handshake",
        "redirect": "redirect",
        "ssl": "ssl",
        "tcp": "tcp",
        "total": "total",
        "wait": "wait",
    }

    def __init__(self, *args, **kwargs):
        """
        Object containing all metrics and their values collected for a Synthetic API test.
        Learn more about those metrics in `Synthetics documentation <https://docs.datadoghq.com/synthetics/#metrics>`_.

        :param dns: The duration in millisecond of the DNS lookup.
        :type dns: float, optional

        :param download: The time in millisecond to download the response.
        :type download: float, optional

        :param first_byte: The time in millisecond to first byte.
        :type first_byte: float, optional

        :param handshake: The duration in millisecond of the TLS handshake.
        :type handshake: float, optional

        :param redirect: The time in millisecond spent during redirections.
        :type redirect: float, optional

        :param ssl: The duration in millisecond of the TLS handshake.
        :type ssl: float, optional

        :param tcp: Time in millisecond to establish the TCP connection.
        :type tcp: float, optional

        :param total: The overall time in millisecond the request took to be processed.
        :type total: float, optional

        :param wait: Time spent in millisecond waiting for a response.
        :type wait: float, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsTiming, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
