# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsTestFileAbortMultipartUploadRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "key": (str,),
            "upload_id": (str,),
        }

    attribute_map = {
        "key": "key",
        "upload_id": "uploadId",
    }

    def __init__(self_, key: str, upload_id: str, **kwargs):
        """
        Request body for aborting a multipart file upload.

        :param key: The full storage path of the file whose upload should be aborted.
        :type key: str

        :param upload_id: The upload ID of the multipart upload to abort.
        :type upload_id: str
        """
        super().__init__(kwargs)

        self_.key = key
        self_.upload_id = upload_id
