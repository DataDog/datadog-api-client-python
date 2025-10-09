# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class PatchTableRequestDataAttributesFileMetadataLocalFile(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "upload_id": (str,),
        }

    attribute_map = {
        "upload_id": "upload_id",
    }

    def __init__(self_, upload_id: str, **kwargs):
        """
        Local file metadata for patch requests using upload ID.

        :param upload_id: The upload ID.
        :type upload_id: str
        """
        super().__init__(kwargs)

        self_.upload_id = upload_id
