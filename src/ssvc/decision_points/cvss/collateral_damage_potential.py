#!/usr/bin/env python
"""
file: collateral_damage_potential
author: adh
created_at: 9/20/23 1:48 PM
"""
from copy import deepcopy

from ssvc.decision_points.base import SsvcValue

NOT_DEFINED = SsvcValue(
    name="Not Defined",
    key="ND",
    description="Assigning this value to the metric will not influence the score. It is a signal to the equation to skip this metric.",
)

MEDIUM_HIGH = SsvcValue(
    name="Medium-High",
    key="MH",
    description="A successful exploit of this vulnerability may result in significant physical or property damage or loss.",
)

LOW_MEDIUM = SsvcValue(
    name="Low-Medium",
    key="LM",
    description="A successful exploit of this vulnerability may result in moderate physical or property damage or loss.",
)

CDP_NONE_2 = SsvcValue(
    name="None",
    key="N",
    description="There is no potential for loss of life, physical assets, productivity or revenue.",
)

HIGH = SsvcValue(
    name="High",
    key="H",
    description="A successful exploit of this vulnerability may result in catastrophic physical or property damage and loss. The range of effect may be over a wide area.",
)

MEDIUM = SsvcValue(
    name="Medium",
    key="M",
    description="A successful exploit of this vulnerability may result in significant physical or property damage or loss.",
)

LOW = SsvcValue(
    name="Low",
    key="L",
    description="A successful exploit of this vulnerability may result in light physical or property damage or loss. The system itself may be damaged or destroyed.",
)
from ssvc.decision_points.cvss.base import CvssDecisionPoint

CDP_NONE = SsvcValue(
    name="None",
    key="N",
    description="There is no potential for physical or property damage.",
)


COLLATERAL_DAMAGE_POTENTIAL_1 = CvssDecisionPoint(
    name="Collateral Damage Potential",
    description="This metric measures the potential for a loss in physical equipment, property damage or loss of life or limb.",
    key="CDP",
    version="1.0.0",
    values=(
        CDP_NONE,
        LOW,
        MEDIUM,
        HIGH,
    ),
)

COLLATERAL_DAMAGE_POTENTIAL_2 = deepcopy(COLLATERAL_DAMAGE_POTENTIAL_1)
COLLATERAL_DAMAGE_POTENTIAL_2.version = "2.0.0"
COLLATERAL_DAMAGE_POTENTIAL_2.values = (
    CDP_NONE_2,
    LOW,
    LOW_MEDIUM,
    MEDIUM_HIGH,
    HIGH,
    NOT_DEFINED,
)


def main():
    print(COLLATERAL_DAMAGE_POTENTIAL_1.to_json(indent=2))
    print(COLLATERAL_DAMAGE_POTENTIAL_2.to_json(indent=2))


if __name__ == "__main__":
    main()
