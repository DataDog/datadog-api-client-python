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


class FleetConfigurationFileV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "agent_hash": (str,),
            "file_content": (str,),
            "file_path": (str,),
            "filename": (str,),
            "fleet_hash": (str,),
        }

    attribute_map = {
        "agent_hash": "agent_hash",
        "file_content": "file_content",
        "file_path": "file_path",
        "filename": "filename",
        "fleet_hash": "fleet_hash",
    }

    def __init__(
        self_,
        agent_hash: Union[str, UnsetType] = unset,
        file_content: Union[str, UnsetType] = unset,
        file_path: Union[str, UnsetType] = unset,
        filename: Union[str, UnsetType] = unset,
        fleet_hash: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A configuration file for an integration.

        :param agent_hash: Hash of the configuration file as seen by the agent.
        :type agent_hash: str, optional

        :param file_content: The raw content of the configuration file.
        :type file_content: str, optional

        :param file_path: Path to the configuration file.
        :type file_path: str, optional

        :param filename: Name of the configuration file.
        :type filename: str, optional

        :param fleet_hash: Hash of the configuration file as applied by fleet management.
        :type fleet_hash: str, optional
        """
        if agent_hash is not unset:
            kwargs["agent_hash"] = agent_hash
        if file_content is not unset:
            kwargs["file_content"] = file_content
        if file_path is not unset:
            kwargs["file_path"] = file_path
        if filename is not unset:
            kwargs["filename"] = filename
        if fleet_hash is not unset:
            kwargs["fleet_hash"] = fleet_hash
        super().__init__(kwargs)
