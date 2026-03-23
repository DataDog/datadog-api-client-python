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


class TestOptimizationUpdateServiceSettingsRequestAttributes(ModelNormal):
    validations = {
        "repository_id": {
            "min_length": 1,
        },
        "service_name": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "auto_test_retries_enabled": (bool,),
            "code_coverage_enabled": (bool,),
            "early_flake_detection_enabled": (bool,),
            "env": (str,),
            "failed_test_replay_enabled": (bool,),
            "pr_comments_enabled": (bool,),
            "repository_id": (str,),
            "service_name": (str,),
            "test_impact_analysis_enabled": (bool,),
        }

    attribute_map = {
        "auto_test_retries_enabled": "auto_test_retries_enabled",
        "code_coverage_enabled": "code_coverage_enabled",
        "early_flake_detection_enabled": "early_flake_detection_enabled",
        "env": "env",
        "failed_test_replay_enabled": "failed_test_replay_enabled",
        "pr_comments_enabled": "pr_comments_enabled",
        "repository_id": "repository_id",
        "service_name": "service_name",
        "test_impact_analysis_enabled": "test_impact_analysis_enabled",
    }

    def __init__(
        self_,
        repository_id: str,
        service_name: str,
        auto_test_retries_enabled: Union[bool, UnsetType] = unset,
        code_coverage_enabled: Union[bool, UnsetType] = unset,
        early_flake_detection_enabled: Union[bool, UnsetType] = unset,
        env: Union[str, UnsetType] = unset,
        failed_test_replay_enabled: Union[bool, UnsetType] = unset,
        pr_comments_enabled: Union[bool, UnsetType] = unset,
        test_impact_analysis_enabled: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating Test Optimization service settings.
        All non-required fields are optional; only provided fields will be updated.

        :param auto_test_retries_enabled: Whether Auto Test Retries are enabled for this service.
        :type auto_test_retries_enabled: bool, optional

        :param code_coverage_enabled: Whether Code Coverage is enabled for this service.
        :type code_coverage_enabled: bool, optional

        :param early_flake_detection_enabled: Whether Early Flake Detection is enabled for this service.
        :type early_flake_detection_enabled: bool, optional

        :param env: The environment name. If omitted, defaults to ``none``.
        :type env: str, optional

        :param failed_test_replay_enabled: Whether Failed Test Replay is enabled for this service.
        :type failed_test_replay_enabled: bool, optional

        :param pr_comments_enabled: Whether PR Comments are enabled for this service.
        :type pr_comments_enabled: bool, optional

        :param repository_id: The repository identifier.
        :type repository_id: str

        :param service_name: The service name.
        :type service_name: str

        :param test_impact_analysis_enabled: Whether Test Impact Analysis is enabled for this service.
        :type test_impact_analysis_enabled: bool, optional
        """
        if auto_test_retries_enabled is not unset:
            kwargs["auto_test_retries_enabled"] = auto_test_retries_enabled
        if code_coverage_enabled is not unset:
            kwargs["code_coverage_enabled"] = code_coverage_enabled
        if early_flake_detection_enabled is not unset:
            kwargs["early_flake_detection_enabled"] = early_flake_detection_enabled
        if env is not unset:
            kwargs["env"] = env
        if failed_test_replay_enabled is not unset:
            kwargs["failed_test_replay_enabled"] = failed_test_replay_enabled
        if pr_comments_enabled is not unset:
            kwargs["pr_comments_enabled"] = pr_comments_enabled
        if test_impact_analysis_enabled is not unset:
            kwargs["test_impact_analysis_enabled"] = test_impact_analysis_enabled
        super().__init__(kwargs)

        self_.repository_id = repository_id
        self_.service_name = service_name
