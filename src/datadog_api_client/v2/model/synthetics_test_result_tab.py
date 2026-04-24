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


class SyntheticsTestResultTab(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "focused": (bool,),
            "title": (str,),
            "url": (str,),
        }

    attribute_map = {
        "focused": "focused",
        "title": "title",
        "url": "url",
    }

    def __init__(
        self_,
        focused: Union[bool, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Information about a browser tab involved in a step.

        :param focused: Whether the tab was focused during the step.
        :type focused: bool, optional

        :param title: Title of the tab.
        :type title: str, optional

        :param url: URL loaded in the tab.
        :type url: str, optional
        """
        if focused is not unset:
            kwargs["focused"] = focused
        if title is not unset:
            kwargs["title"] = title
        if url is not unset:
            kwargs["url"] = url
        super().__init__(kwargs)
