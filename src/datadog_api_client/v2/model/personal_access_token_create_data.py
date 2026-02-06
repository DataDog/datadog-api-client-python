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
    from datadog_api_client.v2.model.personal_access_token_create_attributes import PersonalAccessTokenCreateAttributes
    from datadog_api_client.v2.model.personal_access_token_type import PersonalAccessTokenType


class PersonalAccessTokenCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.personal_access_token_create_attributes import (
            PersonalAccessTokenCreateAttributes,
        )
        from datadog_api_client.v2.model.personal_access_token_type import PersonalAccessTokenType

        return {
            "attributes": (PersonalAccessTokenCreateAttributes,),
            "type": (PersonalAccessTokenType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: PersonalAccessTokenCreateAttributes, type: PersonalAccessTokenType, **kwargs):
        """
        Object used to create a personal access token.

        :param attributes: Attributes used to create a personal access token.
        :type attributes: PersonalAccessTokenCreateAttributes

        :param type: Personal access tokens resource type.
        :type type: PersonalAccessTokenType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
