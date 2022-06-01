# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsBatchDetailsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_ci_batch_metadata import SyntheticsCIBatchMetadata
        from datadog_api_client.v1.model.synthetics_batch_result import SyntheticsBatchResult
        from datadog_api_client.v1.model.synthetics_status import SyntheticsStatus

        return {
            "metadata": (SyntheticsCIBatchMetadata,),
            "results": ([SyntheticsBatchResult],),
            "status": (SyntheticsStatus,),
        }

    attribute_map = {
        "metadata": "metadata",
        "results": "results",
        "status": "status",
    }

    def __init__(self, *args, **kwargs):
        """
        Wrapper object that contains the details of a batch.

        :param metadata: Metadata for the Synthetics tests run.
        :type metadata: SyntheticsCIBatchMetadata, optional

        :param results: List of results for the batch.
        :type results: [SyntheticsBatchResult], optional

        :param status: Determines whether or not the batch has passed, failed, or is in progress.
        :type status: SyntheticsStatus, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsBatchDetailsData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
