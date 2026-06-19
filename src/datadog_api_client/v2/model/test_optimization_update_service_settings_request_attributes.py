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
            "auto_test_retries_enabled_inherit": (bool,),
            "code_coverage_enabled": (bool,),
            "code_coverage_enabled_inherit": (bool,),
            "early_flake_detection_enabled": (bool,),
            "early_flake_detection_enabled_inherit": (bool,),
            "env": (str,),
            "failed_test_replay_enabled": (bool,),
            "failed_test_replay_enabled_inherit": (bool,),
            "pr_comments_enabled": (bool,),
            "repository_id": (str,),
            "service_name": (str,),
            "test_impact_analysis_enabled": (bool,),
            "test_impact_analysis_enabled_inherit": (bool,),
        }

    attribute_map = {
        "auto_test_retries_enabled": "auto_test_retries_enabled",
        "auto_test_retries_enabled_inherit": "auto_test_retries_enabled_inherit",
        "code_coverage_enabled": "code_coverage_enabled",
        "code_coverage_enabled_inherit": "code_coverage_enabled_inherit",
        "early_flake_detection_enabled": "early_flake_detection_enabled",
        "early_flake_detection_enabled_inherit": "early_flake_detection_enabled_inherit",
        "env": "env",
        "failed_test_replay_enabled": "failed_test_replay_enabled",
        "failed_test_replay_enabled_inherit": "failed_test_replay_enabled_inherit",
        "pr_comments_enabled": "pr_comments_enabled",
        "repository_id": "repository_id",
        "service_name": "service_name",
        "test_impact_analysis_enabled": "test_impact_analysis_enabled",
        "test_impact_analysis_enabled_inherit": "test_impact_analysis_enabled_inherit",
    }

    def __init__(
        self_,
        repository_id: str,
        service_name: str,
        auto_test_retries_enabled: Union[bool, UnsetType] = unset,
        auto_test_retries_enabled_inherit: Union[bool, UnsetType] = unset,
        code_coverage_enabled: Union[bool, UnsetType] = unset,
        code_coverage_enabled_inherit: Union[bool, UnsetType] = unset,
        early_flake_detection_enabled: Union[bool, UnsetType] = unset,
        early_flake_detection_enabled_inherit: Union[bool, UnsetType] = unset,
        env: Union[str, UnsetType] = unset,
        failed_test_replay_enabled: Union[bool, UnsetType] = unset,
        failed_test_replay_enabled_inherit: Union[bool, UnsetType] = unset,
        pr_comments_enabled: Union[bool, UnsetType] = unset,
        test_impact_analysis_enabled: Union[bool, UnsetType] = unset,
        test_impact_analysis_enabled_inherit: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating Test Optimization service settings.
        All non-required fields are optional; only provided fields will be updated.
        Setting a field to ``null`` is a no-op. To reset a setting to inherit from the repository level, use the corresponding ``<setting>_inherit`` field.

        :param auto_test_retries_enabled: Whether Auto Test Retries are enabled for this service. Setting to ``null`` is a no-op; use ``auto_test_retries_enabled_inherit`` to reset to repository-level inheritance.
        :type auto_test_retries_enabled: bool, optional

        :param auto_test_retries_enabled_inherit: When ``true`` , resets the Auto Test Retries setting to inherit from the repository level.
        :type auto_test_retries_enabled_inherit: bool, optional

        :param code_coverage_enabled: Whether Code Coverage is enabled for this service. Setting to ``null`` is a no-op; use ``code_coverage_enabled_inherit`` to reset to repository-level inheritance.
        :type code_coverage_enabled: bool, optional

        :param code_coverage_enabled_inherit: When ``true`` , resets the Code Coverage setting to inherit from the repository level.
        :type code_coverage_enabled_inherit: bool, optional

        :param early_flake_detection_enabled: Whether Early Flake Detection is enabled for this service. Setting to ``null`` is a no-op; use ``early_flake_detection_enabled_inherit`` to reset to repository-level inheritance.
        :type early_flake_detection_enabled: bool, optional

        :param early_flake_detection_enabled_inherit: When ``true`` , resets the Early Flake Detection setting to inherit from the repository level.
        :type early_flake_detection_enabled_inherit: bool, optional

        :param env: The environment name. If omitted, defaults to ``none``.
        :type env: str, optional

        :param failed_test_replay_enabled: Whether Failed Test Replay is enabled for this service. Setting to ``null`` is a no-op; use ``failed_test_replay_enabled_inherit`` to reset to repository-level inheritance.
        :type failed_test_replay_enabled: bool, optional

        :param failed_test_replay_enabled_inherit: When ``true`` , resets the Failed Test Replay setting to inherit from the repository level.
        :type failed_test_replay_enabled_inherit: bool, optional

        :param pr_comments_enabled: This field is ignored. PR Comments cannot be overridden at the service level.
        :type pr_comments_enabled: bool, optional

        :param repository_id: The repository identifier.
        :type repository_id: str

        :param service_name: The service name.
        :type service_name: str

        :param test_impact_analysis_enabled: Whether Test Impact Analysis is enabled for this service. Setting to ``null`` is a no-op; use ``test_impact_analysis_enabled_inherit`` to reset to repository-level inheritance.
        :type test_impact_analysis_enabled: bool, optional

        :param test_impact_analysis_enabled_inherit: When ``true`` , resets the Test Impact Analysis setting to inherit from the repository level.
        :type test_impact_analysis_enabled_inherit: bool, optional
        """
        if auto_test_retries_enabled is not unset:
            kwargs["auto_test_retries_enabled"] = auto_test_retries_enabled
        if auto_test_retries_enabled_inherit is not unset:
            kwargs["auto_test_retries_enabled_inherit"] = auto_test_retries_enabled_inherit
        if code_coverage_enabled is not unset:
            kwargs["code_coverage_enabled"] = code_coverage_enabled
        if code_coverage_enabled_inherit is not unset:
            kwargs["code_coverage_enabled_inherit"] = code_coverage_enabled_inherit
        if early_flake_detection_enabled is not unset:
            kwargs["early_flake_detection_enabled"] = early_flake_detection_enabled
        if early_flake_detection_enabled_inherit is not unset:
            kwargs["early_flake_detection_enabled_inherit"] = early_flake_detection_enabled_inherit
        if env is not unset:
            kwargs["env"] = env
        if failed_test_replay_enabled is not unset:
            kwargs["failed_test_replay_enabled"] = failed_test_replay_enabled
        if failed_test_replay_enabled_inherit is not unset:
            kwargs["failed_test_replay_enabled_inherit"] = failed_test_replay_enabled_inherit
        if pr_comments_enabled is not unset:
            kwargs["pr_comments_enabled"] = pr_comments_enabled
        if test_impact_analysis_enabled is not unset:
            kwargs["test_impact_analysis_enabled"] = test_impact_analysis_enabled
        if test_impact_analysis_enabled_inherit is not unset:
            kwargs["test_impact_analysis_enabled_inherit"] = test_impact_analysis_enabled_inherit
        super().__init__(kwargs)

        self_.repository_id = repository_id
        self_.service_name = service_name
