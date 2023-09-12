# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CustomDestinationMetadata(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "custom_destinations_limit": (int,),
            "deleted_enclave_ids": ([str],),
        }

    attribute_map = {
        "custom_destinations_limit": "customDestinationsLimit",
        "deleted_enclave_ids": "deletedEnclaveIds",
    }

    def __init__(
        self_,
        custom_destinations_limit: Union[int, UnsetType] = unset,
        deleted_enclave_ids: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The metadata relevant to your configuration or recent request.

        :param custom_destinations_limit: The amount of custom destinations your organization is able to create.
        :type custom_destinations_limit: int, optional

        :param deleted_enclave_ids: The managed enclave IDs of the resource that is deleted.
        :type deleted_enclave_ids: [str], optional
        """
        if custom_destinations_limit is not unset:
            kwargs["custom_destinations_limit"] = custom_destinations_limit
        if deleted_enclave_ids is not unset:
            kwargs["deleted_enclave_ids"] = deleted_enclave_ids
        super().__init__(kwargs)
