# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class OCIConfigAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "created_at": (str,),
            "error_messages": ([str], none_type),
            "status": (str,),
            "status_updated_at": (str,),
            "updated_at": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "created_at": "created_at",
        "error_messages": "error_messages",
        "status": "status",
        "status_updated_at": "status_updated_at",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        account_id: str,
        created_at: str,
        status: str,
        status_updated_at: str,
        updated_at: str,
        error_messages: Union[List[str], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for an OCI config.

        :param account_id: The OCID of the OCI tenancy.
        :type account_id: str

        :param created_at: The timestamp when the OCI config was created.
        :type created_at: str

        :param error_messages: The error messages for the OCI config.
        :type error_messages: [str], none_type, optional

        :param status: The status of the OCI config.
        :type status: str

        :param status_updated_at: The timestamp when the OCI config status was last updated.
        :type status_updated_at: str

        :param updated_at: The timestamp when the OCI config was last updated.
        :type updated_at: str
        """
        if error_messages is not unset:
            kwargs["error_messages"] = error_messages
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.created_at = created_at
        self_.status = status
        self_.status_updated_at = status_updated_at
        self_.updated_at = updated_at
