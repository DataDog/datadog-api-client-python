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
    from datadog_api_client.v2.model.upsert_o_auth_scopes_restriction_data_attributes import (
        UpsertOAuthScopesRestrictionDataAttributes,
    )
    from datadog_api_client.v2.model.upsert_o_auth_scopes_restriction_type import UpsertOAuthScopesRestrictionType


class UpsertOAuthScopesRestrictionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.upsert_o_auth_scopes_restriction_data_attributes import (
            UpsertOAuthScopesRestrictionDataAttributes,
        )
        from datadog_api_client.v2.model.upsert_o_auth_scopes_restriction_type import UpsertOAuthScopesRestrictionType

        return {
            "attributes": (UpsertOAuthScopesRestrictionDataAttributes,),
            "type": (UpsertOAuthScopesRestrictionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: UpsertOAuthScopesRestrictionType,
        attributes: Union[UpsertOAuthScopesRestrictionDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object of an upsert OAuth2 scopes restriction request.

        :param attributes: Attributes of an upsert OAuth2 scopes restriction request.
        :type attributes: UpsertOAuthScopesRestrictionDataAttributes, optional

        :param type: JSON:API resource type for an upsert OAuth2 client scopes restriction request.
        :type type: UpsertOAuthScopesRestrictionType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
