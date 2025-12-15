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


class CaseInsightsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "ref": (str,),
            "resource_id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "ref": "ref",
        "resource_id": "resource_id",
        "type": "type",
    }

    def __init__(
        self_,
        ref: Union[str, UnsetType] = unset,
        resource_id: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        An insight of the case.

        :param ref: Reference of the insight.
        :type ref: str, optional

        :param resource_id: Unique identifier of the resource. For example, the unique identifier of a security finding.
        :type resource_id: str, optional

        :param type: Type of the resource. For example, the type of a security finding is "SECURITY_FINDING".
        :type type: str, optional
        """
        if ref is not unset:
            kwargs["ref"] = ref
        if resource_id is not unset:
            kwargs["resource_id"] = resource_id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
