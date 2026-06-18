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
    from datadog_api_client.v2.model.vercel_config_attributes import VercelConfigAttributes
    from datadog_api_client.v2.model.vercel_config_data_response_type import VercelConfigDataResponseType


class VercelConfigDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.vercel_config_attributes import VercelConfigAttributes
        from datadog_api_client.v2.model.vercel_config_data_response_type import VercelConfigDataResponseType

        return {
            "attributes": (VercelConfigAttributes,),
            "id": (str,),
            "type": (VercelConfigDataResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: VercelConfigAttributes, id: str, type: VercelConfigDataResponseType, **kwargs):
        """
        Vercel configuration data returned by the API.

        :param attributes: Attributes of the Datadog Vercel integration configuration.
        :type attributes: VercelConfigAttributes

        :param id: Vercel configuration ID.
        :type id: str

        :param type: Type identifier for a Vercel configuration resource.
        :type type: VercelConfigDataResponseType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
