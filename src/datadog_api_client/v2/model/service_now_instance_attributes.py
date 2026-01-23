# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ServiceNowInstanceAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "instance_name": (str,),
        }

    attribute_map = {
        "instance_name": "instance_name",
    }

    def __init__(self_, instance_name: str, **kwargs):
        """
        Attributes of a ServiceNow instance

        :param instance_name: The name of the ServiceNow instance
        :type instance_name: str
        """
        super().__init__(kwargs)

        self_.instance_name = instance_name
