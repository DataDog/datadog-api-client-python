# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class FleetDeploymentPackage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "version": (str,),
        }

    attribute_map = {
        "name": "name",
        "version": "version",
    }

    def __init__(self_, name: str, version: str, **kwargs):
        """
        A package and its target version for deployment.

        :param name: The name of the package to deploy.
        :type name: str

        :param version: The target version of the package to deploy.
        :type version: str
        """
        super().__init__(kwargs)

        self_.name = name
        self_.version = version
