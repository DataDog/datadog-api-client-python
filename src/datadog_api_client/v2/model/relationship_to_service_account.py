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
    from datadog_api_client.v2.model.relationship_to_service_account_data import RelationshipToServiceAccountData


class RelationshipToServiceAccount(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_service_account_data import RelationshipToServiceAccountData

        return {
            "data": (RelationshipToServiceAccountData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: RelationshipToServiceAccountData, **kwargs):
        """
        Relationship to service account.

        :param data: Relationship to service account object.
        :type data: RelationshipToServiceAccountData
        """
        super().__init__(kwargs)

        self_.data = data
