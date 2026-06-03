# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ServiceRepositoryInfoRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "service": (str,),
            "version": (str,),
        }

    attribute_map = {
        "service": "service",
        "version": "version",
    }

    def __init__(self_, service: str, version: str, **kwargs):
        """
        Attributes for the service repository info request.

        :param service: The name of the service.
        :type service: str

        :param version: The version of the service.
        :type version: str
        """
        super().__init__(kwargs)

        self_.service = service
        self_.version = version
