# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItemsOutcome(ModelSimple):
    """
    Outcome of attempting to refresh one experiment.

    :param value: Must be one of ["TRIGGERED", "SKIPPED_ALREADY_RUNNING", "SKIPPED_NOT_EDITABLE", "SKIPPED_ORG_AT_CAPACITY", "FAILED"].
    :type value: str
    """

    allowed_values = {
        "TRIGGERED",
        "SKIPPED_ALREADY_RUNNING",
        "SKIPPED_NOT_EDITABLE",
        "SKIPPED_ORG_AT_CAPACITY",
        "FAILED",
    }
    TRIGGERED: ClassVar["ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItemsOutcome"]
    SKIPPED_ALREADY_RUNNING: ClassVar["ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItemsOutcome"]
    SKIPPED_NOT_EDITABLE: ClassVar["ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItemsOutcome"]
    SKIPPED_ORG_AT_CAPACITY: ClassVar["ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItemsOutcome"]
    FAILED: ClassVar["ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItemsOutcome"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItemsOutcome.TRIGGERED = (
    ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItemsOutcome("TRIGGERED")
)
ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItemsOutcome.SKIPPED_ALREADY_RUNNING = (
    ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItemsOutcome("SKIPPED_ALREADY_RUNNING")
)
ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItemsOutcome.SKIPPED_NOT_EDITABLE = (
    ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItemsOutcome("SKIPPED_NOT_EDITABLE")
)
ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItemsOutcome.SKIPPED_ORG_AT_CAPACITY = (
    ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItemsOutcome("SKIPPED_ORG_AT_CAPACITY")
)
ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItemsOutcome.FAILED = (
    ExperimentsRefreshExperimentResultsBatchMetaV2DTOResultsItemsOutcome("FAILED")
)
