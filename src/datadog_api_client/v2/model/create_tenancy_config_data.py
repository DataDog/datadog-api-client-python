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
    from datadog_api_client.v2.model.update_tenancy_config_data_type import UpdateTenancyConfigDataType


class CreateTenancyConfigData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_tenancy_config_data_attributes import CreateTenancyConfigDataAttributes
        from datadog_api_client.v2.model.update_tenancy_config_data_type import UpdateTenancyConfigDataType

        return {
            "attributes": (CreateTenancyConfigDataAttributes,),
            "id": (str,),
            "type": (UpdateTenancyConfigDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: UpdateTenancyConfigDataType,
        attributes: Union[CreateTenancyConfigDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object for creating a new OCI tenancy integration configuration, including the tenancy ID, type, and configuration attributes.

        :param attributes: Attributes for creating a new OCI tenancy integration configuration, including credentials, region settings, and collection options.
        :type attributes: CreateTenancyConfigDataAttributes, optional

        :param id: The OCID of the OCI tenancy to configure.
        :type id: str

        :param type: OCI tenancy resource type.
        :type type: UpdateTenancyConfigDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
