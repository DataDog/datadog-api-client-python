# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ProcessSummaryAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "cmdline": (str,),
            "executable": (str,),
            "host": (str,),
            "identifying_tags": ([str],),
            "pid": (int,),
            "ppid": (int,),
            "start": (str,),
            "tags": ([str],),
            "timestamp": (str,),
            "user": (str,),
        }

    attribute_map = {
        "cmdline": "cmdline",
        "executable": "executable",
        "host": "host",
        "identifying_tags": "identifying_tags",
        "pid": "pid",
        "ppid": "ppid",
        "start": "start",
        "tags": "tags",
        "timestamp": "timestamp",
        "user": "user",
    }

    def __init__(
        self_,
        cmdline: Union[str, UnsetType] = unset,
        executable: Union[str, UnsetType] = unset,
        host: Union[str, UnsetType] = unset,
        identifying_tags: Union[List[str], UnsetType] = unset,
        pid: Union[int, UnsetType] = unset,
        ppid: Union[int, UnsetType] = unset,
        start: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        timestamp: Union[str, UnsetType] = unset,
        user: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for a process summary.

        :param cmdline: Process command line.
        :type cmdline: str, optional

        :param executable: Path to the process executable.
        :type executable: str, optional

        :param host: Host running the process.
        :type host: str, optional

        :param identifying_tags: Tags that uniquely identify the process: a host identity tag ( ``host`` , ``task_arn`` ,
            or ``eks_fargate_node`` ) and a ``pid`` tag. Omitted if either tag is unavailable.
        :type identifying_tags: [str], optional

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
        if cmdline is not unset:
            kwargs["cmdline"] = cmdline
        if executable is not unset:
            kwargs["executable"] = executable
        if host is not unset:
            kwargs["host"] = host
        if identifying_tags is not unset:
            kwargs["identifying_tags"] = identifying_tags
        if pid is not unset:
            kwargs["pid"] = pid
        if ppid is not unset:
            kwargs["ppid"] = ppid
        if start is not unset:
            kwargs["start"] = start
        if tags is not unset:
            kwargs["tags"] = tags
        if timestamp is not unset:
            kwargs["timestamp"] = timestamp
        if user is not unset:
            kwargs["user"] = user
        super().__init__(kwargs)
