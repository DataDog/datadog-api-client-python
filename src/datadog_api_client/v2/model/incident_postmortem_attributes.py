# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.postmortem_status import PostmortemStatus


class IncidentPostmortemAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.postmortem_status import PostmortemStatus

        return {
            "created": (datetime,),
            "document_id": (str,),
            "document_type": (str,),
            "document_url": (str,),
            "modified": (datetime,),
            "status": (PostmortemStatus,),
            "title": (str,),
        }

    attribute_map = {
        "created": "created",
        "document_id": "document_id",
        "document_type": "document_type",
        "document_url": "document_url",
        "modified": "modified",
        "status": "status",
        "title": "title",
    }

    def __init__(
        self_,
        created: datetime,
        document_id: str,
        document_type: str,
        document_url: str,
        modified: datetime,
        status: PostmortemStatus,
        title: str,
        **kwargs,
    ):
        """
        The postmortem's attributes.

        :param created: Timestamp when the postmortem was created.
        :type created: datetime

        :param document_id: The identifier of the postmortem document within its host platform.
        :type document_id: str

        :param document_type: The type of document backing the postmortem (for example, ``datadog_notebooks`` , ``confluence`` , or ``google_docs`` ). Can be empty if the document type is unknown.
        :type document_type: str

        :param document_url: The URL of the postmortem document.
        :type document_url: str

        :param modified: Timestamp when the postmortem was last modified.
        :type modified: datetime

        :param status: The status of the postmortem.
        :type status: PostmortemStatus

        :param title: The title of the postmortem.
        :type title: str
        """
        super().__init__(kwargs)

        self_.created = created
        self_.document_id = document_id
        self_.document_type = document_type
        self_.document_url = document_url
        self_.modified = modified
        self_.status = status
        self_.title = title
