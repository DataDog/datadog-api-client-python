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


class RuleBasedViewComplianceFramework(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "control": (str,),
            "framework": (str,),
            "is_default": (bool,),
            "message": (str,),
            "requirement": (str,),
            "version": (str,),
        }

    attribute_map = {
        "control": "control",
        "framework": "framework",
        "is_default": "is_default",
        "message": "message",
        "requirement": "requirement",
        "version": "version",
    }

    def __init__(
        self_,
        control: Union[str, UnsetType] = unset,
        framework: Union[str, UnsetType] = unset,
        is_default: Union[bool, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        requirement: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Compliance framework mapping for a rule.

        :param control: Identifier of the control inside the requirement.
        :type control: str, optional

        :param framework: Handle of the compliance framework.
        :type framework: str, optional

        :param is_default: Whether the framework is a Datadog default framework. ``true`` indicates a Datadog framework and ``false`` indicates a custom framework.
        :type is_default: bool, optional

        :param message: Optional message describing the framework mapping for the rule.
        :type message: str, optional

        :param requirement: Name of the requirement that contains the control.
        :type requirement: str, optional

        :param version: Version of the compliance framework.
        :type version: str, optional
        """
        if control is not unset:
            kwargs["control"] = control
        if framework is not unset:
            kwargs["framework"] = framework
        if is_default is not unset:
            kwargs["is_default"] = is_default
        if message is not unset:
            kwargs["message"] = message
        if requirement is not unset:
            kwargs["requirement"] = requirement
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
