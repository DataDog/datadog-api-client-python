# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.rum_application_create_attributes import RUMApplicationCreateAttributes

if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_application_create_type import RUMApplicationCreateType


@dataclass
class RUMApplicationCreateJSON:
    type: str
    name: Union[str, UnsetType] = unset


class RUMApplicationCreate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_application_create_type import RUMApplicationCreateType

        return {
            "attributes": (RUMApplicationCreateAttributes,),
            "type": (RUMApplicationCreateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }
    json_api_model = RUMApplicationCreateJSON

    def __init__(self_, attributes: RUMApplicationCreateAttributes, type: RUMApplicationCreateType, **kwargs):
        """
        RUM application creation.

        :param attributes: RUM application creation attributes.
        :type attributes: RUMApplicationCreateAttributes

        :param type: RUM application creation type.
        :type type: RUMApplicationCreateType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
