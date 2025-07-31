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
    from datadog_api_client.v2.model.virus_total_credentials_update import VirusTotalCredentialsUpdate
    from datadog_api_client.v2.model.virus_total_integration_type import VirusTotalIntegrationType
    from datadog_api_client.v2.model.virus_total_api_key_update import VirusTotalAPIKeyUpdate


class VirusTotalIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.virus_total_credentials_update import VirusTotalCredentialsUpdate
        from datadog_api_client.v2.model.virus_total_integration_type import VirusTotalIntegrationType

        return {
            "credentials": (VirusTotalCredentialsUpdate,),
            "type": (VirusTotalIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: VirusTotalIntegrationType,
        credentials: Union[VirusTotalCredentialsUpdate, VirusTotalAPIKeyUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``VirusTotalIntegrationUpdate`` object.

        :param credentials: The definition of the ``VirusTotalCredentialsUpdate`` object.
        :type credentials: VirusTotalCredentialsUpdate, optional

        :param type: The definition of the ``VirusTotalIntegrationType`` object.
        :type type: VirusTotalIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
