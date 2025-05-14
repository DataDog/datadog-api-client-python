# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_google_cloud_storage_destination_acl import (
        ObservabilityPipelineGoogleCloudStorageDestinationAcl,
    )
    from datadog_api_client.v2.model.observability_pipeline_gcp_auth import ObservabilityPipelineGcpAuth
    from datadog_api_client.v2.model.observability_pipeline_metadata_entry import ObservabilityPipelineMetadataEntry
    from datadog_api_client.v2.model.observability_pipeline_google_cloud_storage_destination_storage_class import (
        ObservabilityPipelineGoogleCloudStorageDestinationStorageClass,
    )
    from datadog_api_client.v2.model.observability_pipeline_google_cloud_storage_destination_type import (
        ObservabilityPipelineGoogleCloudStorageDestinationType,
    )


class ObservabilityPipelineGoogleCloudStorageDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_google_cloud_storage_destination_acl import (
            ObservabilityPipelineGoogleCloudStorageDestinationAcl,
        )
        from datadog_api_client.v2.model.observability_pipeline_gcp_auth import ObservabilityPipelineGcpAuth
        from datadog_api_client.v2.model.observability_pipeline_metadata_entry import ObservabilityPipelineMetadataEntry
        from datadog_api_client.v2.model.observability_pipeline_google_cloud_storage_destination_storage_class import (
            ObservabilityPipelineGoogleCloudStorageDestinationStorageClass,
        )
        from datadog_api_client.v2.model.observability_pipeline_google_cloud_storage_destination_type import (
            ObservabilityPipelineGoogleCloudStorageDestinationType,
        )

        return {
            "acl": (ObservabilityPipelineGoogleCloudStorageDestinationAcl,),
            "auth": (ObservabilityPipelineGcpAuth,),
            "bucket": (str,),
            "id": (str,),
            "inputs": ([str],),
            "key_prefix": (str,),
            "metadata": ([ObservabilityPipelineMetadataEntry],),
            "storage_class": (ObservabilityPipelineGoogleCloudStorageDestinationStorageClass,),
            "type": (ObservabilityPipelineGoogleCloudStorageDestinationType,),
        }

    attribute_map = {
        "acl": "acl",
        "auth": "auth",
        "bucket": "bucket",
        "id": "id",
        "inputs": "inputs",
        "key_prefix": "key_prefix",
        "metadata": "metadata",
        "storage_class": "storage_class",
        "type": "type",
    }

    def __init__(
        self_,
        acl: ObservabilityPipelineGoogleCloudStorageDestinationAcl,
        auth: ObservabilityPipelineGcpAuth,
        bucket: str,
        id: str,
        inputs: List[str],
        storage_class: ObservabilityPipelineGoogleCloudStorageDestinationStorageClass,
        type: ObservabilityPipelineGoogleCloudStorageDestinationType,
        key_prefix: Union[str, UnsetType] = unset,
        metadata: Union[List[ObservabilityPipelineMetadataEntry], UnsetType] = unset,
        **kwargs,
    ):
        """
        The ``google_cloud_storage`` destination stores logs in a Google Cloud Storage (GCS) bucket.
        It requires a bucket name, GCP authentication, and metadata fields.

        :param acl: Access control list setting for objects written to the bucket.
        :type acl: ObservabilityPipelineGoogleCloudStorageDestinationAcl

        :param auth: GCP credentials used to authenticate with Google Cloud Storage.
        :type auth: ObservabilityPipelineGcpAuth

        :param bucket: Name of the GCS bucket.
        :type bucket: str

        :param id: Unique identifier for the destination component.
        :type id: str

        :param inputs: A list of component IDs whose output is used as the ``input`` for this component.
        :type inputs: [str]

        :param key_prefix: Optional prefix for object keys within the GCS bucket.
        :type key_prefix: str, optional

        :param metadata: Custom metadata to attach to each object uploaded to the GCS bucket.
        :type metadata: [ObservabilityPipelineMetadataEntry], optional

        :param storage_class: Storage class used for objects stored in GCS.
        :type storage_class: ObservabilityPipelineGoogleCloudStorageDestinationStorageClass

        :param type: The destination type. Always ``google_cloud_storage``.
        :type type: ObservabilityPipelineGoogleCloudStorageDestinationType
        """
        if key_prefix is not unset:
            kwargs["key_prefix"] = key_prefix
        if metadata is not unset:
            kwargs["metadata"] = metadata
        super().__init__(kwargs)

        self_.acl = acl
        self_.auth = auth
        self_.bucket = bucket
        self_.id = id
        self_.inputs = inputs
        self_.storage_class = storage_class
        self_.type = type
