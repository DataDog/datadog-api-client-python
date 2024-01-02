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


class AWSRelatedAccountAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "has_datadog_integration": (bool,),
            "name": (str,),
        }

    attribute_map = {
        "has_datadog_integration": "has_datadog_integration",
        "name": "name",
    }

    def __init__(
        self_, has_datadog_integration: Union[bool, UnsetType] = unset, name: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Attributes for an AWS related account.

        :param has_datadog_integration: Whether or not the AWS account has a Datadog integration.
        :type has_datadog_integration: bool, optional

        :param name: The name of the AWS account.
        :type name: str, optional
        """
        if has_datadog_integration is not unset:
            kwargs["has_datadog_integration"] = has_datadog_integration
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
