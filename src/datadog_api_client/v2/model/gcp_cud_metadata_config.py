# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class GCPCudMetadataConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "dataset_id": (str,),
            "project_id": (str,),
            "table_id": (str,),
        }

    attribute_map = {
        "dataset_id": "dataset_id",
        "project_id": "project_id",
        "table_id": "table_id",
    }

    def __init__(self_, dataset_id: str, project_id: str, table_id: str, **kwargs):
        """
        The BigQuery table the committed use discount (CUD) metadata is read from. Only returned when CUD metadata is configured for the account.

        :param dataset_id: The BigQuery dataset ID of the CUD metadata export.
        :type dataset_id: str

        :param project_id: The Google Cloud project ID of the CUD metadata export.
        :type project_id: str

        :param table_id: The BigQuery table ID of the CUD metadata export.
        :type table_id: str
        """
        super().__init__(kwargs)

        self_.dataset_id = dataset_id
        self_.project_id = project_id
        self_.table_id = table_id
