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


class FleetConfigurationLayer(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "compiled_configuration": (str,),
            "env_configuration": (str,),
            "file_configuration": (str,),
            "parsed_configuration": (str,),
            "remote_configuration": (str,),
            "runtime_configuration": (str,),
        }

    attribute_map = {
        "compiled_configuration": "compiled_configuration",
        "env_configuration": "env_configuration",
        "file_configuration": "file_configuration",
        "parsed_configuration": "parsed_configuration",
        "remote_configuration": "remote_configuration",
        "runtime_configuration": "runtime_configuration",
    }

    def __init__(
        self_,
        compiled_configuration: Union[str, UnsetType] = unset,
        env_configuration: Union[str, UnsetType] = unset,
        file_configuration: Union[str, UnsetType] = unset,
        parsed_configuration: Union[str, UnsetType] = unset,
        remote_configuration: Union[str, UnsetType] = unset,
        runtime_configuration: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Configuration information organized by layers.

        :param compiled_configuration: The final compiled configuration.
        :type compiled_configuration: str, optional

        :param env_configuration: Configuration from environment variables.
        :type env_configuration: str, optional

        :param file_configuration: Configuration from files.
        :type file_configuration: str, optional

        :param parsed_configuration: Parsed configuration output.
        :type parsed_configuration: str, optional

        :param remote_configuration: Remote configuration settings.
        :type remote_configuration: str, optional

        :param runtime_configuration: Runtime configuration.
        :type runtime_configuration: str, optional
        """
        if compiled_configuration is not unset:
            kwargs["compiled_configuration"] = compiled_configuration
        if env_configuration is not unset:
            kwargs["env_configuration"] = env_configuration
        if file_configuration is not unset:
            kwargs["file_configuration"] = file_configuration
        if parsed_configuration is not unset:
            kwargs["parsed_configuration"] = parsed_configuration
        if remote_configuration is not unset:
            kwargs["remote_configuration"] = remote_configuration
        if runtime_configuration is not unset:
            kwargs["runtime_configuration"] = runtime_configuration
        super().__init__(kwargs)
