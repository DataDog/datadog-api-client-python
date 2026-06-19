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


class TestOptimizationServiceSettingsAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "auto_test_retries_enabled": (bool,),
            "auto_test_retries_enabled_is_overridden": (bool,),
            "code_coverage_enabled": (bool,),
            "code_coverage_enabled_is_overridden": (bool,),
            "early_flake_detection_enabled": (bool,),
            "early_flake_detection_enabled_is_overridden": (bool,),
            "env": (str,),
            "failed_test_replay_enabled": (bool,),
            "failed_test_replay_enabled_is_overridden": (bool,),
            "pr_comments_enabled": (bool,),
            "repository_id": (str,),
            "service_name": (str,),
            "test_impact_analysis_enabled": (bool,),
            "test_impact_analysis_enabled_is_overridden": (bool,),
        }

    attribute_map = {
        "auto_test_retries_enabled": "auto_test_retries_enabled",
        "auto_test_retries_enabled_is_overridden": "auto_test_retries_enabled_is_overridden",
        "code_coverage_enabled": "code_coverage_enabled",
        "code_coverage_enabled_is_overridden": "code_coverage_enabled_is_overridden",
        "early_flake_detection_enabled": "early_flake_detection_enabled",
        "early_flake_detection_enabled_is_overridden": "early_flake_detection_enabled_is_overridden",
        "env": "env",
        "failed_test_replay_enabled": "failed_test_replay_enabled",
        "failed_test_replay_enabled_is_overridden": "failed_test_replay_enabled_is_overridden",
        "pr_comments_enabled": "pr_comments_enabled",
        "repository_id": "repository_id",
        "service_name": "service_name",
        "test_impact_analysis_enabled": "test_impact_analysis_enabled",
        "test_impact_analysis_enabled_is_overridden": "test_impact_analysis_enabled_is_overridden",
    }

    def __init__(
        self_,
        auto_test_retries_enabled: Union[bool, UnsetType] = unset,
        auto_test_retries_enabled_is_overridden: Union[bool, UnsetType] = unset,
        code_coverage_enabled: Union[bool, UnsetType] = unset,
        code_coverage_enabled_is_overridden: Union[bool, UnsetType] = unset,
        early_flake_detection_enabled: Union[bool, UnsetType] = unset,
        early_flake_detection_enabled_is_overridden: Union[bool, UnsetType] = unset,
        env: Union[str, UnsetType] = unset,
        failed_test_replay_enabled: Union[bool, UnsetType] = unset,
        failed_test_replay_enabled_is_overridden: Union[bool, UnsetType] = unset,
        pr_comments_enabled: Union[bool, UnsetType] = unset,
        repository_id: Union[str, UnsetType] = unset,
        service_name: Union[str, UnsetType] = unset,
        test_impact_analysis_enabled: Union[bool, UnsetType] = unset,
        test_impact_analysis_enabled_is_overridden: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for Test Optimization service settings.

        :param auto_test_retries_enabled: Whether Auto Test Retries are enabled for this service.
        :type auto_test_retries_enabled: bool, optional

        :param auto_test_retries_enabled_is_overridden: Whether the Auto Test Retries setting is overridden at the service level.
        :type auto_test_retries_enabled_is_overridden: bool, optional

        :param code_coverage_enabled: Whether Code Coverage is enabled for this service.
        :type code_coverage_enabled: bool, optional

        :param code_coverage_enabled_is_overridden: Whether the Code Coverage setting is overridden at the service level.
        :type code_coverage_enabled_is_overridden: bool, optional

        :param early_flake_detection_enabled: Whether Early Flake Detection is enabled for this service.
        :type early_flake_detection_enabled: bool, optional

        :param early_flake_detection_enabled_is_overridden: Whether the Early Flake Detection setting is overridden at the service level.
        :type early_flake_detection_enabled_is_overridden: bool, optional

        :param env: The environment name.
        :type env: str, optional

        :param failed_test_replay_enabled: Whether Failed Test Replay is enabled for this service.
        :type failed_test_replay_enabled: bool, optional

        :param failed_test_replay_enabled_is_overridden: Whether the Failed Test Replay setting is overridden at the service level.
        :type failed_test_replay_enabled_is_overridden: bool, optional

        :param pr_comments_enabled: Whether PR Comments are enabled. This value reflects the repository-level setting and cannot be overridden at the service level.
        :type pr_comments_enabled: bool, optional

        :param repository_id: The repository identifier.
        :type repository_id: str, optional

        :param service_name: The service name.
        :type service_name: str, optional

        :param test_impact_analysis_enabled: Whether Test Impact Analysis is enabled for this service.
        :type test_impact_analysis_enabled: bool, optional

        :param test_impact_analysis_enabled_is_overridden: Whether the Test Impact Analysis setting is overridden at the service level.
        :type test_impact_analysis_enabled_is_overridden: bool, optional
        """
        if auto_test_retries_enabled is not unset:
            kwargs["auto_test_retries_enabled"] = auto_test_retries_enabled
        if auto_test_retries_enabled_is_overridden is not unset:
            kwargs["auto_test_retries_enabled_is_overridden"] = auto_test_retries_enabled_is_overridden
        if code_coverage_enabled is not unset:
            kwargs["code_coverage_enabled"] = code_coverage_enabled
        if code_coverage_enabled_is_overridden is not unset:
            kwargs["code_coverage_enabled_is_overridden"] = code_coverage_enabled_is_overridden
        if early_flake_detection_enabled is not unset:
            kwargs["early_flake_detection_enabled"] = early_flake_detection_enabled
        if early_flake_detection_enabled_is_overridden is not unset:
            kwargs["early_flake_detection_enabled_is_overridden"] = early_flake_detection_enabled_is_overridden
        if env is not unset:
            kwargs["env"] = env
        if failed_test_replay_enabled is not unset:
            kwargs["failed_test_replay_enabled"] = failed_test_replay_enabled
        if failed_test_replay_enabled_is_overridden is not unset:
            kwargs["failed_test_replay_enabled_is_overridden"] = failed_test_replay_enabled_is_overridden
        if pr_comments_enabled is not unset:
            kwargs["pr_comments_enabled"] = pr_comments_enabled
        if repository_id is not unset:
            kwargs["repository_id"] = repository_id
        if service_name is not unset:
            kwargs["service_name"] = service_name
        if test_impact_analysis_enabled is not unset:
            kwargs["test_impact_analysis_enabled"] = test_impact_analysis_enabled
        if test_impact_analysis_enabled_is_overridden is not unset:
            kwargs["test_impact_analysis_enabled_is_overridden"] = test_impact_analysis_enabled_is_overridden
        super().__init__(kwargs)
