# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsCIBatchMetadataCI(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_ci_batch_metadata_pipeline import SyntheticsCIBatchMetadataPipeline
        from datadog_api_client.v1.model.synthetics_ci_batch_metadata_provider import SyntheticsCIBatchMetadataProvider

        return {
            "pipeline": (SyntheticsCIBatchMetadataPipeline,),
            "provider": (SyntheticsCIBatchMetadataProvider,),
        }

    attribute_map = {
        "pipeline": "pipeline",
        "provider": "provider",
    }

    def __init__(self, *args, **kwargs):
        """
        Description of the CI provider.

        :param pipeline: Description of the CI pipeline.
        :type pipeline: SyntheticsCIBatchMetadataPipeline, optional

        :param provider: Description of the CI provider.
        :type provider: SyntheticsCIBatchMetadataProvider, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsCIBatchMetadataCI, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
