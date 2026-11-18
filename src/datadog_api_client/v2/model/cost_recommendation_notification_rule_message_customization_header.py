# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CostRecommendationNotificationRuleMessageCustomizationHeader(ModelNormal):
    validations = {
        "custom_text": {
            "max_length": 500,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "custom_text": (str,),
            "notification_name": (bool,),
            "total_savings": (bool,),
        }

    attribute_map = {
        "custom_text": "custom_text",
        "notification_name": "notification_name",
        "total_savings": "total_savings",
    }

    def __init__(
        self_,
        custom_text: Union[str, UnsetType] = unset,
        notification_name: Union[bool, UnsetType] = unset,
        total_savings: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        What the digest header shows.

        :param custom_text: Text shown in the header, up to 500 characters. It can use the ``{{ total_savings }}`` , ``{{ rec_count }}`` ,
            and ``{{ digest_date }}`` variables.
        :type custom_text: str, optional

        :param notification_name: Whether the header shows the rule name.
        :type notification_name: bool, optional

        :param total_savings: Whether the header shows the total potential savings.
        :type total_savings: bool, optional
        """
        if custom_text is not unset:
            kwargs["custom_text"] = custom_text
        if notification_name is not unset:
            kwargs["notification_name"] = notification_name
        if total_savings is not unset:
            kwargs["total_savings"] = total_savings
        super().__init__(kwargs)
