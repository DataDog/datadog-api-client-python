# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_gateway_model_metadata_source_matched_by import (
        AiGatewayModelMetadataSourceMatchedBy,
    )


class AiGatewayModelMetadataSource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_gateway_model_metadata_source_matched_by import (
            AiGatewayModelMetadataSourceMatchedBy,
        )

        return {
            "matched_by": (AiGatewayModelMetadataSourceMatchedBy,),
            "model_id": (str,),
            "name": (str,),
            "observed_at": (datetime,),
            "provider": (str,),
            "revision": (str,),
        }

    attribute_map = {
        "matched_by": "matched_by",
        "model_id": "model_id",
        "name": "name",
        "observed_at": "observed_at",
        "provider": "provider",
        "revision": "revision",
    }

    def __init__(
        self_,
        matched_by: AiGatewayModelMetadataSourceMatchedBy,
        model_id: str,
        name: str,
        provider: str,
        observed_at: Union[datetime, UnsetType] = unset,
        revision: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Provenance for model metadata enrichment.

        :param matched_by: Identifier strategy used to match the gateway catalog entry. Date-suffix and shared canonical-model fallback matches produce partial metadata.
        :type matched_by: AiGatewayModelMetadataSourceMatchedBy

        :param model_id: Model identifier in the metadata source provider catalog.
        :type model_id: str

        :param name: Metadata source name.
        :type name: str

        :param observed_at: Last successful observation of this valid source record. Retained invalid entries keep their previous timestamp.
        :type observed_at: datetime, optional

        :param provider: Provider namespace in the metadata source, or canonical for a shared model record.
        :type provider: str

        :param revision: SHA-256 content revision of the source snapshot that supplied this record.
        :type revision: str, optional
        """
        if observed_at is not unset:
            kwargs["observed_at"] = observed_at
        if revision is not unset:
            kwargs["revision"] = revision
        super().__init__(kwargs)

        self_.matched_by = matched_by
        self_.model_id = model_id
        self_.name = name
        self_.provider = provider
