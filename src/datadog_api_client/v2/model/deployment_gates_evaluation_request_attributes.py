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


class DeploymentGatesEvaluationRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "env": (str,),
            "identifier": (str,),
            "primary_tag": (str,),
            "service": (str,),
            "version": (str,),
        }

    attribute_map = {
        "env": "env",
        "identifier": "identifier",
        "primary_tag": "primary_tag",
        "service": "service",
        "version": "version",
    }

    def __init__(
        self_,
        env: str,
        service: str,
        identifier: Union[str, UnsetType] = unset,
        primary_tag: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for a deployment gate evaluation request.

        :param env: The environment of the deployment.
        :type env: str

        :param identifier: The identifier of the deployment gate. Defaults to "default".
        :type identifier: str, optional

        :param primary_tag: A primary tag to scope APM Faulty Deployment Detection rules.
        :type primary_tag: str, optional

        :param service: The service being deployed.
        :type service: str

        :param version: The version of the deployment. Required for APM Faulty Deployment Detection rules.
        :type version: str, optional
        """
        if identifier is not unset:
            kwargs["identifier"] = identifier
        if primary_tag is not unset:
            kwargs["primary_tag"] = primary_tag
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.env = env
        self_.service = service
