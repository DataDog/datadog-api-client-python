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
    from datadog_api_client.v2.model.upsert_o_auth_scopes_restriction_data import UpsertOAuthScopesRestrictionData


class UpsertOAuthScopesRestrictionRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.upsert_o_auth_scopes_restriction_data import UpsertOAuthScopesRestrictionData

        return {
            "data": (UpsertOAuthScopesRestrictionData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: UpsertOAuthScopesRestrictionData, **kwargs):
        """
        Request payload for creating or updating the scopes restriction of an OAuth2 client.

        :param data: Data object of an upsert OAuth2 scopes restriction request.
        :type data: UpsertOAuthScopesRestrictionData
        """
        super().__init__(kwargs)

        self_.data = data
