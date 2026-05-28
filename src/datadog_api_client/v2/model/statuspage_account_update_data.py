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
    from datadog_api_client.v2.model.statuspage_account_update_attributes import StatuspageAccountUpdateAttributes
    from datadog_api_client.v2.model.statuspage_account_type import StatuspageAccountType


class StatuspageAccountUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.statuspage_account_update_attributes import StatuspageAccountUpdateAttributes
        from datadog_api_client.v2.model.statuspage_account_type import StatuspageAccountType

        return {
            "attributes": (StatuspageAccountUpdateAttributes,),
            "type": (StatuspageAccountType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: StatuspageAccountUpdateAttributes, type: StatuspageAccountType, **kwargs):
        """
        Statuspage account data for an update request.

        :param attributes: The Statuspage account attributes for an update request.
        :type attributes: StatuspageAccountUpdateAttributes

        :param type: Statuspage account resource type.
        :type type: StatuspageAccountType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
