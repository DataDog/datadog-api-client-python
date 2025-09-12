# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.gcp_uc_config_response_data_attributes import GcpUcConfigResponseDataAttributes
    from datadog_api_client.v2.model.gcp_uc_config_response_data_type import GcpUcConfigResponseDataType


class GcpUcConfigResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.gcp_uc_config_response_data_attributes import GcpUcConfigResponseDataAttributes
        from datadog_api_client.v2.model.gcp_uc_config_response_data_type import GcpUcConfigResponseDataType

        return {
            "attributes": (GcpUcConfigResponseDataAttributes,),
            "id": (str,),
            "type": (GcpUcConfigResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: GcpUcConfigResponseDataType,
        attributes: Union[GcpUcConfigResponseDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``GcpUcConfigResponseData`` object.

        :param attributes: The definition of ``GcpUcConfigResponseDataAttributes`` object.
        :type attributes: GcpUcConfigResponseDataAttributes, optional

        :param id: The ``GcpUcConfigResponseData`` ``id``.
        :type id: str, optional

        :param type: Google Cloud Usage Cost config resource type.
        :type type: GcpUcConfigResponseDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
