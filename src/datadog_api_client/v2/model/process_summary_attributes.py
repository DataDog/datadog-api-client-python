# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ProcessSummaryAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "cmdline": (str,),
            "host": (str,),
            "pid": (int,),
            "ppid": (int,),
            "start": (str,),
            "tags": ([str],),
            "timestamp": (str,),
            "user": (str,),
        }

    attribute_map = {
        "cmdline": "cmdline",
        "host": "host",
        "pid": "pid",
        "ppid": "ppid",
        "start": "start",
        "tags": "tags",
        "timestamp": "timestamp",
        "user": "user",
    }

    def __init__(self, *args, **kwargs):
        """
        Attributes for a process summary.

        :param cmdline: Process command line.
        :type cmdline: str, optional

        :param host: Host running the process.
        :type host: str, optional

        :param pid: Process ID.
        :type pid: int, optional

        :param ppid: Parent process ID.
        :type ppid: int, optional

        :param start: Time the process was started.
        :type start: str, optional

        :param tags: List of tags associated with the process.
        :type tags: [str], optional

        :param timestamp: Time the process was seen.
        :type timestamp: str, optional

        :param user: Process owner.
        :type user: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ProcessSummaryAttributes, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
