# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class JiraAccountAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "consumer_key": (str,),
            "instance_url": (str,),
            "last_webhook_timestamp": (datetime,),
        }

    attribute_map = {
        "consumer_key": "consumer_key",
        "instance_url": "instance_url",
        "last_webhook_timestamp": "last_webhook_timestamp",
    }

    def __init__(
        self_,
        consumer_key: str,
        instance_url: str,
        last_webhook_timestamp: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Jira account

        :param consumer_key: The consumer key for the Jira account
        :type consumer_key: str

        :param instance_url: The URL of the Jira instance
        :type instance_url: str

        :param last_webhook_timestamp: Timestamp of the last webhook received
        :type last_webhook_timestamp: datetime, optional
        """
        if last_webhook_timestamp is not unset:
            kwargs["last_webhook_timestamp"] = last_webhook_timestamp
        super().__init__(kwargs)

        self_.consumer_key = consumer_key
        self_.instance_url = instance_url
