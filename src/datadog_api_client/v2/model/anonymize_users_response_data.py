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
    from datadog_api_client.v2.model.anonymize_users_response_attributes import AnonymizeUsersResponseAttributes
    from datadog_api_client.v2.model.anonymize_users_response_type import AnonymizeUsersResponseType


class AnonymizeUsersResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.anonymize_users_response_attributes import AnonymizeUsersResponseAttributes
        from datadog_api_client.v2.model.anonymize_users_response_type import AnonymizeUsersResponseType

        return {
            "attributes": (AnonymizeUsersResponseAttributes,),
            "id": (str,),
            "type": (AnonymizeUsersResponseType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[AnonymizeUsersResponseAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[AnonymizeUsersResponseType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response data for anonymizing users.

        :param attributes: Attributes of an anonymize users response.
        :type attributes: AnonymizeUsersResponseAttributes, optional

        :param id: Unique identifier of the response.
        :type id: str, optional

        :param type: Type of the anonymize users response.
        :type type: AnonymizeUsersResponseType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
