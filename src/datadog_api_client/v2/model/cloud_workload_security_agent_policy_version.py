# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class CloudWorkloadSecurityAgentPolicyVersion(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "date": (str, none_type),
            "name": (str,),
        }

    attribute_map = {
        "date": "date",
        "name": "name",
    }

    def __init__(self_, date: Union[str, none_type, UnsetType] = unset, name: Union[str, UnsetType] = unset, **kwargs):
        """
        The versions of the policy

        :param date: The date and time the version was created
        :type date: str, none_type, optional

        :param name: The version of the policy
        :type name: str, optional
        """
        if date is not unset:
            kwargs["date"] = date
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
