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


class CIAppHostInfo(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "hostname": (str,),
            "labels": ([str],),
            "name": (str,),
            "workspace": (str,),
        }

    attribute_map = {
        "hostname": "hostname",
        "labels": "labels",
        "name": "name",
        "workspace": "workspace",
    }

    def __init__(
        self_,
        hostname: Union[str, UnsetType] = unset,
        labels: Union[List[str], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        workspace: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Contains information of the host running the pipeline, stage, job, or step.

        :param hostname: FQDN of the host.
        :type hostname: str, optional

        :param labels: A list of labels used to select or identify the node.
        :type labels: [str], optional

        :param name: Name for the host.
        :type name: str, optional

        :param workspace: The path where the code is checked out.
        :type workspace: str, optional
        """
        if hostname is not unset:
            kwargs["hostname"] = hostname
        if labels is not unset:
            kwargs["labels"] = labels
        if name is not unset:
            kwargs["name"] = name
        if workspace is not unset:
            kwargs["workspace"] = workspace
        super().__init__(kwargs)
