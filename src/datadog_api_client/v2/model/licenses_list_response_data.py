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
    from datadog_api_client.v2.model.licenses_list_response_data_attributes import LicensesListResponseDataAttributes
    from datadog_api_client.v2.model.licenses_list_response_data_type import LicensesListResponseDataType


class LicensesListResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.licenses_list_response_data_attributes import (
            LicensesListResponseDataAttributes,
        )
        from datadog_api_client.v2.model.licenses_list_response_data_type import LicensesListResponseDataType

        return {
            "attributes": (LicensesListResponseDataAttributes,),
            "id": (str,),
            "type": (LicensesListResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: LicensesListResponseDataAttributes, id: str, type: LicensesListResponseDataType, **kwargs
    ):
        """
        The data object in a licenses list response, containing the list of SPDX licenses.

        :param attributes: The attributes of the licenses list response, containing the array of SPDX licenses.
        :type attributes: LicensesListResponseDataAttributes

        :param id: The unique identifier for this licenses list response.
        :type id: str

        :param type: The type identifier for license list responses.
        :type type: LicensesListResponseDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
