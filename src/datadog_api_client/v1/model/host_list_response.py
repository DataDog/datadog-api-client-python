# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class HostListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.host import Host

        return {
            "host_list": ([Host],),
            "total_matching": (int,),
            "total_returned": (int,),
        }

    attribute_map = {
        "host_list": "host_list",
        "total_matching": "total_matching",
        "total_returned": "total_returned",
    }

    def __init__(self, *args, **kwargs):
        """
        Response with Host information from Datadog.

        :param host_list: Array of hosts.
        :type host_list: [Host], optional

        :param total_matching: Number of host matching the query.
        :type total_matching: int, optional

        :param total_returned: Number of host returned.
        :type total_returned: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(HostListResponse, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
