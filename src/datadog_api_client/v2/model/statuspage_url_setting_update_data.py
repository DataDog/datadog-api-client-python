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
    from datadog_api_client.v2.model.statuspage_url_setting_update_attributes import (
        StatuspageUrlSettingUpdateAttributes,
    )
    from datadog_api_client.v2.model.statuspage_url_setting_type import StatuspageUrlSettingType


class StatuspageUrlSettingUpdateData(ModelNormal):
    validations = {
        "id": {
            "max_length": 100,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.statuspage_url_setting_update_attributes import (
            StatuspageUrlSettingUpdateAttributes,
        )
        from datadog_api_client.v2.model.statuspage_url_setting_type import StatuspageUrlSettingType

        return {
            "attributes": (StatuspageUrlSettingUpdateAttributes,),
            "id": (str,),
            "type": (StatuspageUrlSettingType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: StatuspageUrlSettingUpdateAttributes, id: str, type: StatuspageUrlSettingType, **kwargs
    ):
        """
        Statuspage URL setting data for an update request.

        :param attributes: The Statuspage URL setting attributes for an update request.
        :type attributes: StatuspageUrlSettingUpdateAttributes

        :param id: The ID of the Statuspage URL setting.
        :type id: str

        :param type: Statuspage URL setting resource type.
        :type type: StatuspageUrlSettingType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
