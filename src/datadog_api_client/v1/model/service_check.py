# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ServiceCheck(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.service_check_status import ServiceCheckStatus

        return {
            "check": (str,),
            "host_name": (str,),
            "message": (str,),
            "status": (ServiceCheckStatus,),
            "tags": ([str],),
            "timestamp": (int,),
        }

    attribute_map = {
        "check": "check",
        "host_name": "host_name",
        "message": "message",
        "status": "status",
        "tags": "tags",
        "timestamp": "timestamp",
    }

    def __init__(self, check, host_name, status, tags, *args, **kwargs):
        """
        An object containing service check and status.

        :param check: The check.
        :type check: str

        :param host_name: The host name correlated with the check.
        :type host_name: str

        :param message: Message containing check status.
        :type message: str, optional

        :param status: The status of a service check.
        :type status: ServiceCheckStatus

        :param tags: Tags related to a check.
        :type tags: [str]

        :param timestamp: Time of check.
        :type timestamp: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.check = check
        self.host_name = host_name
        self.status = status
        self.tags = tags

    @classmethod
    def _from_openapi_data(cls, check, host_name, status, tags, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ServiceCheck, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.check = check
        self.host_name = host_name
        self.status = status
        self.tags = tags
        return self
