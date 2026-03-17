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
    from datadog_api_client.v2.model.licenses_list_request_data_attributes import LicensesListRequestDataAttributes
    from datadog_api_client.v2.model.licenses_list_request_data_type import LicensesListRequestDataType


class LicensesListRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.licenses_list_request_data_attributes import LicensesListRequestDataAttributes
        from datadog_api_client.v2.model.licenses_list_request_data_type import LicensesListRequestDataType

        return {
            "attributes": (LicensesListRequestDataAttributes,),
            "id": (str,),
            "type": (LicensesListRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: LicensesListRequestDataType,
        attributes: Union[LicensesListRequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: LicensesListRequestDataAttributes, optional

        :param id: Unique identifier for the request
        :type id: str, optional

        :param type:
        :type type: LicensesListRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
