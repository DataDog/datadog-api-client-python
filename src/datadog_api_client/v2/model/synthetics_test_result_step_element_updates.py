# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SyntheticsTestResultStepElementUpdates(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "multi_locator": ({str: (str,)},),
            "target_outer_html": (str,),
            "version": (int,),
        }

    attribute_map = {
        "multi_locator": "multi_locator",
        "target_outer_html": "target_outer_html",
        "version": "version",
    }

    def __init__(
        self_,
        multi_locator: Union[Dict[str, str], UnsetType] = unset,
        target_outer_html: Union[str, UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Element locator updates produced during a step.

        :param multi_locator: Updated multi-locator definition.
        :type multi_locator: {str: (str,)}, optional

        :param target_outer_html: Updated outer HTML of the targeted element.
        :type target_outer_html: str, optional

        :param version: Version of the element locator definition.
        :type version: int, optional
        """
        if multi_locator is not unset:
            kwargs["multi_locator"] = multi_locator
        if target_outer_html is not unset:
            kwargs["target_outer_html"] = target_outer_html
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
