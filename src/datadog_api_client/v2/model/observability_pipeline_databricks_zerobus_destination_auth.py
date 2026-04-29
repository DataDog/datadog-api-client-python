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


class ObservabilityPipelineDatabricksZerobusDestinationAuth(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "client_id": (str,),
            "client_secret_key": (str,),
        }

    attribute_map = {
        "client_id": "client_id",
        "client_secret_key": "client_secret_key",
    }

    def __init__(self_, client_id: str, client_secret_key: Union[str, UnsetType] = unset, **kwargs):
        """
        OAuth credentials for authenticating with the Databricks Zerobus ingestion API.

        :param client_id: Your service principal application ID (UUID).
        :type client_id: str

        :param client_secret_key: Name of the environment variable or secret that holds the OAuth client secret used to authenticate with the Databricks ingestion endpoint.
        :type client_secret_key: str, optional
        """
        if client_secret_key is not unset:
            kwargs["client_secret_key"] = client_secret_key
        super().__init__(kwargs)

        self_.client_id = client_id
