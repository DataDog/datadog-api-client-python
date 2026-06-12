# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.deployment_gates_evaluation_configuration import (
        DeploymentGatesEvaluationConfiguration,
    )


class DeploymentGatesEvaluationRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.deployment_gates_evaluation_configuration import (
            DeploymentGatesEvaluationConfiguration,
        )

        return {
            "configuration": (DeploymentGatesEvaluationConfiguration,),
            "env": (str,),
            "identifier": (str,),
            "primary_tag": (str,),
            "service": (str,),
            "version": (str,),
        }

    attribute_map = {
        "configuration": "configuration",
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
        configuration: Union[DeploymentGatesEvaluationConfiguration, UnsetType] = unset,
        identifier: Union[str, UnsetType] = unset,
        primary_tag: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for a deployment gate evaluation request.
        When ``configuration`` is provided, rules are evaluated inline from that configuration.
        When omitted, rules are resolved from the preconfigured gate for the given service and environment.

        :param configuration: Inline rule definitions for a deployment gate evaluation. When provided, rules are evaluated
            directly from this configuration instead of using the preconfigured gate rules.
            At least one rule is required.
        :type configuration: DeploymentGatesEvaluationConfiguration, optional

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
        if configuration is not unset:
            kwargs["configuration"] = configuration
        if identifier is not unset:
            kwargs["identifier"] = identifier
        if primary_tag is not unset:
            kwargs["primary_tag"] = primary_tag
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.env = env
        self_.service = service
