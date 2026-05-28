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
    from datadog_api_client.v2.model.opsgenie_account_create_attributes import OpsgenieAccountCreateAttributes
    from datadog_api_client.v2.model.opsgenie_account_type import OpsgenieAccountType


class OpsgenieAccountCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.opsgenie_account_create_attributes import OpsgenieAccountCreateAttributes
        from datadog_api_client.v2.model.opsgenie_account_type import OpsgenieAccountType

        return {
            "attributes": (OpsgenieAccountCreateAttributes,),
            "type": (OpsgenieAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: OpsgenieAccountCreateAttributes, type: OpsgenieAccountType, **kwargs):
        """
        Opsgenie account data for a create request.

        :param attributes: The Opsgenie account attributes for a create request.
        :type attributes: OpsgenieAccountCreateAttributes

        :param type: Opsgenie account resource type.
        :type type: OpsgenieAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
