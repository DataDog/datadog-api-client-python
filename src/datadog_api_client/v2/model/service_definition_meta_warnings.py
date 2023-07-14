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


class ServiceDefinitionMetaWarnings(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "instance_location": (str,),
            "keyword_location": (str,),
            "message": (str,),
        }

    attribute_map = {
        "instance_location": "instance-location",
        "keyword_location": "keyword-location",
        "message": "message",
    }

    def __init__(
        self_,
        instance_location: Union[str, UnsetType] = unset,
        keyword_location: Union[str, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Schema validation warnings.

        :param instance_location: The warning instance location.
        :type instance_location: str, optional

        :param keyword_location: The warning keyword location.
        :type keyword_location: str, optional

        :param message: The warning message.
        :type message: str, optional
        """
        if instance_location is not unset:
            kwargs["instance_location"] = instance_location
        if keyword_location is not unset:
            kwargs["keyword_location"] = keyword_location
        if message is not unset:
            kwargs["message"] = message
        super().__init__(kwargs)
