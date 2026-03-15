# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.idp_config_attributes import IDPConfigAttributes
    from datadog_api_client.v2.model.idp_config_type import IDPConfigType


class IDPConfigData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.idp_config_attributes import IDPConfigAttributes
        from datadog_api_client.v2.model.idp_config_type import IDPConfigType

        return {
            "attributes": (IDPConfigAttributes,),
            "id": (str,),
            "type": (IDPConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: IDPConfigAttributes, id: str, type: IDPConfigType, **kwargs):
        """
        IDP configuration data.

        :param attributes: IDP configuration attributes.
        :type attributes: IDPConfigAttributes

        :param id: Configuration identifier.
        :type id: str

        :param type: Resource type.
        :type type: IDPConfigType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
