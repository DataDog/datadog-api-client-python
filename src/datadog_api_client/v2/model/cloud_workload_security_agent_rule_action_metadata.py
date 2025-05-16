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


class CloudWorkloadSecurityAgentRuleActionMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "image_tag": (str,),
            "service": (str,),
            "short_image": (str,),
        }

    attribute_map = {
        "image_tag": "image_tag",
        "service": "service",
        "short_image": "short_image",
    }

    def __init__(
        self_,
        image_tag: Union[str, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        short_image: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The metadata action applied on the scope matching the rule

        :param image_tag: The image tag of the metadata action
        :type image_tag: str, optional

        :param service: The service of the metadata action
        :type service: str, optional

        :param short_image: The short image of the metadata action
        :type short_image: str, optional
        """
        if image_tag is not unset:
            kwargs["image_tag"] = image_tag
        if service is not unset:
            kwargs["service"] = service
        if short_image is not unset:
            kwargs["short_image"] = short_image
        super().__init__(kwargs)
