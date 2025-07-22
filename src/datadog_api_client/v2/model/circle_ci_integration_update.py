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
    from datadog_api_client.v2.model.circle_ci_credentials_update import CircleCICredentialsUpdate
    from datadog_api_client.v2.model.circle_ci_integration_type import CircleCIIntegrationType
    from datadog_api_client.v2.model.circle_ciapi_key_update import CircleCIAPIKeyUpdate


class CircleCIIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.circle_ci_credentials_update import CircleCICredentialsUpdate
        from datadog_api_client.v2.model.circle_ci_integration_type import CircleCIIntegrationType

        return {
            "credentials": (CircleCICredentialsUpdate,),
            "type": (CircleCIIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: CircleCIIntegrationType,
        credentials: Union[CircleCICredentialsUpdate, CircleCIAPIKeyUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``CircleCIIntegrationUpdate`` object.

        :param credentials: The definition of the ``CircleCICredentialsUpdate`` object.
        :type credentials: CircleCICredentialsUpdate, optional

        :param type: The definition of the ``CircleCIIntegrationType`` object.
        :type type: CircleCIIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
