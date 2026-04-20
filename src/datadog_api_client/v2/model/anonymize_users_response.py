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
    from datadog_api_client.v2.model.anonymize_users_response_data import AnonymizeUsersResponseData


class AnonymizeUsersResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.anonymize_users_response_data import AnonymizeUsersResponseData

        return {
            "data": (AnonymizeUsersResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[AnonymizeUsersResponseData, UnsetType] = unset, **kwargs):
        """
        Response containing the result of an anonymize users request.

        :param data: Response data for anonymizing users.
        :type data: AnonymizeUsersResponseData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
