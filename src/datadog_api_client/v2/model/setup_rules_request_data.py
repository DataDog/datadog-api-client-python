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
    from datadog_api_client.v2.model.setup_rules_request_attributes import SetupRulesRequestAttributes
    from datadog_api_client.v2.model.setup_rules_request_data_type import SetupRulesRequestDataType


class SetupRulesRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.setup_rules_request_attributes import SetupRulesRequestAttributes
        from datadog_api_client.v2.model.setup_rules_request_data_type import SetupRulesRequestDataType

        return {
            "attributes": (SetupRulesRequestAttributes,),
            "type": (SetupRulesRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: SetupRulesRequestAttributes, type: SetupRulesRequestDataType, **kwargs):
        """
        Data for setting up rules.

        :param attributes: Attributes for setting up rules.
        :type attributes: SetupRulesRequestAttributes

        :param type:
        :type type: SetupRulesRequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
