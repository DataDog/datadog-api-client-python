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
    from datadog_api_client.v2.model.tenancy_config_data_attributes import TenancyConfigDataAttributes
    from datadog_api_client.v2.model.tenancy_config_data_type import TenancyConfigDataType


class TenancyConfigData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tenancy_config_data_attributes import TenancyConfigDataAttributes
        from datadog_api_client.v2.model.tenancy_config_data_type import TenancyConfigDataType

        return {
            "attributes": (TenancyConfigDataAttributes,),
            "id": (str,),
            "type": (TenancyConfigDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: TenancyConfigDataType,
        attributes: Union[TenancyConfigDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``TenancyConfigData`` object.

        :param attributes: The definition of ``TenancyConfigDataAttributes`` object.
        :type attributes: TenancyConfigDataAttributes, optional

        :param id: The OCID of the tenancy config.
        :type id: str, optional

        :param type: OCI tenancy resource type.
        :type type: TenancyConfigDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
