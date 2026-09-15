# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CloudWorkloadSecurityAgentRuleActionCoreDump(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "dentry": (bool,),
            "mount": (bool,),
            "no_compression": (bool,),
            "process": (bool,),
        }

    attribute_map = {
        "dentry": "dentry",
        "mount": "mount",
        "no_compression": "no_compression",
        "process": "process",
    }

    def __init__(
        self_,
        dentry: Union[bool, UnsetType] = unset,
        mount: Union[bool, UnsetType] = unset,
        no_compression: Union[bool, UnsetType] = unset,
        process: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        The core dump action applied on the process matching the rule.

        :param dentry: Whether the directory entry information is included in the core dump.
        :type dentry: bool, optional

        :param mount: Whether the mount information is included in the core dump.
        :type mount: bool, optional

        :param no_compression: Whether the core dump is left uncompressed.
        :type no_compression: bool, optional

        :param process: Whether the process memory is included in the core dump.
        :type process: bool, optional
        """
        if dentry is not unset:
            kwargs["dentry"] = dentry
        if mount is not unset:
            kwargs["mount"] = mount
        if no_compression is not unset:
            kwargs["no_compression"] = no_compression
        if process is not unset:
            kwargs["process"] = process
        super().__init__(kwargs)
