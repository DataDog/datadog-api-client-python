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


class SecurityAgentInvestigationEntity(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "sub_type": (str,),
            "type": (str,),
            "value": (str,),
        }

    attribute_map = {
        "sub_type": "sub_type",
        "type": "type",
        "value": "value",
    }

    def __init__(self_, type: str, value: str, sub_type: Union[str, UnsetType] = unset, **kwargs):
        """
        An entity the investigation found.

        :param sub_type: More specific type of the entity.
        :type sub_type: str, optional

        :param type: Type of the entity, such as a user, a host, or an IP address.
        :type type: str

        :param value: Value that identifies the entity.
        :type value: str
        """
        if sub_type is not unset:
            kwargs["sub_type"] = sub_type
        super().__init__(kwargs)

        self_.type = type
        self_.value = value
