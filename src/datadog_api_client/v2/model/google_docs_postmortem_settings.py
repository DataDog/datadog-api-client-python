# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class GoogleDocsPostmortemSettings(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "parent_folder_id": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "parent_folder_id": "parent_folder_id",
    }

    def __init__(self_, account_id: str, parent_folder_id: str, **kwargs):
        """
        Settings for a postmortem template stored in Google Docs. Required when ``location`` is ``google_docs``.

        :param account_id: The ID of the Google Drive integration account.
        :type account_id: str

        :param parent_folder_id: The ID of the Google Drive folder where postmortems are created.
        :type parent_folder_id: str
        """
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.parent_folder_id = parent_folder_id
