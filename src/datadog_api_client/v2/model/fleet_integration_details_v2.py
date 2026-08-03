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


class FleetIntegrationDetailsV2(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "data_type": (str,),
            "error_messages": ([str],),
            "init_config": (str,),
            "instance_config": (str,),
            "is_custom_check": (bool,),
            "is_default": (bool,),
            "is_init": (bool,),
            "log_config": (str,),
            "name": (str,),
            "pod_count": (int,),
            "source_index": (int,),
            "source_path": (str,),
            "type": (str,),
        }

    attribute_map = {
        "data_type": "data_type",
        "error_messages": "error_messages",
        "init_config": "init_config",
        "instance_config": "instance_config",
        "is_custom_check": "is_custom_check",
        "is_default": "is_default",
        "is_init": "is_init",
        "log_config": "log_config",
        "name": "name",
        "pod_count": "pod_count",
        "source_index": "source_index",
        "source_path": "source_path",
        "type": "type",
    }

    def __init__(
        self_,
        data_type: Union[str, UnsetType] = unset,
        error_messages: Union[List[str], UnsetType] = unset,
        init_config: Union[str, UnsetType] = unset,
        instance_config: Union[str, UnsetType] = unset,
        is_custom_check: Union[bool, UnsetType] = unset,
        is_default: Union[bool, UnsetType] = unset,
        is_init: Union[bool, UnsetType] = unset,
        log_config: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        pod_count: Union[int, UnsetType] = unset,
        source_index: Union[int, UnsetType] = unset,
        source_path: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Detailed information about a single integration.

        :param data_type: Type of data collected, such as metrics or logs.
        :type data_type: str, optional

        :param error_messages: Error messages if the integration has issues.
        :type error_messages: [str], optional

        :param init_config: Initialization configuration (YAML format).
        :type init_config: str, optional

        :param instance_config: Instance-specific configuration (YAML format).
        :type instance_config: str, optional

        :param is_custom_check: Whether this is a custom integration.
        :type is_custom_check: bool, optional

        :param is_default: Whether this is a default integration instance.
        :type is_default: bool, optional

        :param is_init: Whether this integration configuration is an init config.
        :type is_init: bool, optional

        :param log_config: Log collection configuration (YAML format).
        :type log_config: str, optional

        :param name: Name of the integration instance.
        :type name: str, optional

        :param pod_count: Number of pods running this integration. Absent from the response when the count is zero.
        :type pod_count: int, optional

        :param source_index: Index in the configuration file.
        :type source_index: int, optional

        :param source_path: Path to the configuration file.
        :type source_path: str, optional

        :param type: Integration type.
        :type type: str, optional
        """
        if data_type is not unset:
            kwargs["data_type"] = data_type
        if error_messages is not unset:
            kwargs["error_messages"] = error_messages
        if init_config is not unset:
            kwargs["init_config"] = init_config
        if instance_config is not unset:
            kwargs["instance_config"] = instance_config
        if is_custom_check is not unset:
            kwargs["is_custom_check"] = is_custom_check
        if is_default is not unset:
            kwargs["is_default"] = is_default
        if is_init is not unset:
            kwargs["is_init"] = is_init
        if log_config is not unset:
            kwargs["log_config"] = log_config
        if name is not unset:
            kwargs["name"] = name
        if pod_count is not unset:
            kwargs["pod_count"] = pod_count
        if source_index is not unset:
            kwargs["source_index"] = source_index
        if source_path is not unset:
            kwargs["source_path"] = source_path
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
