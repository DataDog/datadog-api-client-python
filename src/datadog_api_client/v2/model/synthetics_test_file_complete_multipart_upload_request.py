# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.synthetics_test_file_complete_multipart_upload_part import (
        SyntheticsTestFileCompleteMultipartUploadPart,
    )


class SyntheticsTestFileCompleteMultipartUploadRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.synthetics_test_file_complete_multipart_upload_part import (
            SyntheticsTestFileCompleteMultipartUploadPart,
        )

        return {
            "key": (str,),
            "parts": ([SyntheticsTestFileCompleteMultipartUploadPart],),
            "upload_id": (str,),
        }

    attribute_map = {
        "key": "key",
        "parts": "parts",
        "upload_id": "uploadId",
    }

    def __init__(self_, key: str, parts: List[SyntheticsTestFileCompleteMultipartUploadPart], upload_id: str, **kwargs):
        """
        Request body for completing a multipart file upload.

        :param key: The full storage path for the uploaded file.
        :type key: str

        :param parts: Array of completed parts with their ETags.
        :type parts: [SyntheticsTestFileCompleteMultipartUploadPart]

        :param upload_id: The upload ID returned when the multipart upload was initiated.
        :type upload_id: str
        """
        super().__init__(kwargs)

        self_.key = key
        self_.parts = parts
        self_.upload_id = upload_id
