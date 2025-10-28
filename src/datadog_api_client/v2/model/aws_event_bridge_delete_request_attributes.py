# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AWSEventBridgeDeleteRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "event_generator_name": (str,),
            "region": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "event_generator_name": "event_generator_name",
        "region": "region",
    }

    def __init__(self_, account_id: str, event_generator_name: str, region: str, **kwargs):
        """
        The EventBridge source to be deleted.

        :param account_id: AWS Account ID.
        :type account_id: str

        :param event_generator_name: The event source name.
        :type event_generator_name: str

        :param region: The event source's
            `AWS region <https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints>`_.
        :type region: str
        """
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.event_generator_name = event_generator_name
        self_.region = region
