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
    from datadog_api_client.v2.model.create_tenancy_config_data_attributes import CreateTenancyConfigDataAttributes
    from datadog_api_client.v2.model.create_tenancy_config_data_type import CreateTenancyConfigDataType


class CreateTenancyConfigData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_tenancy_config_data_attributes import CreateTenancyConfigDataAttributes
        from datadog_api_client.v2.model.create_tenancy_config_data_type import CreateTenancyConfigDataType

        return {
            "attributes": (CreateTenancyConfigDataAttributes,),
            "id": (str,),
            "type": (CreateTenancyConfigDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: CreateTenancyConfigDataType,
        attributes: Union[CreateTenancyConfigDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``CreateTenancyConfigData`` object.

        :param attributes: The definition of ``CreateTenancyConfigDataAttributes`` object.
        :type attributes: CreateTenancyConfigDataAttributes, optional

        :param id: The OCID of the tenancy to be integrated.
        :type id: str

        :param type: OCI tenancy resource type.
        :type type: CreateTenancyConfigDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
