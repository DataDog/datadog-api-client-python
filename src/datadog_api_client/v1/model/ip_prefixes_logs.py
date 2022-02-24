# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class IPPrefixesLogs(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "prefixes_ipv4": ([str],),
            "prefixes_ipv6": ([str],),
        }

    attribute_map = {
        "prefixes_ipv4": "prefixes_ipv4",
        "prefixes_ipv6": "prefixes_ipv6",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Available prefix information for the Logs endpoints.

        :param prefixes_ipv4: List of IPv4 prefixes.
        :type prefixes_ipv4: [str], optional

        :param prefixes_ipv6: List of IPv6 prefixes.
        :type prefixes_ipv6: [str], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IPPrefixesLogs, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
