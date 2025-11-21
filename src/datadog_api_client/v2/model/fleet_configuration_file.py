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


class FleetConfigurationFile(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "file_content": (str,),
            "file_path": (str,),
            "filename": (str,),
        }

    attribute_map = {
        "file_content": "file_content",
        "file_path": "file_path",
        "filename": "filename",
    }

    def __init__(
        self_,
        file_content: Union[str, UnsetType] = unset,
        file_path: Union[str, UnsetType] = unset,
        filename: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A configuration file for an integration.

        :param file_content: The raw content of the configuration file.
        :type file_content: str, optional

        :param file_path: Path to the configuration file.
        :type file_path: str, optional

        :param filename: Name of the configuration file.
        :type filename: str, optional
        """
        if file_content is not unset:
            kwargs["file_content"] = file_content
        if file_path is not unset:
            kwargs["file_path"] = file_path
        if filename is not unset:
            kwargs["filename"] = filename
        super().__init__(kwargs)
