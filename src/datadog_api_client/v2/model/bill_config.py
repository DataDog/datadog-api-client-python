# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class BillConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "export_name": (str,),
            "export_path": (str,),
            "storage_account": (str,),
            "storage_container": (str,),
        }

    attribute_map = {
        "export_name": "export_name",
        "export_path": "export_path",
        "storage_account": "storage_account",
        "storage_container": "storage_container",
    }

    def __init__(self_, export_name: str, export_path: str, storage_account: str, storage_container: str, **kwargs):
        """
        Bill config.

        :param export_name: The name of the configured Azure Export.
        :type export_name: str

        :param export_path: The path where the Azure Export is saved.
        :type export_path: str

        :param storage_account: The name of the storage account where the Azure Export is saved.
        :type storage_account: str

        :param storage_container: The name of the storage container where the Azure Export is saved.
        :type storage_container: str
        """
        super().__init__(kwargs)

        self_.export_name = export_name
        self_.export_path = export_path
        self_.storage_account = storage_account
        self_.storage_container = storage_container
