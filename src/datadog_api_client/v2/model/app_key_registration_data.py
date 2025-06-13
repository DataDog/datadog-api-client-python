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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.app_key_registration_data_type import AppKeyRegistrationDataType


class AppKeyRegistrationData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.app_key_registration_data_type import AppKeyRegistrationDataType

        return {
            "id": (UUID,),
            "type": (AppKeyRegistrationDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }
    read_only_vars = {
        "id",
    }

    def __init__(self_, type: AppKeyRegistrationDataType, id: Union[UUID, UnsetType] = unset, **kwargs):
        """
        Data related to the app key registration.

        :param id: The app key registration identifier
        :type id: UUID, optional

        :param type: The definition of ``AppKeyRegistrationDataType`` object.
        :type type: AppKeyRegistrationDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
