# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SyntheticsTestFileMultipartPresignedUrlsParams(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "key": (str,),
            "upload_id": (str,),
            "urls": ({str: (str,)},),
        }

    attribute_map = {
        "key": "key",
        "upload_id": "upload_id",
        "urls": "urls",
    }

    def __init__(
        self_,
        key: Union[str, UnsetType] = unset,
        upload_id: Union[str, UnsetType] = unset,
        urls: Union[Dict[str, str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Presigned URL parameters returned for a multipart upload.

        :param key: The full storage path for the file being uploaded.
        :type key: str, optional

        :param upload_id: The upload ID assigned by the storage provider for this multipart upload.
        :type upload_id: str, optional

        :param urls: A map of part numbers to presigned upload URLs.
        :type urls: {str: (str,)}, optional
        """
        if key is not unset:
            kwargs["key"] = key
        if upload_id is not unset:
            kwargs["upload_id"] = upload_id
        if urls is not unset:
            kwargs["urls"] = urls
        super().__init__(kwargs)
