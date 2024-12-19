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
    from datadog_api_client.v2.model.update_app_request_data_attributes import UpdateAppRequestDataAttributes
    from datadog_api_client.v2.model.update_app_request_data_type import UpdateAppRequestDataType


class UpdateAppRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_app_request_data_attributes import UpdateAppRequestDataAttributes
        from datadog_api_client.v2.model.update_app_request_data_type import UpdateAppRequestDataType

        return {
            "attributes": (UpdateAppRequestDataAttributes,),
            "id": (str,),
            "type": (UpdateAppRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: UpdateAppRequestDataType,
        attributes: Union[UpdateAppRequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``UpdateAppRequestData`` object.

        :param attributes: The definition of ``UpdateAppRequestDataAttributes`` object.
        :type attributes: UpdateAppRequestDataAttributes, optional

        :param id: The ``data`` ``id``.
        :type id: str, optional

        :param type: The definition of ``UpdateAppRequestDataType`` object.
        :type type: UpdateAppRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
