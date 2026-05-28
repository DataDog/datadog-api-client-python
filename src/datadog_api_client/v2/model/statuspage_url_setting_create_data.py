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
    from datadog_api_client.v2.model.statuspage_url_setting_create_attributes import (
        StatuspageUrlSettingCreateAttributes,
    )
    from datadog_api_client.v2.model.statuspage_url_setting_type import StatuspageUrlSettingType


class StatuspageUrlSettingCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.statuspage_url_setting_create_attributes import (
            StatuspageUrlSettingCreateAttributes,
        )
        from datadog_api_client.v2.model.statuspage_url_setting_type import StatuspageUrlSettingType

        return {
            "attributes": (StatuspageUrlSettingCreateAttributes,),
            "type": (StatuspageUrlSettingType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: StatuspageUrlSettingCreateAttributes, type: StatuspageUrlSettingType, **kwargs):
        """
        Statuspage URL setting data for a create request.

        :param attributes: The Statuspage URL setting attributes for a create request.
        :type attributes: StatuspageUrlSettingCreateAttributes

        :param type: Statuspage URL setting resource type.
        :type type: StatuspageUrlSettingType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
