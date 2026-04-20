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
    from datadog_api_client.v2.model.anonymize_users_request_attributes import AnonymizeUsersRequestAttributes
    from datadog_api_client.v2.model.anonymize_users_request_type import AnonymizeUsersRequestType


class AnonymizeUsersRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.anonymize_users_request_attributes import AnonymizeUsersRequestAttributes
        from datadog_api_client.v2.model.anonymize_users_request_type import AnonymizeUsersRequestType

        return {
            "attributes": (AnonymizeUsersRequestAttributes,),
            "id": (str,),
            "type": (AnonymizeUsersRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AnonymizeUsersRequestAttributes,
        type: AnonymizeUsersRequestType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object to anonymize a list of users.

        :param attributes: Attributes of an anonymize users request.
        :type attributes: AnonymizeUsersRequestAttributes

        :param id: Unique identifier for the request. Not used server-side.
        :type id: str, optional

        :param type: Type of the anonymize users request.
        :type type: AnonymizeUsersRequestType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
