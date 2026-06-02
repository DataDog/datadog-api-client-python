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
    from datadog_api_client.v2.model.opsgenie_account_response_attributes import OpsgenieAccountResponseAttributes
    from datadog_api_client.v2.model.opsgenie_account_type import OpsgenieAccountType


class OpsgenieAccountResponseData(ModelNormal):
    validations = {
        "id": {
            "max_length": 100,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.opsgenie_account_response_attributes import OpsgenieAccountResponseAttributes
        from datadog_api_client.v2.model.opsgenie_account_type import OpsgenieAccountType

        return {
            "attributes": (OpsgenieAccountResponseAttributes,),
            "id": (str,),
            "type": (OpsgenieAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: OpsgenieAccountResponseAttributes, id: str, type: OpsgenieAccountType, **kwargs):
        """
        Opsgenie account data from a response.

        :param attributes: The attributes from an Opsgenie account response.
        :type attributes: OpsgenieAccountResponseAttributes

        :param id: The ID of the Opsgenie account.
        :type id: str

        :param type: Opsgenie account resource type.
        :type type: OpsgenieAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
